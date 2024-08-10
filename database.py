import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("MYSQL_DB_PASSWORD")

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

def login_user(user_email, password):
    pass

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
