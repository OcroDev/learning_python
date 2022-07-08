import sqlite3

conexionBd=sqlite3.connect("PrimeraBase")

cursor_bd = conexionBd.cursor()

#PARA CREAR UNA TABLA
#cursor_bd.execute( "CREATE TABLE PRODUCTOS ( NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20) ) " )

#INSERTAR DATOS
#cursor_bd.execute( "INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES') " )

    #insertar varios datos a la vez
#varios_productos=[
#    ("Camiseta", 10, "Deportes"),
 #   ("Jarrón", 90, "Cerámica"),
#    ("Camión", 10, "Juguetería"),
#]

#cursor_bd.executemany( "INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos )

cursor_bd.execute( "SELECT * FROM PRODUCTOS" )

varios_productos = cursor_bd.fetchall()

for producto in varios_productos:
    print("Nombre: ",producto[0], "| seccion: ", producto[2])

#para confirmar la ejecución del query
conexionBd.commit()



conexionBd.close()


