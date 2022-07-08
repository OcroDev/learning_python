import sqlite3

conexion_bd=sqlite3.connect("GestionProductos")

cursor_bd = conexion_bd.cursor()


cursor_bd.execute(''' CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO FLOAT,
    SECCION VARCHAR(20) ) 
''')


productos = [

    ("Pelota", 20, "Juguetería"),
    ("pantalón", 15, "confección"),
    ("jarrón", 45, "cerámica"),
    ("destornillador", 25, "ferretería"),

]

cursor_bd.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

conexion_bd.commit()

conexion_bd.close()


