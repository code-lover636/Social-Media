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

def create_tables(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (FIRST_NAME VARCHAR(100), SECOND_NAME VARCHAR(100), EMAIL_ID VARCHAR(100) PRIMARY KEY, PASSWORD VARCHAR(200) NOT NULL, DOB DATE, PROFILE_PICTURE BYTEA)")
    cursor.execute("CREATE TABLE IF NOT EXISTS POSTS (POST_ID SERIAL PRIMARY KEY, OWNER_EMAIL VARCHAR(100), POSTED_TIME TIMESTAMP, POST_TITLE VARCHAR(100) NOT NULL, POST_DESC VARCHAR(2000) NOT NULL, LIKE_COUNT INT DEFAULT 0, POST_IMG BYTEA)")
    cursor.execute("CREATE TABLE IF NOT EXISTS REACTIONS (POST_ID INT, OWNER_EMAIL VARCHAR(100))")
    cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (POST_ID) REFERENCES POSTS (POST_ID)")
    cursor.execute("ALTER TABLE REACTIONS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")
    cursor.execute("ALTER TABLE POSTS ADD FOREIGN KEY (OWNER_EMAIL) REFERENCES USERS (EMAIL_ID)")

def init_db():
    connection = psycopg2.connect(host=POSTGRESQL_HOST, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD, database=POSTGRESQL_DB)
    cursor = connection.cursor()

    # Creation
    create_tables(cursor)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    init_db()