import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Animali (id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255) , Peso INT(255) , Età INT(255))"  VALUES (%s, %s , %s , %s , %s)"


mycursor.executemany(sql, val)

mydb.commit()

