import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("MYSQL_DB_PASSWORD")

def create_connection():
    return mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database="YOUR_DATABASE_NAME")

def register_user(first_name, second_name, email_id, password, dob):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM USERS WHERE EMAIL_ID = %s", (email_id,))
    if cursor.fetchone():
        print("User already exists!")
        cursor.close()
        connection.close()
        return False

    sql = "INSERT INTO USERS (FIRST_NAME, SECOND_NAME, EMAIL_ID, PASSWORD, DOB) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (first_name, second_name, email_id, password, dob))
    connection.commit()

    print("User registered successfully!")
    cursor.close()
    connection.close()
    return True

def login_user(email_id, password):
    connection = create_connection()
    cursor = connection.cursor()

    sql = "SELECT * FROM USERS WHERE EMAIL_ID = %s AND PASSWORD = %s"
    cursor.execute(sql, (email_id, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        cursor.close()
        connection.close()
        return True
    else:
        print("Invalid email or password.")
        cursor.close()
        connection.close()
        return False

def add_post(title, desc, image):
    print(title, desc, image, sep="\n")

def fetch_all_posts():
    pass

def fetch_liked_posts(user_email):
    pass

def fetch_my_posts(user_email):
    pass

def like_a_post(postid, user_email):
    pass

def remove_like(postid, user_email):
    pass
