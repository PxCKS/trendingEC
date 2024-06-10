from flask import Flask, render_template, url_for, request,redirect
import mysql.connector


app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ntando_01",
        database="trendingec"
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        sql="SELECT * FROM USERS"

        curso
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not username or not email or not password:
            return "All fields are required", 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_data = "INSERT INTO USERS (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_data, (username, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/password-recovery', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Handle password recovery logic here
        pass
    return render_template('forgot-password.html')

if __name__ == '__main__':
    app.run(debug=True)