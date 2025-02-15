from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to your local .json file
JSON_FILE_PATH = 'classes.json'

# Load existing data from the .json file or initialize an empty list
def load_classes():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Save data to the .json file
def save_classes(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# Load the initial class data
classes = load_classes()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_class', methods=['POST'])
def add_class():
    try:
        # Parse the incoming JSON request
        new_class = request.get_json()
        
        if not new_class:
            return jsonify({"error": "No data provided"}), 400
        
        # Merge the new class data with the existing data
        classes.update(new_class)
        save_classes(classes)  # Save updated data to the .json file
        
        return jsonify({"message": "Class added successfully"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to add class"}), 500

if __name__ == '__main__':
    app.run(debug=True)
