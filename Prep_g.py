import mysql.connector

# Funzione per connettersi al database
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="animals"
    )
    return mydb

# Funzione per inserire un nuovo animale nel database
def add_animal():
    name = input("Inserisci il nome dell'animale: ")
    species = input("Inserisci la specie dell'animale: ")
    age = int(input("Inserisci l'età dell'animale: "))
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO animals (name, species, age) VALUES (%s, %s, %s)"
    val = (name, species, age)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "animale/i inseriti con successo.")

# Funzione per visualizzare tutti gli animali presenti nel database
def show_animals():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM animals")
    animals = cursor.fetchall()
    for animal in animals:
        print(animal)

# Funzione per eliminare un animale dal database
def delete_animal():
    animal_id = int(input("Inserisci l'ID dell'animale da eliminare: "))
    db = connect_to_database()
    cursor = db.cursor()
    sql = "DELETE FROM animals WHERE id = %s"
    val = (animal_id,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "animale/i eliminati con successo.")

# Funzione per modificare un animale nel database
def update_animal():
    animal_id = int(input("Inserisci l'ID dell'animale da modificare: "))
    name = input("Inserisci il nuovo nome dell'animale: ")
    species = input("Inserisci la nuova specie dell'animale: ")
    age = int(input("Inserisci la nuova età dell'animale: "))
    db = connect_to_database()
    cursor = db.cursor()
    sql = "UPDATE animals SET name = %s, species = %s, age = %s WHERE id = %s"
    val = (name, species, age, animal_id)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "animale/i modificati con successo.")

# Menù utente
while True:
    print("Premi 1 per inserire un nuovo animale")
    print("Premi 2 per visualizzare tutti gli animali")
    print("Premi 3 per eliminare un animale")
    print("Premi 4 per modificare un animale")
    print("Premi 5 per uscire dal programma")
    choice = int(input("Scelta: "))
    if choice == 1:
        add_animal()
    elif choice == 2:
        show_animals()
    elif choice == 3:
        delete_animal()
    elif choice == 4:
        update_animal()
    elif choice == 5:
        break
    else:
        print("Scelta non valida. Riprova.")

