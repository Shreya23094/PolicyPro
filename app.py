from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from FullPolicyAnalysis import FullPolicyAnalysis
import streamlit as st
from dotenv import load_dotenv
import PyPDF2

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="PolicyPro", layout="centered")
st.header("📄 PolicyPro")
st.markdown("Extract structured information from insurance policies accurately and efficiently.")
st.markdown("For more details, the reference implementation is available on :[GitHub](https://github.com/Shreya23094/PolicyPro)")

# File/Content Input
options = ['-- Select an option --', 'Upload a File', 'Type in the content']
document_content = ""


content_type = st.selectbox("Choose how you'd like to provide the content:", options)
if content_type == 'Upload a File':
    document = st.file_uploader("Upload the policy document (PDF or TXT).", type=['pdf', 'txt'])
    if document is not None:
        if document.type == "application/pdf":
            try:
                pdf_reader = PyPDF2.PdfReader(document)
                document_content = ""
                for page in pdf_reader.pages:
                    document_content += page.extract_text() + "\n"
            except Exception as e:
                st.error(f"❌ Failed to read PDF: {e}")
        elif document.type == "text/plain":
            try:
                document_content = document.read().decode('utf-8')
            except Exception as e:
                st.error(f"❌ Failed to decode text file: {e}")
        else:
            st.error("Unsupported file format. Please upload a PDF or plain text (.txt) file.")
elif content_type == 'Type in the content':
    document_content = st.text_area("Enter the policy content to be analyzed:")
    
else:
    st.info("ℹ️ Please select an input type to continue.")

# Initialize LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Pydantic Output Parser
parser = PydanticOutputParser(pydantic_object=FullPolicyAnalysis)

# Prompt Template
template = PromptTemplate(
    template="""
You are a professional insurance policy analysis AI.

Extract structured information from the policy document below.
You MUST strictly follow the schema instructions.

{format_instructions}

SECTION REQUIREMENTS (VERY IMPORTANT):

summary (object):
- policy_name: string
- policy_number: string
- issuer: string
- effective_date: YYYY-MM-DD or null
- expiry_date: YYYY-MM-DD or null
- overview: string

coverages (list of objects):
Each item must include:
- title: string
- description: string

eligibility (object):
- criteria: list of strings

claim_procedures (list of objects):
Each item must include:
- step_number: integer
- description: string

obligations (object):
- responsibilities: list of strings

terms_and_conditions (object):
- clauses: list of strings

contact_information (object):
- company_name: string
- phone: string or null
- email: string or null
- website: string or null

other_sections (object):
- key-value pairs where key is section title and value is section text

RULES:
- Do NOT invent information
- If data is missing, use null or empty lists
- Dates MUST be YYYY-MM-DD
- Output must EXACTLY match the schema

Policy Document:
---
{document_content}
---
""",
    input_variables=["document_content"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


chain = template | model | parser

if st.button("Generate Summary"):
    if content_type == "-- Select an option --" or not document_content.strip():
        st.warning("Please provide policy content.")
    else:
        with st.spinner("Analyzing policy document..."):
            try:
                result: FullPolicyAnalysis = chain.invoke(
                    {"document_content": document_content}
                )

                st.subheader("📤 Structured Output")

                st.markdown("### 🔹 Summary")
                st.write(result.summary)

                st.markdown("### 🔹 Coverages")
                st.write(result.coverages)

                st.markdown("### 🔹 Eligibility")
                st.write(result.eligibility)

                st.markdown("### 🔹 Claim Procedures")
                st.write(result.claim_procedures)

                st.markdown("### 🔹 Obligations")
                st.write(result.obligations)

                st.markdown("### 🔹 Terms and Conditions")
                st.write(result.terms_and_conditions)

                st.markdown("### 🔹 Contact Information")
                st.write(result.contact_information)

                st.markdown("### 🔹 Other Sections")
                st.write(result.other_sections)

            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")
