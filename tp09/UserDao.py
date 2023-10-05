import sqlite3
from User import User

class UserDao:

    def __init__(self,db_file) -> None:
       self._con = sqlite3.connect(db_file)

    

    def findAll(self):
        cur = self._con.cursor()
        res = cur.execute("SELECT id,first_name,last_name,email,gender,ip_address FROM users_tbl")

        for row in res.fetchall():
            u = User(*row)
            yield u
        


    

    def save(self,user:User):
        cur = self._con.cursor()
        sql = """INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address) 
        VALUES(?,?,?,?,?)"""
        values = user.first_name,user.last_name,user.email,user.gender,user.ip_address
        cur.execute(sql,values)
        self._con.commit()




    def __del__(self):
        self._con.close()  
