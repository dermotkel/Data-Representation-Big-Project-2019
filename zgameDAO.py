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
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into game (title, developer, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from game"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from game where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update game set title=%s, developer=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from game where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Title','Developer', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
gameDAO = gameDAO()