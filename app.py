from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from FullPolicyAnalysis import FullPolicyAnalysis
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
import json

# Load environment variables
load_dotenv()

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="PolicyPro", layout="centered")
st.header("📄 PolicyPro")
st.markdown("Extract structured information from insurance policies accurately and efficiently.")
st.markdown("For more details, the reference implementation is available on :[GitHub](https://github.com/Shreya23094/PolicyPro)")

# ---------------- INPUT ----------------
options = ['-- Select an option --', 'Upload a File', 'Type in the content']
document_content = ""

content_type = st.selectbox("Choose how you'd like to provide the content:", options)

if content_type == 'Upload a File':
    document = st.file_uploader("Upload the policy document (PDF or TXT).", type=['pdf', 'txt'])
    if document is not None:
        if document.type == "application/pdf":
            try:
                pdf_reader = PyPDF2.PdfReader(document)
                document_content = "\n".join(
                    page.extract_text() or "" for page in pdf_reader.pages
                )
            except Exception as e:
                st.error(f"❌ Failed to read PDF: {e}")
        elif document.type == "text/plain":
            document_content = document.read().decode("utf-8")

elif content_type == 'Type in the content':
    document_content = st.text_area("Enter the policy content to be analyzed:", height=300)

else:
    st.info("ℹ️ Please select an input type to continue.")

# ---------------- LLM ----------------
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# ---------------- PROMPT (CRITICAL FIX) ----------------
prompt = PromptTemplate(
    template="""
You are an information extraction AI.

Read the policy text and RETURN ONE JSON OBJECT
that matches EXACTLY the structure shown below.

IMPORTANT:
- Do NOT explain anything
- Do NOT describe schemas or classes
- Do NOT include extra keys
- Use null if information is missing
- Dates must be YYYY-MM-DD
- Output ONLY valid JSON (no markdown)

EXAMPLE OUTPUT FORMAT (values are examples only):

{
  "summary": {
    "policy_name": "Example Policy",
    "policy_type": "Health Insurance",
    "policy_id": "ABC-123",
    "effective_date": "2024-01-01",
    "expiration_date": "2025-01-01",
    "issuing_entity": "Example Insurance Co.",
    "summary": "Short summary text",
    "last_updated": null,
    "source_url": null,
    "key_definitions": null,
    "table_of_contents": null
  },
  "coverages": null,
  "eligibility": null,
  "claim_procedures": null,
  "obligations": null,
  "contact_information": null,
  "other_sections": null
}

NOW PRODUCE REAL DATA FOR THIS POLICY:

---
{document}
---
""",
    input_variables=["document"]
)

chain = prompt | model

# ---------------- BUTTON ----------------
if st.button("Generate Summary"):
    if not document_content.strip():
        st.warning("Please provide policy content.")
    else:
        with st.spinner("Analyzing policy document..."):
            try:
                raw_output = chain.invoke({"document": document_content}).content.strip()

                # Remove accidental markdown if present
                raw_output = raw_output.removeprefix("```json").removesuffix("```").strip()

                data = json.loads(raw_output)

                # OPTIONAL: validate after generation
                validated = FullPolicyAnalysis.model_validate(data)

                st.subheader("📤 Structured Output")

                for key, value in validated.model_dump().items():
                    st.markdown(f"### 🔹 {key}")
                    st.write(value)

            except json.JSONDecodeError as e:
                st.error("❌ Model did not return valid JSON.")
                st.code(raw_output)

            except Exception as e:
                st.error(f"⚠️ Failed to analyze document: {e}")
