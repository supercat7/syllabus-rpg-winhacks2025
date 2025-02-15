from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
import sys
sys.path.append("./src")
from json_func import read_json, write_comp_to_json 


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
