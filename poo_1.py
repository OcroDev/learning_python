class Coche():
    #constructor
    def __init__(self):
        #propiedades
        self.__largo_chasis=250
        self.__ancho_chasis= 120
        self.__ruedas = 4
        self.__en_marcha=False

    #metodos
    def arrancar( self, arrancamos) :
        self.__en_marcha = arrancamos
        if ( self.__en_marcha ):
            chequeo=self.__comprobcion_interna()

        if ( self.__en_marcha and chequeo ):
            return "El coche esta en marcha"
        elif ( self.__en_marcha and chequeo==False ):
            return "Algo ha ido mal en la comprobación interna, no podemos arrancar"
        else:
            return "el coche está detenido"

        
    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. un ancho de ", self.__ancho_chasis, " y un largo de ", self.__largo_chasis)

    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas

    def __comprobcion_interna(self):
        print("realizando comprobación interna")
        self.gasolina = "ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


#creando objeto
miCoche = Coche()

print(miCoche.arrancar(1))
miCoche.estado()
print("segundo objeto")

miCoche2  = Coche()
print(miCoche.arrancar(0))
miCoche2.estado()
