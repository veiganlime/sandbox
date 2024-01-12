
import sqlite3


def create_table(conn):
    conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    NOT NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);''')


def insert(conn):
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (1, 'Niko', 32, 'Berlin', 20000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (2, 'Patrik', 20, 'Berlin', 25000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (3, 'Vincent', 25, 'Köln', 24000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (4, 'Laura', 35, 'Oberhausen', 28000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (5, 'Amelia', 60, 'Dortmund', 60000.00)
            """)
    conn.commit()


def main():
    conn = sqlite3.connect('data/Company.db')

    #create_table(conn)

    insert(conn)

    conn.close()


if __name__ == "__main__":
    main()

import sqlite3


def create_table(conn):
    conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    NOT NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);''')


def insert(conn):
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (1, 'Niko', 32, 'Berlin', 20000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (2, 'Patrik', 20, 'Berlin', 25000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (3, 'Vincent', 25, 'Köln', 24000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (4, 'Laura', 35, 'Oberhausen', 28000.00)
        """)
    conn.execute("""
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (5, 'Amelia', 60, 'Dortmund', 60000.00)
            """)
    conn.commit()


def main():
    conn = sqlite3.connect('data/Company.db')

    #create_table(conn)

    insert(conn)

    conn.close()


if __name__ == "__main__":
    main()

