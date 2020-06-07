#Autor: Juan Fernando Rodríguez Díaz
from productos import producto
from algoritmos import *
import numpy as np  
def maxe(a,b):
    if a>b:
        return a
    elif b>a:
        return b

def retornaLista(cadena):
    lista = list()
    if (len(cadena))%2 == 0:
        for x,y in zip(cadena[0::2],cadena[1::2]):
            x = int(x)
            y = int(y)
            lista.append((x,y))
        return lista
    else:
        return False

print("Registe ingresando: nombre del producto \"espacio\" peso \"espacio\" valor. O escriba \"stop\" para parar")
lista = []

while True:
    entrada =input()
    if entrada == "stop":
        break
    entrada = entrada.split()
    lista.append(producto(entrada[0],int(entrada[1]),int(entrada[2])))
entrada = []
for i in lista:
    entrada.append((int(i.getPeso()),int(i.getValor())))
peso = int(input("Ingrese el peso maximo"))
print(max(entrada,peso))
matriz= np.zeros((len(lista)+1,peso+1))
print ("ssssss")
for i in range (0,len(lista)):
    print(lista[i].getPeso())
print (matriz)
print("esta es la matriz resultado")
for i in  range (1,(len(lista)+1)):
    for j in range(1,(peso+1)):
        if j>(lista[i-1].getPeso()):
            matriz[i][j] = maxe(matriz[i-1][j],matriz[i-1][j-lista[i-1].getPeso()]+lista[i-1].getValor())

print (matriz)