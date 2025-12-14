import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import json
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
You are an information extraction AI.

Read the policy text and RETURN ONE JSON OBJECT
that matches EXACTLY this example structure.

IMPORTANT:
- Use the SAME keys as the example
- Do NOT explain anything
- Do NOT include schema definitions
- Do NOT include extra keys
- Use null if information is missing
- Dates must be YYYY-MM-DD

EXAMPLE OUTPUT (FORMAT ONLY — values will differ):

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
  "coverages": [
    {
      "section_name": "Coverage Section",
      "coverages": [
        {
          "name": "Coverage name",
          "description": "Coverage description",
          "limits": null,
          "deductible": null,
          "conditions": null,
          "exclusions": null
        }
      ]
    }
  ],
  "eligibility": {
    "section_name": "Eligibility",
    "criteria": [
      {
        "criterion": "Condition",
        "details": "Details",
        "is_required": true
      }
    ],
    "notes": null
  },
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
raw = chain.invoke({"document": document}).content


data = json.loads(raw)
result = FullPolicyAnalysis.model_validate(data)


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
