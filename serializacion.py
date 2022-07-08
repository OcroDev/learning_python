import pickle 

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha= False
        self.acelera=False
        self.frena=False


    def arranacar(self):
        self.en_marcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frenar=True
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.en_marcha, 
        "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "la furgoneta esta ta cargada"
        else:
            return "no esta cargada"


class Moto(Vehiculos):
    hace_caballito=""
    
    def caballito(self):
        self.hace_caballito="voy haciendo caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\n ", self.hace_caballito)

class Vehiculos_electricos(Vehiculos):
    def __init__( self, marca, modelo ):
        
        super().__init__(marca, modelo)
        
        self.autonomia=100

    def cargar_energia(self):
        self.cargando = True

class Bicicleta_electrica(Vehiculos_electricos, Vehiculos):
        pass

coche1 = Vehiculos("mazda","mx5")
coche2 = Vehiculos("seat","leon")
coche3 = Vehiculos("renault","megane")

coches = [coche1, coche2, coche3]

fichero = open("loscoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

ficheroapertura = open("loscoches","rb")

misCoches = pickle.load(ficheroapertura)

ficheroapertura.close()

for c in misCoches:
    c.estado()

