import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE game (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), developer VARCHAR(255), price INT)"

cursor.execute(sql)