from flask import Flask, render_template, request, jsonify
import sys
sys.path.append("./src")
import json_func

# Initialize the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return render_template('index.html')
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
