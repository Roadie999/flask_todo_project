from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Define your route
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Optional home route
@app.route('/')
def home():
    return "Hello, Flask with JSON API!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
