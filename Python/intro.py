#variables
'''
Esto es un cmentario multilinea
'''
'''

cadena = "cadena"
print("contenido:", cadena)
cadena = 1
print("contenido:", cadena)
cadena = 1.5
print("contenido:", cadena)
'''
def func():
    lista =[]
    
    lista.append("uno")
    lista.append(1)
    lista.append(True)
    lista.append(2.5)
    lista[0] = "PI"
    print(lista)
    for ix in range(0, lista.__len__()):
        print(lista[ix])
    for item in lista:
        print(item)
    print(lista.pop(0))
    print(lista)
    pass

def funt():
    tupla = ('uno', 2, 3.3, True)
    tupla[0]= 'dos'
    return tupla
    pass

def fund():
    diccion ={}
    diccion={'persona1':{'nombre':'Josue',
             'edad': 16,
             'ocup': "NINI"},
             'persona2':{'nombre':'Otro',
             'edad': 56,
             'ocup': "NONI"}}
    print(diccion)
    print(diccion['persona1'],diccion["persona2"])
    pass
#func()
#a = funt()
#print(a)
#fund()

class Persona:
    lista = []
    dic = {}
    tupla = ()
    def __init__(self, nombre, edad, ocup) -> None:
        self.nombre = nombre
        self.edad = edad
        self.ocup = ocup
        pass
    pass

p1 = Persona("Josue",16,"nini")
print(p1)
print(p1.nombre, p1.lista, p1.dic, p1.tupla)