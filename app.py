from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Create the Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.todo_db
collection = db.todo_items

# Frontend route (To-Do page)
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Backend API route to submit To-Do items
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return {"message": "Both fields are required"}, 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return {"message": "To-Do item added successfully!"}, 200

# Home route
@app.route('/')
def home():
    return "Hello, Flask with JSON API!"

if __name__ == '__main__':
    app.run(debug=True)
