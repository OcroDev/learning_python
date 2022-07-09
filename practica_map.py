#def numero_par(num):    if num % 2==0:       return True     numeros  = [ 12, 5, 32, 12, 4, 65, 7 ] print( list(filter(lambda numero_par: numero_par%2==0, numeros)))

class Empleado:

    def __init__(self, nombre, cargo ,salario):
        self.cargo  = cargo
        self.nombre  = nombre
        self.salario = salario

    def __str__ (self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
Empleado("juan", "director",6700),
Empleado("ana", "presidente", 15000),
Empleado("jhon", "administrador", 3500),
Empleado("anto", "botones", 1800),

]


def calculo_comision(empleado):
    if (empleado.salario <=3000):
        empleado.salario = empleado.salario*1.03
    return empleado 

listaEmpleadosComision = map(calculo_comision, listaEmpleados)


for empleado in listaEmpleadosComision:
    print(empleado)
