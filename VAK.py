import sqlite3
import os
dirname = os.path.dirname(__file__)
os.chdir(dirname)

connection = sqlite3.connect('KADR1.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tab_1 (ID INTEGER PRIMARY KEY AUTOINCREMENT, zagolovok TEXT,opisanie TEXT,zp INTEGER,kompania TEXT)")
pipls1=(("Программист", "Python", 100000, "Google"),("Программист", "Java", 120000, "Microsoft"),("Программист", "C++", 110000, "Facebook"),("Программист", "C#", 130000, "Google"),("Раработчик", "C++", 110000, "Facebook"),("Программист", "C#", 130000, "Google"),
("Разработчик", "Python", 110000, "google"),("разработчик", "C#", 130000, "Google"))

cursor.executemany("INSERT INTO tab_1 (zagolovok,opisanie,zp,kompania) VALUES (?,?,?,?)", pipls1)
connection.commit()





cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT,FIO TEXT,Opit TEXT,Naviki TEXT,Ozidaemai INTEGER,Dolznosti TEXT)")

pipls2=("Ваня","Python","C++",20000,"Программист"),("Виктор","Java","C++",30000,"Программист"),("Андрей","C#","C++",10000,"Разработчик"),("Саша","C++","C++",20000,"Программист"),("Света","C#","C++",1,"Разработчик"),("Настя","C++","C++",200000,"Программист")

cursor.executemany("INSERT INTO tab_2 (FIO,Opit,Naviki,Ozidaemai,Dolznosti) VALUES (?,?,?,?,?)", pipls2)


connection.commit()




cursor.execute("CREATE TABLE IF NOT EXISTS tab_3(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
users=(("Администратор","123" ),("Пользователь ",  "111"))
cursor.executemany("INSERT INTO tab_3 (username, password) VALUES (?, ?)", users)

connection.commit()
connection.close()