import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('my_database.db')

# Crear un cursor
c = conn.cursor()

# Crear una tabla

c.execute("""CREATE TABLE addresses(
  first_name text,
  last_name text,
  address text,
  city text,
  state text,
  zipcode integer
)""")
conn.commit()
conn.close()
