from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Sample employee data (could be from a database in real apps)
employees = [
    {"id": 1, "name": "Alice", "email":"alice@gmail.com", "position":"Senior Software Dev", "department": "Engineering"},
    {"id": 2, "name": "Bob", "email":"bob@fmail.com", "position":"BA", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "email":"charlie.98@yahoo.in", "position":"Associate", "department": "HR"}
    
]

conn = mysql.connector.connect(
    host = '127.0.0.1:3306',
    user = 'root',
    password = 'root',
    database = 'employee'
)

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/getData', methods=['GET'])
def get_tables():
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    table_names = [table[0] for table in tables]
    return jsonify({"tables":table_names}), 200
    

if __name__ == '__main__':
    app.run(debug=True)
