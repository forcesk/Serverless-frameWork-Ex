import sqlite3

def insertDB():

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    # Se crea la tabla items
    cur.execute('''CREATE TABLE IF NOT EXISTS items
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')

    # Insertando datos
    cur.execute("INSERT INTO items (name) VALUES ('Acceso Concedido')")
    con.commit()

    # Se imprimen las filas en items
    for row in cur.execute('SELECT * FROM items ORDER BY id'):
        print(row)

    con.close()
