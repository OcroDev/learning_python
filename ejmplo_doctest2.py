import math
import doctest

def raiz_cuadrada(lista_numeros):
    """
    la funcion devuelve una lista con la raiz
    cuadrada de los elementos numericos
    pasados por parametros en otra lista
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raiz_cuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,-9,16,50,60]:
    ...     lista.append(i)
    >>> raiz_cuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """
    
    return [math.sqrt(n) for n in lista_numeros]


#print (raiz_cuadrada([9,-16,25,36]))

doctest.testmod()