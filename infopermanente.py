import pickle

class Persona():
    def __init__(self, nombre, genero, edad) :
        self.nombre=nombre
        self.genero = genero
        self.edad=edad 
        print("se ha creado una persona nueva con el nombre: ", self.nombre)

        def __str__(self):
            return "{} {} {} ".format(nombre, genero, edad)


class ListaPersonas():
    personas=[]
    def __init__(self):
        listadepersonas= open("ficheroExterno", "rb")
        listadepersonas.seek(0)
        try:
            self.personas=pickle.load(listadepersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("el fichero esta vacio")
        finally:
            listadepersonas.close()
            del(listadepersonas)

    def agregar_persona(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
   
    def mostrar_personas(self):
        for p in self.personas:
            print(p)
   
    def guardarPersonasEnFicheroExterno(self):
        listadepersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listadepersonas)
        listadepersonas.close()
        del(listadepersonas)
    
    def mostrar_info_fichero_externo(self):
        print("la informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()

#persona = Persona("otro","masculino",29)


#miLista.agregar_persona(persona)

miLista.mostrar_info_fichero_externo()
