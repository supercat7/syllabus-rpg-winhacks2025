from flask import Flask, render_template, request, jsonify
import json
import os
import sys
import webbrowser
sys.path.append("./src")
from json_func import read_json, write_comp_to_json 

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

if __name__ == '__main__':
    # Open the browser automatically
    webbrowser.open_new('http://127.0.0.1:5000')
    app.run(debug=True)