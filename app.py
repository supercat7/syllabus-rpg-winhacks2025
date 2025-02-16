from flask import Flask, render_template, request, jsonify
import json
import os
import sys
import webbrowser
sys.path.append("./src")
from json_func import read_json, append_to_json, get_assignment_by_name, load_all_assignments
import chardet
from ai_func import *
import fitz
from point import *
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    update_level()
    return render_template('profile.html')

@app.route('/todo')
def todo():
    assignments_dict = load_all_assignments()  # Load assignments from JSON file
    return render_template('todo.html', assignments=assignments_dict)

@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        data = request.get_json()
        task_name = data['task_name']
        weight = data['weight']
        due_date = data['due_date']

        new_task = {
            "Assignment": task_name,
            "Weight (%)": f"{weight}%",
            "Due Date": due_date,
            "Grade": ""  # Grade is initially empty
        }

        current_data = read_json()
        
        current_data.append([new_task])
        
        with open('./data/comp.json', 'w') as file:
            json.dump(current_data, file, indent=4)

        return jsonify({"message": "Task added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to add task: {e}"}), 500



@app.route('/enter_grade', methods=['POST'])
def enter_grade():
    try:
        data = request.get_json()  # Get the request JSON data
        assignment_name = data.get('assignment_name')  # Get assignment name from the request
        grade = float(data.get('grade'))  # Get the grade and ensure it's a float

        # Read the current data from the JSON file
        assignments_data = read_json()

        # Flag to check if we found the assignment
        assignment_found = False

        # Loop through all assignment groups
        for assignment_group in assignments_data:
            for assignment in assignment_group:
                if assignment.get("Assignment") == assignment_name:
                    # Update the grade if assignment is found
                    assignment["Grade"] = grade
                    assignment_found = True
                    break

            if assignment_found:
                break

        # If no assignment was found, return an error response
        if not assignment_found:
            return jsonify({"success": False, "message": "Assignment not found"}), 404

        # Write the updated data back to the JSON file
        with open(datapath, 'w') as file:
            json.dump(assignments_data, file, indent=4)

        return jsonify({"success": True, "message": "Grade entered successfully!"})

    except Exception as e:
        return jsonify({"error": f"Failed to enter grade: {e}"}), 500


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
    
    del parsed_data[0]
    append_to_json(parsed_data)
    return jsonify({"data": parsed_data})

if __name__ == '__main__':
    app.run(debug=True)
