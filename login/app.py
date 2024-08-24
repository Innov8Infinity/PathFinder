from flask import Flask, request, jsonify, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Configure the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="meow",
    database="user_registration"
)

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data['name']
    email = data['email']
    password = data['password']
    hashed_password = generate_password_hash(password)

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (name, email, hashed_password))
    db.commit()
    cursor.close()

    return redirect("http://127.0.0.1:5000/")

if __name__ == '__main__':
    app.run(debug=True)
