import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

from FullPolicyAnalysis import FullPolicyAnalysis
from postprocess import (
    normalize_coverages,
    normalize_claims,
    normalize_obligations
)

load_dotenv()

st.set_page_config("PolicyPro", layout="centered")
st.header("📄 PolicyPro")
st.caption("Structured insurance policy analysis using LLMs")

document = st.text_area("Paste policy text here")

# LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = PydanticOutputParser(pydantic_object=FullPolicyAnalysis)

prompt = PromptTemplate(
    template="""
Extract structured information from the policy text below.

{format_instructions}

Rules:
- Do NOT invent information
- Use null when data is missing
- Dates must be YYYY-MM-DD

Policy Text:
---
{document}
---
""",
    input_variables=["document"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser

if st.button("Analyze Policy"):
    if not document.strip():
        st.warning("Please paste a policy document.")
    else:
        with st.spinner("Analyzing..."):
            try:
                result = chain.invoke({"document": document})

                # Post-process
                result.coverages = normalize_coverages(result.coverages)
                result.claim_procedures = normalize_claims(result.claim_procedures)
                result.obligations = normalize_obligations(result.obligations)

                # -------- DISPLAY --------
                st.subheader("📌 Summary")
                st.write(result.summary.summary)

                st.subheader("📦 Coverages")
                for sec in result.coverages or []:
                    st.markdown(f"**{sec.section_name}**")
                    for c in sec.coverages or []:
                        st.write("•", c.description)

                st.subheader("📋 Eligibility")
                if result.eligibility and result.eligibility.criteria:
                    for e in result.eligibility.criteria:
                        st.write("•", e.details or e.criterion)

                st.subheader("📝 Claim Procedures")
                for p in result.claim_procedures or []:
                    st.markdown(f"**{p.procedure_name}**")
                    for s in p.steps or []:
                        st.write(f"{s.step_number}. {s.description}")

                st.success("Analysis completed successfully ✅")

            except Exception as e:
                st.error(f"Failed to analyze document: {e}")
