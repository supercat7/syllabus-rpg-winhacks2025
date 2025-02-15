from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return render_template('index.html')  # Make sure to have an index.html in your templates folder

# Example of handling a POST request
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']  # Assuming form data is passed with key 'data'
    return jsonify({"message": f"Data received: {data}"}), 200

# Define an API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a sample response from API"}), 200

# Error handling route
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
