import mysql.connector

# Connessione al database Animali
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

# Creazione del cursore per eseguire le query
mycursor = mydb.cursor()

# Selezione di tutti gli animali nella tabella Mammiferi
mycursor.execute("SELECT * FROM Mammiferi")

# Stampa dei risultati
myresult = mycursor.fetchall()
for x in myresult:
  print(x)