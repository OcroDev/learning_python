class Areas():
    def area_cuadrado(lado):
        """calcula el area de un cuadrado elevando al cuadrado el lado pasado por parametro """
        lado=3*3
        """tambien multiplica el area"""

        return "el area del cuadrado es: " + str(lado*lado)

    def area_triangulo(base, altura):
        """calcula el area del triangulo"""
        return "el area del triangulo es: " + (str(base*altura)/2)


help(Areas.area_cuadrado)
help(Areas.area_triangulo)

help(Areas)
#print(area_cuadrado(3))
