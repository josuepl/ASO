'''archivo = open("datos.txt")
print(archivo)
#print(archivo.read())
#print(archivo.readline(),"-->Linea 1")
#print(archivo.readline(), "-->Linea 2")
lineas =archivo.readlines()
print(lineas)
print(lineas[0])
palabras = lineas[0].split()
print(palabras)
print(palabras[0], " -", palabras[1], "-", palabras[2])
valor1 = palabras[0]
valor2 = palabras[1]
print(valor1," ",valor2)
'''
class Dato:
    def __init__(self, val1, val2, val3, val4) -> None:
        self.val1 = int(val1)
        self.val2 = int(val2)
        self.val3 = int(val3)
        self.val4 = int(val4)
        pass
    def __str__(self) -> str:
        cad = "val1:"+str(self.val1)+"\t|val2:"+str(self.val2)+"\t|val3:"+str(self.val3)+"\t|val4:"+str(self.val4)
        return cad
    
    def __gt__(self, dato):
        return self.val2 > dato.val2
    
    pass

listaDatos = []
palabras = []
archivo = open("datos.txt")
for line in archivo.readlines():
    print(line)
    for palabra in line.split():
        palabras.append(palabra)
    obj = Dato(palabras[0], palabras[1],palabras[2], palabras[3])
    listaDatos.append(obj)
    palabras.clear()
    pass
print("PID\t|TLL\t|TEXE\t|PRIO\t|")
for elem in listaDatos:
    print(elem)

newL = sorted(listaDatos)
print("================================================================")
print("PID\t|TLL\t|TEXE\t|PRIO\t|")
for elem in newL:
    print(elem)
listEsp=[]
listExe=[]
temp= newL.pop(0)
print("PID:", temp.val1)
listExe.append(temp)
temp= newL.pop(0)
print("PID:",temp.val1)
listExe.append(temp)
temp= newL.pop(0)
print("PID:",temp.val1)
listExe.append(temp)
print("================================================================")
print("PID\t|TLL\t|TEXE\t|PRIO\t|")
for elem in newL:
    print(elem)
print("================================================================")
print("PID\t|TLL\t|TEXE\t|PRIO\t|")
for elem in listExe:
    print(elem)