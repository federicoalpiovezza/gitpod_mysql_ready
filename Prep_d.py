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

# Ciclo per chiedere all'utente di inserire un nuovo animale per 5 volte
for i in range(5):
  # Input dei dati dall'utente
  nome = input("Inserisci il nome del nuovo animale: ")
  razza = input("Inserisci la razza del nuovo animale: ")
  peso = input("Inserisci il peso del nuovo animale: ")
  eta = input("Inserisci l'età del nuovo animale: ")

  # Verifica che peso ed eta siano interi
  try:
    peso = int(peso)
    eta = int(eta)
  except ValueError:
    print("Errore: il peso e l'età devono essere numeri interi.")
    continue

  # Inserimento del nuovo animale nella tabella Mammiferi
  sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
  val = (nome, razza, peso, eta)
  mycursor.execute(sql, val)

  # Commit delle modifiche al database
  mydb.commit()

# Selezione di tutti gli animali nella tabella Mammiferi e stampa dei risultati
mycursor.execute("SELECT * FROM Mammiferi")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)