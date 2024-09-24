# import psycopg2
# import os
# from dotenv import load_dotenv
# from psycopg2 import Error
# import base64

# load_dotenv()

# POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
# POSTGRESQL_DB = os.getenv("POSTGRESQL_DB")
# POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
# POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")

# def init_db():
#     connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
#     cursor = connection.cursor()
#     # cursor.execute("CREATE TABLE IF NOT EXISTS USERS (FIRST_NAME VARCHAR(100), SECOND_NAME VARCHAR(100), EMAIL_ID VARCHAR(100) PRIMARY KEY, PASSWORD VARCHAR(200) NOT NULL, DOB DATE)")
#     # cursor.execute("CREATE TABLE IF NOT EXISTS POSTS (POST_ID INT PRIMARY KEY, OWNER_EMAIL VARCHAR(100), POSTED_TIME TIMESTAMP, POST_TITLE VARCHAR(100) NOT NULL, POST_DESC VARCHAR(200) NOT NULL, LIKE_COUNT INT DEFAULT 0, POST_IMG BYTEA)")
#     # cursor.execute("CREATE TABLE IF NOT EXISTS REACTIONS (POST_ID INT, OWNER_EMAIL VARCHAR(100))")
#     # cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (POST_ID) REFERENCES POSTS (POST_ID)")
#     # cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")
#     # cursor.execute("ALTER TABLE POSTS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")
#     cursor.execute("ALTER TABLE USERS ADD COLUMN PROFILE_PICTURE BYTEA DEFAULT %s",(psycopg2.Binary("https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-in-the-style-of-2d-game-art-image_2884743.jpg"),) )
#     connection.commit()
#     cursor.close()
#     connection.close()

# if __name__ == "__main__":
#     init_db()

import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error
import requests
from io import BytesIO

load_dotenv()

POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_DB = os.getenv("POSTGRESQL_DB")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")

# Function to download and return the image as binary data with headers
def download_image_as_binary(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return BytesIO(response.content).getvalue()  # Convert image content to binary
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")

def init_db():
    try:
        # Establishing the database connection
        connection = psycopg2.connect(
            host=POSTGRESQL_HOST,
            user=POSTGRESQL_USER,
            password=POSTGRESQL_PASSWORD,
            database=POSTGRESQL_DB
        )
        cursor = connection.cursor()

        # Download the image and convert to binary
        image_url = "https://assets.devfolio.co/users/97b24747235b430ba40a12b2632da62a/avatar-92e14b35-94dc-4822-be09-55eae6dff786.jpeg"
        image_binary = download_image_as_binary(image_url)

        # Alter table to add PROFILE_PICTURE column with default binary image
        # cursor.execute("""
        #     ALTER TABLE USERS 
        #     ADD COLUMN IF NOT EXISTS PROFILE_PICTURE BYTEA DEFAULT %s
        # """, (psycopg2.Binary(image_binary),))

        cursor.execute("UPDATE USERS SET PROFILE_PICTURE=%s where email_id='aravindashokan@proton.me'", (psycopg2.Binary(image_binary),))

        # Commit the transaction
        connection.commit()
        print("Column added successfully with default image data.")

    except (Exception, Error) as error:
        print("Error while interacting with PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    init_db()

