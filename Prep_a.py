import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Creazione del database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Animali")

# Connessione al database Animali
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

# Creazione della tabella Mammiferi
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")
