import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("MYSQL_DB_PASSWORD")

def create_db():
    # Create DB
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD)
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS LIBRARY_RECORDS")
    mydb.commit()

    #Create Table
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database="LIBRARY_RECORDS")
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS books(BookID VARCHAR(50), BookName VARCHAR(20), Author VARCHAR(20) )")
    mydb.commit()

    my_cursor.close()
    mydb.close() 


# For retrieving data from database
def get_data():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    
    my_cursor.execute("SELECT * FROM books")
    data = my_cursor.fetchall()
    my_cursor.close()
    mydb.close()
    return data

# For adding a new book record to database
def add_data(bookid,bookname,author):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()

    my_cursor.execute("INSERT INTO books VALUES(%s, %s, %s)", (bookid,bookname,author))
    mydb.commit()
    
    my_cursor.close()
    mydb.close() 

# For deleting a book record permanently from database
def del_data(bookid):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    
    my_cursor.execute("DELETE FROM books WHERE BookID = %s",(bookid,))
    mydb.commit()
    my_cursor.close()
    mydb.close()  
 
# For updating any field in particular record
def update_data(field,newdata,bookid):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd=PASSWORD, database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    
    string = f"UPDATE books SET {field} = %s WHERE BookID = %s"
    my_cursor.execute(string,(newdata,bookid))
    mydb.commit()
       
    my_cursor.close()
    mydb.close()