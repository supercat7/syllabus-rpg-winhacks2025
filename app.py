from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from docx import Document
import PyPDF2
import os
from ai import parse_syllabus_with_ai  # Import the function from ai.py

app = Flask(__name__)

@app.route('/parse_syllabus', methods=['POST'])
def parse_syllabus():
    if 'syllabusFile' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['syllabusFile']
    filename = secure_filename(file.filename)
    
    if filename.endswith('.docx'):
        text = extract_text_from_docx(file)
    elif filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    # Pass the extracted text to the AI for parsing
    extracted_data = parse_syllabus_with_ai(text)
    return jsonify({"data": extracted_data})

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

if __name__ == '__main__':
    app.run(debug=True)
