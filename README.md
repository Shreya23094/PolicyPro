# 📄 PolicyAnalyzer – AI-Powered Insurance Policy Understanding

> **"Revolutionize how people read and understand insurance policies using the power of Generative AI and LangChain."**

---

## 💻 Link for the Live Deployment
[policypro.streamlit.app](https://policypro.streamlit.app/)

## 🚀 Why I Created This Project

In today's fast-moving world, **insurance policies are critical yet extremely hard to understand**. People often:
- Sign documents without knowing the *terms and conditions*,
- Miss out on *coverage details or claim procedures*,
- Or simply *don’t know their rights and obligations*.

**I created PolicyAnalyzer** to simplify this complexity using **AI**, making insurance documents **transparent, interactive, and user-friendly**. No more confusion, legal jargon, or missed clauses—just **clarity and confidence**.

---

## 🧠 What is PolicyAnalyzer?

PolicyAnalyzer is a **Streamlit-based web app** powered by:
- 🧠 **LangChain + Hugging Face (Gemma-2B-IT)** for natural language understanding,
- 🛠️ **Pydantic Output Parsers** for structured extraction,
- 📄 **PDF/Text File Upload** and analysis,
- 📊 **Tabular display of AI-processed key information**.

It reads long policy documents and **outputs structured, accurate, and meaningful summaries** that anyone can understand.

---

## 🔥 Features

| Feature | Description |
|--------|-------------|
| 📁 **Upload or Type Content** | Upload insurance policy documents (PDFs) or paste text manually |
| 🧠 **AI-Powered Extraction** | Uses Hugging Face + LangChain to parse content and extract structure |
| 📝 **Structured Summary** | Outputs clean summaries: Coverages, Eligibility, Claims, Terms, and more |
| 📊 **Tabular Display** | Key-value insights shown in an elegant table format |
| 📤 **Raw JSON Output** | See and debug the raw LLM output if needed |
| ⚙️ **Pydantic Validation** | Ensures every field follows schema and fails gracefully |
| 🌐 **Real-World Ready** | Built for insurance providers, legal analysts, startups, or anyone dealing with policies |

---

## 🌍 Real-Life Impact

### 🏥 For Individuals:
> No more being overwhelmed by pages of policy clauses. Know what's covered and what's not, instantly.

### 🧑‍⚖️ For Legal & Compliance:
> AI-driven document extraction saves hours of manual clause reading and ensures regulatory clarity.

### 🏢 For Insurers & Agents:
> Automate policy explanation and improve customer experience with zero human error.

### 📚 For Educators:
> A perfect tool to teach AI-driven NLP, document parsing, legal-tech, and real-world LangChain applications.

---

## 🛠 Tech Stack

- 🧠 **LLM**: [`google/gemma-2-2b-it`](https://huggingface.co/google/gemma-2-2b-it) via HuggingFace Endpoint
- 🔗 **LangChain**: PromptTemplate, HuggingFaceEndpoint, OutputParser
- 📄 **PDF Parsing**: `PyPDF2`
- ⚙️ **Pydantic Models**: Full policy schema including summaries, obligations, clauses, contacts, and more
- 🌐 **Streamlit**: Interactive frontend UI
- 🧪 **dotenv**: For secure API key management

---


