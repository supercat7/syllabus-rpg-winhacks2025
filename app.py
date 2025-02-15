from flask import Flask, render_template, request, jsonify
import sys
sys.path.append("./src")
import json_func  # Import your function to write to comp.json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_class', methods=['POST'])
def add_class():
    try:
        data = request.get_json()  # Receive JSON data from the frontend
        current_data = {}

        # Read existing data if the JSON file already exists
        try:
            current_data = json_func.read_json()
        except FileNotFoundError:
            current_data = {}

        # Merge the new data with the existing data
        current_data.update(data)

        # Write the updated data back to comp.json
        json_func.write_comp_to_json(current_data)
        return jsonify({"message": "Class added successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to add class"}), 500

if __name__ == '__main__':
    app.run(debug=True)
