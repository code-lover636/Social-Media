import mysql.connector
from mysql.connector import Error

def insert_reaction(post_id, owner_email):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',         # Replace with your host, e.g., 'localhost'
            user='root',              # Replace with your MySQL username
            password='your_password', # Replace with your MySQL password
            database='your_database'  # Replace with your database name
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # SQL query to insert a reaction
            sql = "INSERT INTO REACTIONS (POST_ID, OWNER_EMAIL) VALUES (%s, %s)"
            values = (post_id, owner_email)

            cursor.execute(sql, values)
            conn.commit()

            print(f"Reaction added for Post ID: {post_id} by {owner_email}")

    except Error as err:
        print(f"Error: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()