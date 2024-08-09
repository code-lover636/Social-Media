import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("MYSQL_DB_PASSWORD")

def register_user(user_name, user_email, password):
    pass

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