import os
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document
import PyPDF2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith('.txt'):
        return file.read().decode('utf-8')

    elif filename.endswith('.docx'):
        doc = Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])

    elif filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text

    else:
        return "Unsupported file type"

@app.route('/compare', methods=['POST'])
def compare_files():
    file1 = request.files['file1']
    file2 = request.files['file2']

    text1 = extract_text(file1)
    text2 = extract_text(file2)

    if "Unsupported" in text1 or "Unsupported" in text2:
        return "One or both files are not supported. Please upload .txt, .docx, or .pdf files."

    texts = [text1, text2]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return render_template('result.html', similarity=round(similarity_score * 100, 2))

# Port binding for Render
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
