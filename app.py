from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def erase_fields_main():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    return


def erase_fields_editor():
    f_name_editor.delete(0, END)
    l_name_editor.delete(0, END)
    address_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zipcode_editor.delete(0, END)
    return


def get_data():

    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    erase_fields_main()
    c.execute("SELECT *, oid FROM addresses")
    data = c.fetchall()
    print_data = ''
    for item in data:
        print_data += str(item[0])+"  "+str(item[1]) + \
            "\t \t" + str(item[6]) + '\n'
    query_label = Label(window, text=print_data)
    query_label.grid(row=20, column=0, columnspan=2)
    conn.commit()
    conn.close()
    return


def send_database():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    # INSERT INTO TABLE

    c.execute(
        "INSERT INTO addresses VALUES (:f_name,:l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })
    erase_fields_main()
    conn.commit()
    conn.close()
    return


def delete_entry():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    erase_fields_main()
    c.execute("DELETE from addresses where oid="+delete_box.get())
    conn.commit()
    conn.close()
    return


def update_entry():
    entry_id = delete_box.get()
    print(entry_id)
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("""UPDATE addresses SET
              first_name =:first,
              last_name =:last,
              address =:address,
              city =:city,
              state =:state,
              zipcode =:zipcode
              WHERE oid=:oid""",
              {
                  'first': f_name_editor.get(),
                  "last": l_name_editor.get(),
                  "address": address_editor.get(),
                  "city": city_editor.get(),
                  "state": state_editor.get(),
                  "zipcode": zipcode_editor.get(),
                  'oid': entry_id
              })
    erase_fields_editor()
    query_label_editor = Label(editor, text="Actualizado")
    query_label_editor.grid(row=20, column=0, columnspan=2)
    conn.commit()
    conn.close()
    editor.destroy()
    return


def show_update_form():
    global editor
    editor = Tk()
    editor.title('Actualizar entrada')
    editor.geometry("400x300")
    entry_id = delete_box.get()
    print(entry_id)
    global f_name_editor
    global l_name_editor
    global city_editor
    global state_editor
    global address_editor
    global zipcode_editor

    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()
    c.execute("SELECT *, oid from addresses where oid="+entry_id)

    # Text Box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=5)

    l_name_editor = Entry(editor, width=30, text="dasd")
    l_name_editor.grid(row=1, column=1, padx=20, pady=5)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20, pady=5)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20, pady=5)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20, pady=5)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20, pady=5)

    # Text Label
    f_name_label_editor = Label(editor, text="Nombre")
    f_name_label_editor.grid(row=0, column=0)

    l_name_label_editor = Label(editor, text="Apellido")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Dirección")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="Ciudad")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="Pais")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Código postal")
    zipcode_label_editor.grid(row=5, column=0)

    submit_button_editor = Button(
        editor, text="Guardar", command=update_entry)
    submit_button_editor.grid(row=6, column=0, padx=10, pady=10,
                              ipadx=100, columnspan=137)
    data = c.fetchone()
    f_name_editor.insert(0, data[0])
    l_name_editor.insert(0, data[1])
    address_editor.insert(0, data[2])
    city_editor.insert(0, data[3])
    state_editor.insert(0, data[4])
    zipcode_editor.insert(0, data[5])
    conn.commit()
    conn.close()
    return


window = Tk()
window.title('SQL')
window.geometry("400x700")
# Text Box
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20, pady=5)

l_name = Entry(window, width=30)
l_name.grid(row=1, column=1, padx=20, pady=5)

address = Entry(window, width=30)
address.grid(row=2, column=1, padx=20, pady=5)

city = Entry(window, width=30)
city.grid(row=3, column=1, padx=20, pady=5)

state = Entry(window, width=30)
state.grid(row=4, column=1, padx=20, pady=5)

zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1, padx=20, pady=5)

delete_box = Entry(window, width=30)
delete_box.grid(row=9, column=1, padx=20, pady=5)
# Text Label
f_name_label = Label(window, text="Nombre")
f_name_label.grid(row=0, column=0)

l_name_label = Label(window, text="Apellido")
l_name_label.grid(row=1, column=0)

address_label = Label(window, text="Dirección")
address_label.grid(row=2, column=0)

city_label = Label(window, text="Ciudad")
city_label.grid(row=3, column=0)

state_label = Label(window, text="Pais")
state_label.grid(row=4, column=0)

zipcode_label = Label(window, text="Código postal")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(window, text="ID")
delete_box_label.grid(row=9, column=0)

# Guardar en la base
submit_button = Button(
    window, text="Guardar", command=send_database)
submit_button.grid(row=6, column=0, padx=10, pady=10,
                   ipadx=100, columnspan=137)


query_btn = Button(window, text="Mostrar los registros", command=get_data)
query_btn.grid(row=7, column=0, padx=10, pady=10,
               columnspan=137)

delete_btn = Button(window, text="Borrar entrada", command=delete_entry)
delete_btn.grid(row=10, column=0, padx=10, pady=10,
                columnspan=136)

update_btn = Button(window, text="Actualizar entrada",
                    command=show_update_form)
update_btn.grid(row=11, column=0, padx=10, pady=10,
                columnspan=136)
window.mainloop()
