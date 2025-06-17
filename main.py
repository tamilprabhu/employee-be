from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# conn = mysql.connector.connect(
#     host = 'localhost',
#     port = '8080',
#     user = 'root',
#     password = 'root',
#     database = 'employee'
# )

# Sample employee data (could be from a database in real apps)
employees = [
    {"id": 1, "name": "Alice", "email":"alice@gmail.com", "position":"Senior Software Dev", "department": "Engineering"},
    {"id": 2, "name": "Bob", "email":"bob@fmail.com", "position":"BA", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "email":"charlie.98@yahoo.in", "position":"Associate", "department": "HR"}
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/getData', methods=['GET'])
def get_tables():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='employee'
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        cursor.close()
        conn.close()
        table_names = [table[0] for table in tables]
        return jsonify({"tables": table_names}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert/cert.pem', 'cert/key.pem'))
