import MySQLdb
class Database():
    def conn(self):
        con = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="essypass",
            db="mydb"
         )
        return con
