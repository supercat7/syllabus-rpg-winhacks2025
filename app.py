from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for class data (use a database for persistence)
classes = []

@app.route('/')
def index():
    return render_template('index.html', classes=classes)

@app.route('/add_class', methods=['POST'])
def add_class():
    title = request.form.get('title')
    weight = request.form.get('weight')
    due_date = request.form.get('dueDate')
    
    if title and weight and due_date:
        # Add the class data to the list (or save to a database)
        classes.append({
            'title': title,
            'weight': weight,
            'due_date': due_date
        })
        return redirect(url_for('index'))
    return "Missing data", 400

if __name__ == '__main__':
    app.run(debug=True)