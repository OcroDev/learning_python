class Coche():
    def desplazamiento(self):
        print("tengo 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("tengo 2 ruedas")
    
class Camion():
    def desplazamiento(self):
        print("tengo 6 ruedas ")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Coche()

desplazamientoVehiculo(miVehiculo)