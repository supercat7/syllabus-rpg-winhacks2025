from flask import Flask, render_template, request, jsonify
import sys
sys.path.append("./src")
import json_func

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)