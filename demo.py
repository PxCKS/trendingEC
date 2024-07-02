from flask import Flask, flash, render_template, url_for, request, redirect
import mysql.connector
#from routes.admin import admin_bp

#making the instance of the Flask application
app = Flask(__name__)
#app.register_blueprint(admin_bp, url_prefix='/admin')

#function to make connection to the database
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ntando_01",
        database="trendingec"
    )
    return conn


#Function used to define home page logic
@app.route('/')
def home():
    return render_template('index.html')


#function used to handle login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #checking the http method
    if request.method == 'POST':

        #getting input values from the html pages
        username = request.form.get('username')
        password = request.form.get('password')

        #checking for empty input fields

        #making a connection to the database and creating a cursor object
        conn = get_db_connection()
        cursor = conn.cursor()

        #sql query for checking the table in the database
        sql = "SELECT * FROM USERS WHERE username = %s AND password = %s"
        param = (username, password)
        cursor.execute(sql, param)

        user = cursor.fetchone()
        #closing connection and cursor

        print(f"User fetched: {user}")
        cursor.close()
        conn.close()

        #checking if the specified credential exist in the database
        if user:
            app.logger.info(f"Successful login attempt for user: {username}")

            return redirect(url_for('home'))

        else:
            app.logger.warning(f"Failed login attempt for user: {username}")
            return "Invalid Credentials.", 401

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
        email = request.form.get('email')

        conn = get_db_connection()
        cursor = conn.cursor()

        if not email:
            return "Email is required", 400
        else:
            return redirect(url_for('login'))
    return render_template('forgot-password.html')


if __name__ == '__main__':
    app.run(debug=True)
