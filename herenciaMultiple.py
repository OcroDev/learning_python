class Persona():
    def __init__(self, nombre , edad , lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print( "nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia )

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "Antiguedad", self.antiguedad)


antonio = Empleado(15000, 2, "antonio", "22", "Argentina")

antonio.descripcion()

print(isinstance(antonio, Persona))