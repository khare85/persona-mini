# Resume Matcher with Qdrant Cloud

Match resumes to job descriptions using semantic search and vector embeddings.

## 🔧 Features

- Parse PDF, DOCX, TXT, and scanned image resumes (OCR)
- Store resume vectors in Qdrant Cloud
- Match job descriptions to top candidates
- Skill extraction using spaCy

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm