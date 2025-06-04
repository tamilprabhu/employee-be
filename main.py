from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample employee data (could be from a database in real apps)
employees = [
    {"id": 1, "name": "Alice", "email":"alice@gmail.com", "position":"Senior Software Dev", "department": "Engineering"},
    {"id": 2, "name": "Bob", "email":"bob@fmail.com", "position":"BA", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "email":"charlie.98@yahoo.in", "position":"Associate", "department": "HR"}
    
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
