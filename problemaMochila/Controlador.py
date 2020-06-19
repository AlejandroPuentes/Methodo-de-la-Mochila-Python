from Vista import Ventana
from Modelo import Modelo
from tkinter import messagebox as MessageBox

class Controlador():
    def __init__(self,vista,modelo):
        self.app = vista
        self.modelo = modelo
        self.app.boton.configure(command=self.generar_tabla)
        self.app.consultarPeso.configure(command=self.getPesos)
        self.app.consultarArticulos.configure(command=self.getArticulos)
        self.app.btnCalcular.configure(command=self.resolver)
        
        self.app.ventana.mainloop()


    def Hello(self):
        MessageBox.showinfo("Datos Articulo")

    def generar_tabla(self):
        self.app.crearTabla()
        self.app.mostrar_botones()


    def getArticulos(self):
        data = "Articulos:"
        for x in self.app.articulo:
            data = data+"\n"+x.get()
        MessageBox.showinfo("Datos Articulo", data)

    def getPesos(self):
        data = "Peso:\n"
        for x in self.app.peso:
            data = data+"\n"+x.get()
        MessageBox.showinfo("Datos Articulo", data)

    def resolver(self):
        valores = []
        pesos = []

        for x in self.app.articulo:
            valores.append(int(x.get()))
        for y in self.app.peso:
            pesos.append(int(y.get()))
        
        self.modelo.limpiar_modelo()

        peso_max = int(self.app.pesoEntrada.get())        
        
        self.modelo.set_peso_max(peso_max)

        for i in range(0,len(pesos)):
            self.modelo.agregar_producto("",pesos[i],valores[i])
        
        self.modelo.solucion()


        MessageBox.showinfo("Pasos de la solución", self.modelo.get_matriz())
        MessageBox.showinfo("Solución - Maximo valor", "Z="+str(self.modelo.get_resultado()))
    

