from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from FullPolicyAnalysis import FullPolicyAnalysis
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
import json

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
You are a meticulous policy analysis AI.
Read the full document and extract structured information in JSON format using this structure:

Fields to extract:
- summary: a high-level overview of the policy
- coverages: list of coverage details
- eligibility: who is eligible for the policy
- claim_procedures: steps to file a claim
- obligations: responsibilities of the policyholder
- terms_and_conditions: key clauses of the policy
- contact_information: how to contact the issuer
- other_sections: any extra section not categorized

Rules:
- If a field is missing in the document, set it to null or an empty list.
- Do NOT fabricate data.
- Dates must be in YYYY-MM-DD format.
- Output should be valid, raw JSON. No markdown or triple backticks.

Policy Document:
---
{document_content}
---

Respond ONLY with valid JSON.
""",
    input_variables=["document_content"]
)

chain = template | model

if st.button('Generate Summary'):
    if content_type == '-- Select an option --' or not document_content.strip():
        st.warning("Please complete all required fields before generating the summary.")
    else:
        with st.spinner("Analyzing policy document..."):
            try:
                raw_output = chain.invoke({"document_content": document_content})
                llm_output = raw_output.content.strip()

                # Clean triple backticks or markdown if present
                cleaned_output = llm_output.strip().removeprefix("```json").removesuffix("```").strip()

                # Try parsing the cleaned output
                parsed_output = json.loads(cleaned_output)

                st.subheader("📤 Structured Output (Table View)")
                for key, value in parsed_output.items():        
                    st.markdown(f"### 🔹 {key}")
                    st.write(value)

            except json.JSONDecodeError as e:
                st.error(f"❌ Invalid JSON returned by the model: {str(e)}")

            except Exception as e:
                st.error(f"⚠️ Unexpected Error: {str(e)}")
