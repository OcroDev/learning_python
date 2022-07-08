#funcion normal
def area_triangulo(base, altura):
    return(base*altura)/2

print(area_triangulo(5,7))
print(area_triangulo(9,6))

#funcion lambda
#1
area_triangulo=lambda base, altura: (base*altura)/2
print("lambda:",area_triangulo(2,3))

#2
al_cubo = lambda numero:pow(numero, 3)
print(al_cubo(13))

#3
destacar_valor = lambda comision:"¡{}! $".format(comision)
comision_ana=123412
print(destacar_valor(comision_ana))



