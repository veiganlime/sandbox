from tkinter import *
import sqlite3

root = Tk()
root.title('CoinDB')
root.geometry("400x400")

#Databases
#Creating a database or connecting
conn = sqlite3.connect('coins_db.db')
#Creating cursor
c = conn.cursor()
#Creating table
'''c.execute("""CREATE TABLE coins(
        name,
        prise,
        anzahl
        )""")'''
#Creating function delete
def delete():
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
#Creating function query
def query():
    # Creating a database or connecting
    conn = sqlite3.connect('coins_db.db')
    # Creating cursor
    c = conn.cursor()
    #Select from table
    c.execute("SELECT *, oid FROM coins")
    eintraege = c.fetchall()

    #loop thrue results
    eintraege_ausgabe = ''
    for eintrag in eintraege:
        eintraege_ausgabe += str(eintrag[0]) + " " + "\t" + str(eintrag[1]) + " " + "\t" + str(eintrag[2]) + " " + "\t" + str(eintrag[3]) +  "\n"
    query_lable = Label(root, text=eintraege_ausgabe)
    query_lable.grid(row=5, column=0, columnspan=2)

    # Commiting changes
    conn.commit()
    # close Connection
    conn.close()
#Creating function Submit
def submit():
    # Creating a database or connecting
    conn = sqlite3.connect('coins_db.db')
    # Creating cursor
    c = conn.cursor()
    #Insert into table
    c.execute("INSERT INTO coins VALUES(:name,:price,:anzahl)",
              {
                  'name' : name.get(),
                  'price' : price.get(),
                  'anzahl' : anzahl.get()
              })

    #Clear the text boxes
    name.delete(0, END)
    price.delete(0, END)
    anzahl.delete(0, END)

    # Commiting changes
    conn.commit()
    # close Connection
    conn.close()
# Creating Text Boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20)
price = Entry(root, width=30)
price.grid(row=1, column=1, padx=20)
anzahl = Entry(root, width=30)
anzahl.grid(row=2, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=7, column=1, padx=20)

#Creating text box labels
name_lable = Label(root, text="Coin")
name_lable.grid(row=0, column=0)
price_lable = Label(root, text="Price")
price_lable.grid(row=1, column=0)
anzahl_lable = Label(root, text="Anzahl")
anzahl_lable.grid(row=2, column=0)
delete_box_label = Label(root, text="ID zu löschen")
delete_box_label.grid(row=7,column=0)

# Creating button Submit
submit_btn = Button(root, text="Eintrag hinzufügen", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2,pady=10, padx=10, ipadx=100)

#Creating a query button
query_btn = Button(root, text="Alle Einträge anzeigen", command=query)
query_btn.grid(row=4, column=0, columnspan=2,pady=10, padx=10, ipadx=93)

#Creating a delete button
delte_btn = Button(root, text="Eintrag löschen", command=delete)
delte_btn.grid(row=6, column=0, columnspan=2,pady=10, padx=10, ipadx=110)
#Commiting changes
conn.commit()
#close Connection
conn.close()

#print(conn)
root.mainloop()