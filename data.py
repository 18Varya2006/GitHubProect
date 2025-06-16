from tkinter import END, DISABLED, NORMAL
import datetime

def save_data(tree, log_file, E_name, E_age, E_city, E_kom, L_id, B1, B2, B3, connection, cursor):
    
    name = E_name.get()
    age  = E_age.get()
    city = E_city.get()
    kom = E_kom.get()
    
    cursor.execute("UPDATE tab_1 SET zagolovok=?, opisanie=?, zp=?, kompania=? WHERE ID=?", (name, age, city, kom, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)
    E_kom.delete(0, END)
 
    B2.config(state=NORMAL)
    B3.config(state=NORMAL)
    B1.config(text="Ввод", command=lambda:  add_data(tree, E_name, E_age, E_city, E_kom, log_file, connection, cursor))
    L_id.config(text="IID:")

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} изменена\n")


def save_data1(tree, log_file, E_name, E_age, E_city,E_kom,E_dolz, L_id, B_del, B_edit, B_Enter, connection, cursor):
    

    name = E_name.get()
    age  = E_age.get()
    city = E_city.get()
    kom = E_kom.get()
    dolz = E_dolz.get()

    
    cursor.execute("UPDATE tab_2 SET FIO=?, Opit=?, Naviki=?, Ozidaemai=?, Dolznosti=? WHERE ID=?", (name, age, city, kom, dolz, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_2")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)
    E_kom.delete(0, END)
    E_dolz.delete(0, END)
 
    B_del.config(state=NORMAL)
    B_edit.config(state=NORMAL)
    B_Enter.config(text="Ввод", command=lambda:  add_data(tree, E_name, E_age, E_city, E_kom, E_dolz, log_file, connection, cursor))
    L_id.config(text="IID:")

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} изменена\n")



def del_data(tree, log_file, connection, cursor):
    data = tree.item(tree.selection())
    data_ID=data["values"][0]
    cursor.execute(f"DELETE FROM tab_2 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_2")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {data_ID} удалена\n")


def del_data1(tree, log_file, connection, cursor):
    data = tree.item(tree.selection())
    data_ID=data["values"][0]
    cursor.execute(f"DELETE FROM tab_1 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {data_ID} удалена\n")
    
    

    

def edit_data(tree, log_file, E_name, E_age, E_city,E_kom, L_id, B2, B3, B1, connection, cursor):
    global id
    iid = tree.selection()
    
    
    id = tree.item(iid)["values"][0]
    name = tree.item(iid)["values"][1]
    age = tree.item(iid)["values"][2]
    city = tree.item(iid)["values"][3]
    kom = tree.item(iid)["values"][4]

    L_id.config(text=id)

    E_name.insert(0, name)
    E_age.insert(0, age)
    E_city.insert(0, city)
    E_kom.insert(0, kom)

    B2.config(state=DISABLED)
    B3.config(state=DISABLED)
    B1.config(text="Сохранить", command=lambda: save_data(tree, log_file, E_name, E_age, E_city, E_kom, L_id, B1, B2, B3, connection, cursor))


def edit_data1(tree, log_file, E_name, E_age, E_city,E_kom,E_dolz, L_id, B1, B2, B3, connection, cursor):
    global id
    iid = tree.selection()
    
    
    id = tree.item(iid)["values"][0]
    name = tree.item(iid)["values"][1]
    age = tree.item(iid)["values"][2]
    city = tree.item(iid)["values"][3]
    kom = tree.item(iid)["values"][4]
    dolz = tree.item(iid)["values"][5]

    L_id.config(text=id)

    E_name.insert(0, name)
    E_age.insert(0, age)
    E_city.insert(0, city)
    E_kom.insert(0, kom)
    E_dolz.insert(0, dolz)

    B2.config(state=DISABLED)
    B3.config(state=DISABLED)
    B1.config(text="Сохранить", command=lambda: save_data1(tree, log_file, E_name, E_age, E_city, E_kom, E_dolz, L_id, B1, B2, B3, connection, cursor))




def add_data(tree, E_name, E_age, E_city, log_file,E_kom, connection, cursor):
    

    name = E_name.get()
    age = E_age.get()
    city = E_city.get()
    kom = E_kom.get()

    
    cursor.execute("INSERT INTO tab_1 (zagolovok, opisanie, zp, kompania) VALUES (?, ?, ?, ?)", (name, age, city, kom))
    connection.commit()
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)    
    
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} добавлена\n")
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)
    E_kom.delete(0, END)


def add_data1(tree, E_name, E_age, E_city, E_kom, E_dolz, log_file, connection, cursor):
    

    name = E_name.get()
    age = E_age.get()
    city = E_city.get()
    kom = E_kom.get()
    dolz = E_dolz.get()
        
    cursor.execute("INSERT INTO tab_2 (FIO, Opit, Naviki, Ozidaemai, Dolznosti) VALUES (?, ?, ?, ?, ?)", (name, age, city, kom,dolz))
    connection.commit()
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_2")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)    
    
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)
    E_kom.delete(0, END)
    E_dolz.delete(0, END)