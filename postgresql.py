import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

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
        return True
    else:
        print("Invalid email or password.")
        cursor.close()
        connection.close()
        return False


def add_post(title, desc, image, user_email, posted_time):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    print(posted_time)
    cursor.execute("INSERT INTO POSTS(owner_email, posted_time, post_title, post_desc, post_img) VALUES(%s, %s, %s, %s, %s)", (user_email, str(posted_time), title, desc, psycopg2.Binary(image) ))
    connection.commit()

    print("Posted successfully")
    cursor.close()
    connection.close()


def fetch_all_posts():
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = "SELECT * FROM POSTS ORDER BY POSTED_TIME DESC"
    cursor.execute(sql)
    posts = cursor.fetchall()
    return posts

def isLiked(postid, user_email):
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
    try:
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
        liked_posts = cursor.fetchall()

        for post in liked_posts:
            print(f"Post ID: {post[0]}, Title: {post[1]}, Description: {post[2]}")

        return liked_posts

    except (Exception, Error) as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

   


def fetch_my_posts(user_email):
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()
    sql = "SELECT * FROM POSTS WHERE OWNER_EMAIL=%s ORDER BY POSTED_TIME DESC"
    cursor.execute(sql, (user_email,))
    posts = cursor.fetchall()
    return posts


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


# def init_db():
#     connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS USERS (FIRST_NAME VARCHAR(100), SECOND_NAME VARCHAR(100), EMAIL_ID VARCHAR(100) PRIMARY KEY, PASSWORD VARCHAR(200) NOT NULL, DOB DATE)")
#     cursor.execute("CREATE TABLE IF NOT EXISTS POSTS (POST_ID INT PRIMARY KEY, OWNER_EMAIL VARCHAR(100), POSTED_TIME TIMESTAMP, POST_TITLE VARCHAR(100) NOT NULL, POST_DESC VARCHAR(200) NOT NULL, LIKE_COUNT INT DEFAULT 0, POST_IMG BYTEA)")
#     cursor.execute("CREATE TABLE IF NOT EXISTS REACTIONS (POST_ID INT, OWNER_EMAIL VARCHAR(100))")
#     cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (POST_ID) REFERENCES POSTS (POST_ID)")
#     cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")
#     cursor.execute("ALTER TABLE POSTS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")
#     connection.commit()
#     cursor.close()
#     connection.close()

# if __name__ == "__main__":
#     init_db()