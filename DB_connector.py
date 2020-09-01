import sqlite3

class  db_connect:

    def __init__(self):
        self.db_connect = sqlite3.connect("Timer.db")
        self.db_connect.cursor()

        self.db_connect.row_factory = sqlite3.Row
        self.db_connect.execute("create table if not exists Timer(ID integer primary key autoincrement, Time_IN text,Time_Out text, Total text) ")
        self.db_connect.commit()


    def View(self):
        self.db_connect.cursor()
        cursor = self.db_connect.execute("select * from Timer")
        self.db_connect.commit()
        return cursor

    def View_1(self,name):
        self.db_connect.cursor()
        cursor = self.db_connect.execute("select Time_Out from Timer where ID = ?",(name,))
        self.db_connect.commit()
        return cursor

    def insert_in(self,value):
        self.db_connect.execute("insert into Timer(Time_IN) values(?)",(value,))    # how you writing this !! ***
        self.ID = self.db_connect.execute("select ID from Timer where Time_IN = ? ",(value,)).fetchall()
        self.db_connect.commit()
        return self.ID

    def insert_Out(self,value, Total,ID):
        self.db_connect.execute("Update  Timer SET Time_Out = ? ,Total= ?  where ID = ?",[value,Total,ID])
        self.db_connect.commit()
        return "Time OUT is submitted "

