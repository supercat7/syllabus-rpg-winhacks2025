from flask import Flask, render_template, request, jsonify
import json
import os
import sys
import webbrowser
sys.path.append("./src")
from json_func import read_json, write_comp_to_json 
import chardet
from ai_func import *
import fitz

app = Flask(__name__)

#Route for the home page 
@app.route('/') 
def index():
    return render_template('index.html')

#Route for the profile page 
@app.route('/profile')
def profile():
    return render_template('profile.html')

#route for the To-Do-List page
@app.route('/todo')
def todo():
    return render_template('todo.html')

#Route for adding a class
@app.route('/add_class', methods=['POST'])
def add_class():
    try:
        # Parse the incoming JSON request
        new_class = request.get_json()
        print(f"Received new class data: {new_class}")  # Debugging

        if not new_class:
            return jsonify({"error": "No data provided"}), 400
        
        write_comp_to_json(new_class)
        return jsonify({"message": "Class added successfully"}), 200
    except Exception as e:
        print(f"Error in /add_class route: {e}")  # Debugging
        return jsonify({"error": "Failed to add class", "message": str(e)}), 500


@app.route('/parse_syllabus', methods=['POST'])
def parse_syllabus():
    if 'syllabusFile' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['syllabusFile']
    
    pdf_file = file.read()
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    
    syllabus_text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        syllabus_text += page.get_text()
  
    parsed_data = parse_syllabus_with_ai(syllabus_text)


if __name__ == '__main__':
    app.run(debug=True)