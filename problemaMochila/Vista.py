from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

class Aplicacion():

    def __init__(self):
        #Configuracion ventana
        self.ventana = Tk()
        self.ventana.title("Programacion entera binaria")
        self.ventana.geometry('500x500')
        self.ventana.resizable(width = False, height = False)

        self.peso = []
        self.articulo = []


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
        
        self.consultarPeso = ttk.Button(self.ventana, text = "Consultar Datos Peso", command = self.getPesos)
        self.consultarPeso.place(x=50, y=450)

        self.consultarArticulos = ttk.Button(self.ventana, text = "Consultar Datos Articulos", command = self.getArticulos)
        self.consultarArticulos.place(x=250, y=450)


        #Frame
        frame = Frame(self.ventana)
        frame.pack()

    def crearTabla(self):
        x1 = 0
        if not self.pesoEntrada.get() or not self.articulosEntrada.get():
            MessageBox.showerror("ERROR", "Por favor llene los espacios")
        else:
            try:
                valorPesoEntrada = int(self.pesoEntrada.get())
                valorArticulosEntrada = int(self.articulosEntrada.get())
                if valorPesoEntrada < 0:
                    MessageBox.showerror("ERROR", "Por favor, el peso debe ser positivo")
                elif valorArticulosEntrada < 0:
                    MessageBox.showerror("ERROR", "Por favor, la cantidad de articulos debe ser positiva")
                else:
                    
                    peso = ttk.Label(self.ventana, text = "Pesos", width = 5, font=("Helvetica","11"))
                    peso.place(x=10,y=200)
                    
                    articulo = ttk.Label(self.ventana, text = "Valores", width = 10, font=("Helvetica","11"))
                    articulo.place(x=1,y=250)
                    
                    if len(self.peso) > 0:
                        for x in self.peso:
                            x.destroy()
                        for y in self.articulo:
                            y.destroy()
                        self.peso = []
                        self.articulo = []


                    for x in range(int(self.articulosEntrada.get())):
                        temp = ttk.Entry(self.ventana, width = 5)
                        temp.place(x=70+x1, y= 200)
                        self.peso.append(temp)
                        x1 += 50
                        

                    x1 = 0
                    
                    for y in range(int(self.articulosEntrada.get())):
                        temp = ttk.Entry(self.ventana, width = 5)
                        temp.place(x=70+x1, y= 250)
                        self.articulo.append(temp)
                        x1 += 50                

            except ValueError:
                MessageBox.showerror("ERROR", "Por favor, el peso debe ser positivo")



    def getPesos(self):
        data = "Peso:\n"
        for x in self.peso:
            data = data+"\n"+x.get()
        MessageBox.showinfo("Datos Articulo", data)

    def getArticulos(self):
        data = "Articulos:"
        for x in self.articulo:
            data = data+"\n"+x.get()
        MessageBox.showinfo("Datos Articulo", data)

        
            

        
        
