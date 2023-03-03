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

# Richiesta all'utente del numero di animali da inserire
n = int(input("Quanti animali vuoi inserire? "))

# Ciclo per l'inserimento dei n animali
for i in range(n):
    print("Inserimento animale n°", i+1)
    nome = input("Inserisci il nome proprio dell'animale: ")
    razza = input("Inserisci la razza dell'animale: ")
    peso = int(input("Inserisci il peso dell'animale: "))
    eta = int(input("Inserisci l'età dell'animale: "))

    # Query per inserire l'animale nella tabella Mammiferi
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (nome, razza, peso, eta)
    mycursor.execute(sql, val)

    # Richiesta all'utente se vuole continuare ad inserire animali
    if i < n-1:
        risposta = input("Animale inserito. Vuoi inserire un altro animale? (sì/no) ")
        if risposta.lower() == "no":
            break

# Salvataggio dei cambiamenti nel database
mydb.commit()

# Selezione di tutti gli animali nella tabella Mammiferi che pesano più di 2 kg
sql = "SELECT * FROM Mammiferi WHERE Peso > 2"
mycursor.execute(sql)

# Stampa dei risultati
myresult = mycursor.fetchall()
for x in myresult:
  print(x)