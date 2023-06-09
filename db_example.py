import sqlite3, json

# Hay que crear una conexión a la base de datos desde este documento Python
conn = sqlite3.connect("example.db")

# Crear un objeto cursor. El cursor permite realizar consultas a la base de datos.
cursor = conn.cursor()

# Le pasamos los comandos a execute() para que el cursor los ejecute.
# Acá creamos una tabla (solo ejecutar una vez, la primera vez):
cursor.execute('''
    CREATE TABLE users
    (id INTEGER PRIMARY KEY,
     name TEXT,
     age INTEGER)
''')


# Se pueden hacer tantos execute() como sean necesarios y van a irse añadiendo a la DB.
# Con INSERT, insertamos registros a nuestra DB:
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Sebastian', 11))

# cursor.execute('''
#     INSERT INTO users (name, age) VALUES (?, ?)
# ''', ('Tobias', 14))


# Podemos hacer SELECT y guardar los registros en una variable
cursor.execute("SELECT * FROM users")
registros = cursor.fetchall()

# Lista de tuples
print(registros)

# El [0] es la primera fila, el [1] es la segunda columna (name)
print(registros[0][1])

for fila in registros:
    print(fila) # Se imprime cada fila

conn.commit() # Se committean los cambios a la DB
conn.close() # Se cierra la conexión una vez realizados y committeados los cambios



