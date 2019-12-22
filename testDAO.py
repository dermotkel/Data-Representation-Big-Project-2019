import mysql.connector
class gameDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )