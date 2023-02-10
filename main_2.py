#ti serve per creare una tabella visualizzarla e aggiunger una chiave primaria a una tabella gia esistente 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers REMOVE COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
