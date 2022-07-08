from cgitb import text
from io import open

archivo = open("archivo.txt", "r")


texto = archivo.read()

archivo.close()

print(texto)