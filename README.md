# 📝 Plagiarism Checker

A web-based plagiarism checker built using **Flask** and **Scikit-learn**.  
Upload two documents (supports `.txt`, `.docx`, and `.pdf`) and instantly see the percentage of similarity between them using **TF-IDF** and **Cosine Similarity**.

---

## 🚀 Live Demo

🔗 [Click here to try the app online](https://plagiarism-checker-3zzv.onrender.com)

---

## 📂 Features

- Upload and compare two files (`.txt`, `.docx`, or `.pdf`)
- Processes and extracts raw text from uploaded documents
- Calculates similarity using Natural Language Processing (NLP)
- Shows percentage match using **TF-IDF** + **Cosine Similarity**
- Clean and easy-to-use interface

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Scikit-learn**
- **PyMuPDF** (`fitz`) – for PDF text extraction
- **python-docx** – for DOCX support
- **HTML/CSS (Jinja2 templates)**
- **Deployed on Render**

---

## 📦 Installation (Local Setup)

1. Clone the repository:
   git clone https://github.com/Raza-Shaikh/Plagiarism-Checker.git
   cd Plagiarism-Checker


2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

---

## 📁 File Structure:
Plagiarism-Checker/
│
├── templates/
│   ├── index.html
│   └── result.html
├── demo1.txt
├── demo2.txt
├── app.py
├── requirements.txt
├── render.yaml
└── README.md
