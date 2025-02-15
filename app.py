from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
import sys
sys.path.append("./src")
from json_func import read_json, write_comp_to_json 


app = Flask(__name__)

# Save data to the .json file
def save_classes(data):
    write_comp_to_json(data)

# Load the initial class data
classes = read_json()

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
