import sqlite3 as sql
import hashlib as hash

conn = sql.connect('data/login.db')
cursor = conn.cursor()



create_userdata_table = '''CREATE TABLE IF NOT EXISTS userdata
    (ID INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)'''


cursor.execute(create_userdata_table)


username1, password1 = "emil", hash.sha256("admin".encode()).hexdigest()

print(password1)

cursor.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username1, password1) )

conn.commit()