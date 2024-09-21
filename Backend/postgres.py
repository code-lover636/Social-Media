import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error
import base64

load_dotenv()

POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_DB = os.getenv("POSTGRESQL_DB")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")


def register_user(first_name, second_name, email_id, password, dob):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM USERS WHERE EMAIL_ID = %s", (email_id,))
    if cursor.fetchone():
        print("User already exists!")
        cursor.close()
        connection.close()
        return False

    sql = "INSERT INTO USERS (FIRST_NAME, SECOND_NAME, EMAIL_ID, PASSWORD, DOB) VALUES (%s, %s, %s, MD5(%s), %s)"
    cursor.execute(sql, (first_name, second_name, email_id, password, dob))
    connection.commit()

    print("User registered successfully!")
    cursor.close()
    connection.close()
    return True


def login_user(email_id, password):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = "SELECT * FROM USERS WHERE EMAIL_ID = %s AND PASSWORD = MD5(%s)"
    cursor.execute(sql, (email_id, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        cursor.close()
        connection.close()
        return user[0], user[1]
    else:
        print("Invalid email or password.")
        cursor.close()
        connection.close()
        return False


def add_post(title, desc, image, user_email, posted_time):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO POSTS(owner_email, posted_time, post_title, post_desc, post_img) VALUES(%s, %s, %s, %s, %s)", (user_email, str(posted_time), title, desc, psycopg2.Binary(image) ))
    connection.commit()

    print("Posted successfully")
    cursor.close()
    connection.close()


def fetch_all_posts(user_email):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = "SELECT * FROM POSTS LEFT OUTER JOIN REACTIONS ON POSTS.POST_ID = REACTIONS.POST_ID AND REACTIONS.OWNER_EMAIL = %s ORDER BY POSTS.POSTED_TIME DESC "
    cursor.execute(sql,  (user_email,))
    posts = cursor.fetchall()

    # Convert binary images to base64 strings if necessary
    formatted_posts = []
    for post in posts:
        post_id, owner_email, posted_time, post_title, post_desc, like_count, post_img, rpostid, rownerid = post
        if rpostid:
            liked = 1
        else:
            liked = 0
        post_img_base64 = base64.b64encode(post_img).decode('utf-8') if post_img else None
        formatted_posts.append((post_id, posted_time, post_title, post_desc, owner_email, like_count, post_img_base64, liked))
    
    return formatted_posts

def isLiked(user_email, postid):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = """
        SELECT POSTS.LIKE_COUNT
        FROM POSTS
        JOIN REACTIONS ON POSTS.POST_ID = REACTIONS.POST_ID
        WHERE REACTIONS.OWNER_EMAIL = %s AND POSTS.POST_ID = %s
        """
    cursor.execute(sql, (user_email, postid))
    posts = cursor.fetchone()
    if not posts:
        return False
    else:
        return True


def fetch_liked_posts(user_email):
    conn = psycopg2.connect(
        host=POSTGRESQL_HOST,
        user=POSTGRESQL_USER,
        password=POSTGRESQL_PASSWORD,
        database=POSTGRESQL_DB
    )
    cursor = conn.cursor()

    sql = """
    SELECT POSTS.POST_ID, POSTS.OWNER_EMAIL, POSTS.POSTED_TIME, POSTS.POST_TITLE, POSTS.POST_DESC, POSTS.LIKE_COUNT, POSTS.POST_IMG
    FROM POSTS
    JOIN REACTIONS ON POSTS.POST_ID = REACTIONS.POST_ID
    WHERE REACTIONS.OWNER_EMAIL = %s
    """
    cursor.execute(sql, (user_email,))
    posts = cursor.fetchall()

    # Convert binary images to base64 strings if necessary
    formatted_posts = []
    for post in posts:
        post_id, owner_email, posted_time, post_title, post_desc, like_count, post_img = post
        post_img_base64 = base64.b64encode(post_img).decode('utf-8') if post_img else None
        formatted_posts.append((post_id, posted_time, post_title, post_desc, owner_email, like_count, post_img_base64, 1))

    return formatted_posts

    if cursor:
        cursor.close()
    if conn:
        conn.close()   


def fetch_my_posts(user_email):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = "SELECT POSTS.*, CASE WHEN REACTIONS.POST_ID IS NOT NULL THEN 1 ELSE 0 END AS IS_LIKED FROM POSTS LEFT OUTER JOIN REACTIONS ON POSTS.POST_ID = REACTIONS.POST_ID AND REACTIONS.OWNER_EMAIL = %s WHERE POSTS.OWNER_EMAIL = %s ORDER BY POSTS.POSTED_TIME DESC"
    cursor.execute(sql, (user_email, user_email,))
    posts = cursor.fetchall()

    # Convert binary images to base64 strings if necessary
    formatted_posts = []
    for post in posts:
        post_id, owner_email, posted_time, post_title, post_desc, like_count, post_img, liked = post
        post_img_base64 = base64.b64encode(post_img).decode('utf-8') if post_img else None
        formatted_posts.append((post_id, posted_time, post_title, post_desc, owner_email, like_count, post_img_base64, liked))
    
    return formatted_posts


def like_a_post(postid, user_email):
    try:
        conn = psycopg2.connect(
            host=POSTGRESQL_HOST,
            user=POSTGRESQL_USER,
            password=POSTGRESQL_PASSWORD,
            database=POSTGRESQL_DB
        )
        cursor = conn.cursor()

        sql = "INSERT INTO REACTIONS (POST_ID, OWNER_EMAIL) VALUES (%s, %s)"
        values = (postid, user_email)

        cursor.execute(sql, values)
        cursor.execute("UPDATE POSTS SET LIKE_COUNT = LIKE_COUNT + 1 WHERE POST_ID = %s", (postid,))
        conn.commit()

        print(f"Post ID: {postid} liked by {user_email}")

    except (Exception, Error) as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()




def remove_like(postid, user_email):
    try:
        conn = psycopg2.connect(
            host=POSTGRESQL_HOST,
            user=POSTGRESQL_USER,
            password=POSTGRESQL_PASSWORD,
            database=POSTGRESQL_DB
        )
        cursor = conn.cursor()
        sql = "DELETE FROM REACTIONS WHERE POST_ID = %s AND OWNER_EMAIL = %s"
        values = (postid, user_email)

        cursor.execute(sql, values)
        cursor.execute("UPDATE POSTS SET LIKE_COUNT = LIKE_COUNT - 1 WHERE POST_ID = %s", (postid,))

        conn.commit()

        print("Reaction deleted successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()