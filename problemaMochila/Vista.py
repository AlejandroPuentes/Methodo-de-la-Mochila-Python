from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

class Aplicacion():

    def crearTabla(self):
        x1 = 0
        if not self.pesoEntrada.get() or not self.articulosEntrada.get():
            MessageBox.showerror("ERROR", "Por favor llene los espacios")
        else:
            peso = ttk.Label(self.ventana, text = "Pesos", width = 5, font=("Helvetica","11"))
            peso.place(x=10,y=200)
            articulo = ttk.Label(self.ventana, text = "Valores", width = 10, font=("Helvetica","11"))
            articulo.place(x=1,y=250)
            
            for x in range(int(self.articulosEntrada.get())):
                self.peso = ttk.Entry(self.ventana, width = 5)
                self.peso.place(x=70+x1, y= 200)
                x1 += 50

            x1 = 0
            
            for y in range(int(self.articulosEntrada.get())):
                self.articulo = ttk.Entry(self.ventana, width = 5)
                self.articulo.place(x=70+x1, y= 250)
                x1 += 50

    def __init__(self):
        #Configuracion ventana
        self.ventana = Tk()
        self.ventana.title("Programacion entera binaria")
        self.ventana.geometry('500x500')
        self.ventana.resizable(width = False, height = False)

        #Presentacion
        cristhian = Label(self.ventana, text = "Cristhian Camilo Martinez Rey - 20181020021", width = 40, font = ("Helvetica","10"))
        cristhian.pack(anchor = CENTER)
        alejandro = Label(self.ventana, text = "Brayan Alejandro Puentes - 20181020044", width = 40, font = ("Helvetica","10"))
        alejandro.pack(anchor = CENTER)
        brayan = Label(self.ventana, text = "Jose Alejandro Pintor Gonzales - 20152020054", width = 40, font = ("Helvetica","10"))
        brayan.pack(anchor = CENTER)
        
        #Labels
        self.variables = Label(self.ventana, text = "Peso limite",width = 15, font=("Helvetica","15"))
        self.variables.pack(anchor = NW)
        self.restricciones = Label(self.ventana, text = "Articulos:", width = 15, font = ("Helvetica","15"))
        self.restricciones.pack(anchor = NW)

        #Entradas
        self.pesoEntrada = ttk.Entry(self.ventana)
        self.pesoEntrada.place(x=150,y=72)
        self.articulosEntrada = ttk.Entry(self.ventana)
        self.articulosEntrada.place(x=150,y=102)

        #Boton
        self.boton = ttk.Button(self.ventana, text = "Listo", command = self.crearTabla)
        self.boton.place(x=150, y=150)
        
        #Frame
        frame = Frame(self.ventana)
        frame.pack()

        
        
