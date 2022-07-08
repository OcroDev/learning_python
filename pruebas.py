# Generadores



def generador_ciudades(*ciudades):
    for elemento in ciudades:
        for letra in elemento:
            yield letra

ciudades_generadas = generador_ciudades("Madrid","Barcelona", "Bilbao", "Valencia")

print(next(ciudades_generadas))
print(next(ciudades_generadas))


# Excepciones

try:
    print
except:
    print