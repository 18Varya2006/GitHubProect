import sqlite3
from tkinter import ttk
from tkinter import*
import tkinter
from data import del_data, add_data, edit_data, del_data1, edit_data1, add_data1
import os
import datetime
from tkinter import messagebox

def on_clo():
    now=datetime.datetime.now()
    name=now.strftime("%d.%m.%Y_%H.%S")
    log_file.write(f"{name}Выключение ИС")
    log_file.close()
    connection.close()
    tk.destroy()

dirname=os.path.dirname(__file__)
os.chdir(dirname)





def on_login():
    entry_user = user_combobox.get()
    entry_password = password_entry.get()
    
    connection = sqlite3.connect('KADR1.db')
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM tab_3 WHERE username=? AND password=?", (entry_user, entry_password))
    base_user = cursor.fetchone()
    connection.commit()
    connection.close()
    # print(base_user)
    
    if base_user:
        tk.destroy()
        import data
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")



tk = Tk()
tk.title("Авторизация")
tk.geometry("400x200")
tk.resizable(False, False)


    


connection = sqlite3.connect('KADR1.db')
cursor = connection.cursor()
cursor.execute("SELECT username FROM tab_3")
users =  cursor.fetchall()
connection.commit()
connection.close()
    

Label(tk, text="Пользователь:").place(x=50, y=40)

user_combobox = ttk.Combobox(tk, values=users, width=25)
user_combobox.place(x=50, y=65)

if users:
    user_combobox.current(0)
    
Label(tk, text="Пароль:").place(x=50, y=100)
password_entry = Entry(tk, show="*", width=28)
password_entry.place(x=50, y=125)
    
# Кнопки
login_btn = Button(tk, text="Войти", width=10, command=on_login)
login_btn.place(x=100, y=160)
    
cancel_btn = Button(tk, text="Отмена", width=10, command=tk.destroy)
cancel_btn.place(x=200, y=160)
    
password_entry.focus_set()
    

tk.mainloop()


tk=Tk()
tk.geometry("250x100")
tk.title("Кадровое агенство")

if not os.path.exists("log"):
    os.mkdir("log")
def adm():
    uy=Tk()
    uy.title("Администрирование")
    uy.geometry("250x300")
    
    tre=ttk.Treeview(uy, columns=('users', 'pass'), show="headings")

    tre.heading("users", text="Пользователи", anchor="center")
    tre.heading("pass", text="Пароль", anchor="center")
    Bu=Button(uy, text="Удалить")
    Bu.place(x=200, y=300)
    
    tre.column('users', width=100)
    tre.column("pass", width=100)
    def del_data1(tree, log_file, connection, cursor):
        data = tree.item(tree.selection())
        data_ID=data["values"][0]
        cursor.execute(f"DELETE FROM tab_3 WHERE famil={data_ID}")
        connection.commit()

        for item in tree.get_children():
            tree.delete(item)
        cursor.execute("SELECT * FROM tab_3")
        pipls = cursor.fetchall()
        connection.commit()    
        for d in pipls:
            tree.insert('', END, values=d)
        
        now=datetime.datetime.now()
        name = now.strftime("%d.%m.%Y_%H.%M.%S")
        log_file.write(f"{name} Запись {data_ID} удалена администратором\n")
        print(data_ID)
        
    
    tre.place(x=10, y=10)

now=datetime.datetime.now()
name = now.strftime("%d.%m.%Y_%H.%M.%S")

log_file=open(rf"log\log_{name}.txt", 'w')

menubar = Menu(tk)
tk.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Администратирование", command=adm)


file_menu.add_command(label="Настройки")

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="О программе")






colums_tuple = ("ID", "zagolovok","opisanie", "zp", "kompania")
def vak():
    tu=Tk()
    tu.title("Вакансии")
    tu.geometry("500x400")
    tre = ttk.Treeview(tu, columns=colums_tuple, show="headings")
    tre.heading("ID", text="ID", anchor="center")
    tre.heading("zagolovok",text="Заголовок",anchor="center")
    tre.heading("opisanie", text="Описание", anchor="center")
    tre.heading("zp",text="ЗП", anchor="center")
    tre.heading("kompania", text="Компания", anchor="center")

    tre.column("ID",width=100, anchor="w")
    tre.column("zagolovok",width=100, anchor="w")
    tre.column("opisanie", width=80, anchor="w")
    tre.column("zp", width=100, anchor="w")  
    tre.column("kompania", width=100, anchor="w")


    L_name=Label(tu,text="заголовок")
    L_age=Label(tu,text="описание")
    L_city=Label(tu,text="ЗП")
    L_kom=Label(tu,text="Компания")

    L_name.place(x=50,y=250)
    L_age.place(x=50,y=280)
    L_city.place(x=50,y=310)
    L_kom.place(x=50,y=340)


    connection = sqlite3.connect('KADR1.db')
    cursor = connection.cursor()

    cursor.execute(" SELECT * FROM tab_1")

    pipls=cursor.fetchall()
    for data in pipls:
        tre.insert("", END, values=data)
    # pipls=(("Программист", "Python", 100000, "Google"),("Программист", "Java", 120000, "Microsoft"),("Программист", "C++", 110000, "Facebook"),("Программист", "C#", 130000, "Google"),("Раработчик", "C++", 110000, "Facebook"),("Программист", "C#", 130000, "Google"),
    # ("Разработчик", "Python", 110000, "google"),("разработчик", "C#", 130000, "Google"))

    connection.commit()

    L_id=Label(tk, text="IID:")
    L_id.place(x=100, y=215)

    E_name=Entry(tu)
    E_age=Entry(tu)
    E_city=Entry(tu)
    E_kom=Entry(tu)

    E_name.place(x=120,y=250)
    E_age.place(x=120,y=280)
    E_city.place(x=120,y=310)
    E_kom.place(x=120,y=340)

    B1=Button(tu,text="Ввод",command=lambda: add_data(tre,  E_name, E_age, E_city, log_file,E_kom, connection, cursor))
    B2=Button(tu,text="Удалить", command=lambda: del_data1(tre, log_file, connection, cursor))
    B3=Button(tu, text="Изменить", command=lambda: edit_data(tre, log_file, E_name, E_age, E_city,E_kom, L_id, B2, B3, B1, connection, cursor))

    B1.place(x=400,y=350)
    B2.place(x=400,y=300)
    B3.place(x=400,y=250)

    


    tre.pack(padx=10, pady=10)
    tu.mainloop()



columns_tuple = ("ID", "FIO","Opit", "Naviki", "Ozidaemai","Dolznosti")
def rez():
    tr=Tk()
    tr.title("Резюме")
    tr.geometry("600x500")
    tree = ttk.Treeview(tr, columns=columns_tuple, show="headings")
    tree.heading("ID",text="ID",anchor="center")
    tree.heading("FIO",text="ФИО",anchor="center")
    tree.heading("Opit", text="Опыт", anchor="center")
    tree.heading("Naviki",text="Навыки", anchor="center")
    tree.heading("Ozidaemai", text="Ожидаемая ЗП", anchor="center")
    tree.heading("Dolznosti", text="Должность", anchor="center")

    tree.column("ID",width=100, anchor="w")
    tree.column("FIO",width=100, anchor="w")
    tree.column("Opit", width=80, anchor="w")
    tree.column("Naviki", width=100, anchor="w")  
    tree.column("Ozidaemai", width=100, anchor="w")
    tree.column("Dolznosti", width=100, anchor="w")

    L_name=Label(tr,text="Имя")
    L_age=Label(tr,text="Возраст")
    L_city=Label(tr,text="Город")
    L_kom=Label(tr,text="Компания")
    L_dolz=Label(tr,text="Должность")

   

    L_name.place(x=50,y=250)
    L_age.place(x=50,y=280)
    L_city.place(x=50,y=310)
    L_kom.place(x=50,y=340)
    L_dolz.place(x=50,y=370)

    L_id=Label(tk, text="IID:")
    L_id.place(x=100, y=215)


    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID,FIO TEXT,Opit TEXT,Naviki TEXT,Ozidaemai INTEGER,Dolznosti TEXT)")
    cursor.execute(" SELECT * FROM tab_2") 
    pipls=cursor.fetchall()
    for data in pipls:
        tree.insert("", END, values=data)
    pipls=("Ваня","Python","C++",2,"Программист"),("Виктор","Java","C++",3,"Программист"),("Андрей","C#","C++",1,"Разработчик"),("Саша","C++","C++",2,"Программист"),("Света","C#","C++",1,"Разработчик"),("Настя","C++","C++",2,"Программист")

    connection.commit()

  
    E_name=Entry(tr)
    E_age=Entry(tr)
    E_city=Entry(tr)
    E_kom=Entry(tr)
    E_dolz=Entry(tr)

    E_name.place(x=120,y=250)
    E_age.place(x=120,y=280)
    E_city.place(x=120,y=310)
    E_kom.place(x=120,y=340)
    E_dolz.place(x=120,y=370)

    B1=Button(tr,text="Ввод",command=lambda: add_data1(tree,  E_name, E_age, E_city, E_kom, E_dolz, log_file, connection, cursor))
    B2=Button(tr,text="Удалить", command=lambda: del_data(tree, log_file, connection, cursor))
    B3=Button(tr, text="Изменить", command=lambda: edit_data1 (tree, log_file, E_name, E_age, E_city,E_kom,E_dolz, L_id, B1, B2, B3, connection, cursor))

    B1.place(x=400,y=350)
    B2.place(x=300,y=350)
    B3.place(x=500, y=350)
    


    tree.pack(padx=10, pady=10)
    tr.mainloop()


    tree.pack(padx=10, pady=10)
    


connection = sqlite3.connect('KADR1.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tab_1 (ID INTEGER,zagolovok TEXT,opisanie TEXT,zp INTEGER,kompania TEXT)")
cursor.execute(" SELECT * FROM tab_1") 
pipls=cursor.fetchall()
print(pipls)

B1=Button(tk,text="Вакансии",command=vak)
B2=Button(tk,text="Резюме",command=rez)

B1.place(x=50,y=40)
B2.place(x=150,y=40)

tk.mainloop()
             
