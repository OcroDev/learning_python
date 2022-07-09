def funcion_decoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs):
        #Acciones adicionales que decoran
        print("vamos a realizar un calculo: ")

        funcion_parametro(*args, **kwargs)
      
        #acciones adicionales que decoran
        print("hemos terminado el cálculo")
    
    return funcion_interior









@funcion_decoradora
def suma(num1,num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(7,8,9)

resta(1,4)

potencia(base=5, exponente=3)