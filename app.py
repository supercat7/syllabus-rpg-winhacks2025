from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from docx import Document
import PyPDF2
import os
from ai import parse_syllabus_with_ai  # Import the function from ai.py

app = Flask(__name__)
datapath = "./data/comp.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_class', methods=['POST'])
def add_class():
    try:
        new_class = request.get_json()
        print(f"Received new class data: {new_class}")  # Print the incoming data

        if not new_class:
            return jsonify({"error": "No data provided"}), 400
        
        write_comp_to_json(new_class)
        return jsonify({"message": "Class added successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to add class", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
