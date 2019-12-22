import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="datarepresentation"
)

cursor = db.cursor()
sql="insert into game (title, developer, price) values (%s,%s,%s)"
values = ("Dayz Gone","SIE Bend Studio",40)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
