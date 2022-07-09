import re

cadena = "Vamos a aprender expresioens regulares en Python. Python es un lenguaje"
texto_buscar = "Python"

#if(re.search(texto_buscar, cadena)) is not None:
 #   print("he encontrado el texto")
#else:
 #   print("no he encontrado el texto")

texto_encontrado = re.search(texto_buscar, cadena)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())
 
print(len(re.findall(texto_buscar, cadena)))


print("##########################")

lista_nombres=['ana gomez',
               'maria martin',
               'sandra lopez',
               'santiago martin']

for elemento in lista_nombres:
    if re.findall('MARTIN$', elemento.upper()):
        print(elemento)

print("##########################")

lista_nombres=['ana gomez',
               'maria martin',
               'sandra lopez',
               'santiago martin']

for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento):
        print(elemento)

lista_nombres=['Ma1', 
                'Se1', 
                'Ma2', 
                'Ba1', 
                'Ma:3', 
                'Va1', 
                'Va2', 
                'Ma4',
                'MaA',
                'Ma.5',
                'MaB',
                'Ma:C'
]

for elemento in lista_nombres:
    if re.findall('Ma[.:]', elemento):
        print(elemento)



print("##########################")


nombre1='Jara gomez'
mombre2= 'maria martin'
nombre3= 'Lara lopez'
nombre4= 'santiago martin'

if re.match("Sandra", nombre3, re.IGNORECASE):
    print("hemos encontrado el nombre")
else:
    print("no lo hemos encontrado")

if re.search("lopez", nombre3, re.IGNORECASE):
    print("hemos encontrado el nombre")
else:
    print("no lo hemos encontrado")