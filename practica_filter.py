#def numero_par(num):    if num % 2==0:       return True     numeros  = [ 12, 5, 32, 12, 4, 65, 7 ] print( list(filter(lambda numero_par: numero_par%2==0, numeros)))

class Empleado:

    def __init__(self, nombre, cargo ,salario):
        self.cargo  = cargo
        self.nombre  = nombre
        self.salario = salario

    def __str__ (self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
Empleado("juan", "director", 45000),
Empleado("ana", "presidente", 55000),
Empleado("jhon", "administrador", 35000),
Empleado("anto", "botones", 5000),

]


salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)

