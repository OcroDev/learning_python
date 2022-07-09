import doctest
from operator import truediv

def area_triangulo(base,altura):
    """
    calcula el area de un triangulo dado
    
    >>> area_triangulo(3,6)
    'El área del triángulo es: 9.0'
    >>> area_triangulo(4,5)
    'El área del triángulo es: 10.0'
    >>> area_triangulo(9,3)
    'El área del triángulo es: 13.5'
    """
    return "El área del triángulo es: "+str((base*altura)/2)

def comprobarmail(email):
    """
    la funcion evalua un mail recibido en busca de la @ si tiene una @ es correcto,
    si tiene mas de una @ es incorrecto, si la @ está al final es incorrecto

    >>> comprobarmail('rohe@curso.com')
    True
    >>> comprobarmail('rohecurso.com@')
    False
    >>> comprobarmail('rohecurso.com')
    False
    >>> comprobarmail('rohe@curso@.es')
    False

    """
    arroba=email.count('@')

    if(arroba!=1 or email.rfind('@')==(len(email)-1) or email.find('@')==0):
        return False
    else:
        return True

doctest.testmod()
