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
import point

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

# Route for adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        # Get task details from the request
        data = request.get_json()
        task_name = data['task_name']
        weight = data['weight']
        due_date = data['due_date']

        # Create the task dictionary with the Grade field
        new_task = {
            "Assignment": task_name,
            "Weight (%)": f"{weight}%",
            "Due Date": due_date,
            "Grade": ""  # Grade is initially empty
        }

        # Append to the existing tasks in the JSON file
        append_to_json([new_task])

        # Return success message
        return jsonify({"message": "Task added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to add task: {e}"}), 500

# Route for entering a grade
@app.route('/enter_grade', methods=['POST'])
def enter_grade():
    data = request.get_json()
    assignment_name = data.get('assignment_name')
    grade = float(data.get('grade'))
    
    assignment = get_assignment_by_name(assignment_name)
    if not assignment:
        return jsonify({"success": False, "message": "Assignment not found"})
    
    weight = float(assignment["Weight (%)"].replace('%', ''))  # Extract weight as a number
    points = grade_to_point(grade, weight)
    
    # Update the assignment with the calculated points
    assignment["Grade"] = points
    
    # Remove the assignment from the list
    data = read_json()
    for assignment_group in data:
        if assignment in assignment_group:
            assignment_group.remove(assignment)
            break
    
    # Save the updated JSON
    with open('./data/comp.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    # Update points in the points.json file (if needed)
    current_points = get_point()  # Get current points
    new_points = current_points + points
    set_point(new_points)
    
    return jsonify({"success": True, "message": "Grade entered successfully!"})

# Route for parsing the syllabus
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
