from productos import producto
from algoritmos import *
import numpy as np  


class Modelo():
    def __init__(self):
        self.num_elementos = 0
        self.peso_max = 0
        self.lista = []
        self.matriz = []
        self.resultado = 0
        

    def limpiar_modelo(self):
        self.num_elementos = 0
        self.peso_max = 0
        self.lista = []
        self.matriz = []
        self.resultado = 0


    def retornaLista(self,cadena):
        lista = list()
        if (len(cadena))%2 == 0:
            for x,y in zip(cadena[0::2],cadena[1::2]):
                x = int(x)
                y = int(y)
                lista.append((x,y))
            return lista
        else:
            return False

    def get_peso_max(self):
        return self.peso_max    
    def get_num_elementos(self):
        return self.num_elementos

    def set_peso_max(self,peso_max):
        self.peso_max = peso_max
    def set_num_elementos(self,num_elementos):
        self.num_elementos = num_elementos

    
    def agregar_producto(self,nombre,peso,valor):
        nuevo_producto = producto(nombre,peso,valor)
        self.num_elementos = self.num_elementos + 1
        self.lista.append(nuevo_producto)



    def solucion(self):
        self.matriz = [ [0 for x in range(self.peso_max+1)] for x in range(self.num_elementos+1)]
        print ("ssssss")

        for i in range (0,len(self.lista)):
            print(self.lista[i].getPeso())
        print (self.matriz)

        print("esta es la matriz resultado")
        for i in  range (1,self.num_elementos+1):
            for j in range(1,self.peso_max+1):
                if (self.lista[i-1].getPeso())<=j:
                    self.matriz[i][j] = np.max(( self.matriz[i-1][j], self.matriz[i-1][(j-self.lista[i-1].getPeso())] + self.lista[i-1].getValor() ))
                else:
                    self.matriz[i][j] = self.matriz[i-1][j]
        
        print (self.matriz)

        
        self.resultado = self.matriz[self.num_elementos][self.peso_max]
        
    def get_matriz(self):
        data = ""

        for i in self.matriz:
            data = data + str(i) + "\n"
        
        return data
        
    
    def get_resultado(self):
        return self.resultado


        
