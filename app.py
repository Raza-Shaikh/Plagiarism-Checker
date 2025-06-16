import os
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_files():
    file1 = request.files['file1']
    file2 = request.files['file2']

    text1 = file1.read().decode('utf-8')
    text2 = file2.read().decode('utf-8')

    texts = [text1, text2]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return render_template('result.html', similarity=round(similarity_score * 100, 2))

import os

port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT not set
app.run(host="0.0.0.0", port=port)

