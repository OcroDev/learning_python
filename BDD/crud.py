import sqlite3

conexion_bd=sqlite3.connect("GestionProductos")

cursor_bd = conexion_bd.cursor()

#leer un registro en la BD (read)
#cursor_bd.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección' ")
#productos = cursor_bd.fetchall()
#print(productos)

#actualizar un registro (update)
#cursor_bd.execute("UPDATE PRODUCTOS SET PRECIO = 50 WHERE NOMBRE_ARTICULO='Pelota' ")


#eliminar un registro
cursor_bd.execute("DELETE FROM PRODUCTOS WHERE ID= 4")



conexion_bd.commit()

conexion_bd.close()


