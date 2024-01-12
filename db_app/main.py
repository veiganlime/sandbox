from tkinter import *
import sqlite3

global editor_window
global root
global delete_box
global error_antwort_lable
global name
global price
global anzahl


# Databases
# Creating a database or connecting

# Creating function edit
def edit():
    # Creating a database or connecting
    conn = sqlite3.connect('coins_db.db')
    # Creating cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE coins SET
                name = :name,
                prise = :prise,
                anzahl = :anzahl 

                WHERE oid = :oid """,
              {
                  'name': name_editor.get(),
                  'prise': price_editor.get(),
                  'anzahl': anzahl_editor.get(),
                  'oid': record_id
              })
    # Commiting changes
    conn.commit()
    # close Connection
    conn.close()
    editor_window.destroy()


# Creating function update
def update():
    try:
        int(delete_box.get())
        error_antwort_lable.config(text="")

        editor_window = Tk()
        editor_window.title('Bearbeitung')
        editor_window.geometry("400x300")
        # Creating a database or connecting
        conn = sqlite3.connect('coins_db.db')
        # Creating cursor
        c = conn.cursor()
        # Select from table
        eintrag_ID = delete_box.get()
        c.execute("SELECT * FROM coins WHERE oid = " + eintrag_ID)
        eintraege = c.fetchall()
        # Creating Global Variables for text box name
        global name_editor
        global price_editor
        global anzahl_editor
        # Creating Text Boxes
        name_editor = Entry(editor_window, width=30)
        name_editor.grid(row=0, column=1, padx=20)
        price_editor = Entry(editor_window, width=30)
        price_editor.grid(row=1, column=1, padx=20)
        anzahl_editor = Entry(editor_window, width=30)
        anzahl_editor.grid(row=2, column=1, padx=20)
        # Creating text box labels
        name_editor_lable = Label(editor_window, text="Coin")
        name_editor_lable.grid(row=0, column=0)
        price_editor_lable = Label(editor_window, text="Price")
        price_editor_lable.grid(row=1, column=0)
        anzahl_editor_lable = Label(editor_window, text="Anzahl")
        anzahl_editor_lable.grid(row=2, column=0)
        # loop throught results
        for eintrag in eintraege:
            name_editor.insert(0, eintrag[0])
            price_editor.insert(0, eintrag[1])
            anzahl_editor.insert(0, eintrag[2])

        # Creating button Submit
        submit_editor_btn = Button(editor_window, text="Eintrag hinzufügen", command=edit, width=50)
        submit_editor_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

        # Commiting changes
        conn.commit()
        # close Connection
        conn.close()
    except ValueError:
        error_antwort_lable.config(text="Entry value isn't correct", fg="red")


# Creating function delete
def delete():
    try:
        int(delete_box.get())
        # Creating a database or connecting
        conn = sqlite3.connect('coins_db.db')
        # Creating cursor
        c = conn.cursor()
        # Delete from table
        c.execute("DELETE from coins WHERE oid = " + delete_box.get())

        # Commiting changes
        conn.commit()
        # close Connection
        conn.close()
    except ValueError:
        error_antwort_lable.config(text="Entry value isn't correct", fg="red")


# Creating function query
def query():
    # Creating a database or connecting
    conn = sqlite3.connect('coins_db.db')
    # Creating cursor
    c = conn.cursor()
    # Select from table
    c.execute("SELECT *, oid FROM coins")
    eintraege = c.fetchall()
    # loop through results
    eintraege_ausgabe = ''
    for eintrag in eintraege:
        eintraege_ausgabe += str(eintrag[0]) + " " + "\t" + str(eintrag[1]) + " " + "\t" + str(
            eintrag[2]) + " " + "\t" + str(eintrag[3]) + "\n"

    query_lable = Label(root, text=eintraege_ausgabe)
    query_lable.grid(row=5, column=0, columnspan=2)

    # Commiting changes
    conn.commit()
    # close Connection
    conn.close()


# Creating function Submit
def submit():
    try:
        if not name.get():
            raise ValueError
        if not price.get():
            raise ValueError
        if not anzahl.get():
            raise ValueError
    except ValueError:
        error_antwort_lable.config(text="Entry value isn't correct", fg="red")
    else:
        error_antwort_lable.config(text="")
        # Creating a database or connecting
        conn = sqlite3.connect('coins_db.db')
        # Creating cursor
        c = conn.cursor()
        # Insert into table
        c.execute("INSERT INTO coins VALUES(:name,:price,:anzahl)",
                  {
                      'name': name.get(),
                      'price': price.get(),
                      'anzahl': anzahl.get()
                  })
        # Clear the text boxes
        name.delete(0, END)
        price.delete(0, END)
        anzahl.delete(0, END)
        # Commiting changes
        conn.commit()
        # close Connection
        conn.close()

def create_table():
    conn = sqlite3.connect('coins_db.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS coins(
                           name TEXT,
                           price REAL,
                           anzahl INTEGER
                           )""")
    conn.commit()
    conn.close()


root = Tk()
root.title('CoinDB')
root.geometry("400x600")
create_table()
# Creating Text Boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20)
price = Entry(root, width=30)
price.grid(row=1, column=1, padx=20)
anzahl = Entry(root, width=30)
anzahl.grid(row=2, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=7, column=1, padx=20)
# Creating text box labels
name_lable = Label(root, text="Coin")
name_lable.grid(row=0, column=0)
price_lable = Label(root, text="Price")
price_lable.grid(row=1, column=0)
anzahl_lable = Label(root, text="Anzahl")
anzahl_lable.grid(row=2, column=0)
delete_box_label = Label(root, text="ID zu bearbeiten")
delete_box_label.grid(row=7, column=0)
error_antwort_lable = Label(root, text='')
error_antwort_lable.grid(row=9, column=0)
# Creating button Submit
submit_btn = Button(root, text="Eintrag hinzufügen", command=submit, width=50)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
# Creating a query button
query_btn = Button(root, text="Alle Einträge anzeigen", command=query, width=50)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
# Creating a delete button
delte_btn = Button(root, text="Eintrag löschen", command=delete, width=50)
delte_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
# Creating a update button
update_btn = Button(root, text="Eintrag bearbeiten", command=update, width=50)
update_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()




