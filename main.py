import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute(mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"))