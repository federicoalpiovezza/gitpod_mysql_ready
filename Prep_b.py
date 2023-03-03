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

# Inserimento di 5 animali nella tabella Mammiferi
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
val = [
  ("Fido", "Golden Retriever", 25, 5),
  ("Gatto", "Persiano", 5, 3),
  ("Bianca", "Pastore Tedesco", 30, 7),
  ("Leo", "British Shorthair", 6, 2),
  ("Tigre", "Bengala", 150, 10)
]
mycursor.executemany(sql, val)

# Commit delle modifiche al database
mydb.commit()

# Verifica dei dati inseriti
mycursor.execute("SELECT * FROM Mammiferi")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)