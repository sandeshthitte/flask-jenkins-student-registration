from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'studentuser',
    'password': 'password123',
    'database': 'studentdb'
}

# Home page: Registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']
        contact = request.form['contact']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = '''
        INSERT INTO students (name, email, phone, course, address, contact)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (name, email, phone, course, address, contact)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

        return '✅ Student Registered Successfully!'
    return render_template('register.html')


# Page to list all registered students
@app.route('/students')
def list_students():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, phone, course, address, contact FROM students")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("students.html", students=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
