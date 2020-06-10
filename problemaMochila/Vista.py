from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

class Aplicacion():

    def crearTabla(self):
        x1 = 0
        y1 = 0
        if not self.variablesEntrada.get() and not self.restriccionesEntrada.get():
            MessageBox.showerror("ERROR", "Por favor llene los espacios")
        else:
            for b in range(int(self.restriccionesEntrada.get())):
                x1 = 0
                for i in range(int(self.variablesEntrada.get())):
                    self.entradas = ttk.Entry(self.ventana, width = 5)
                    self.entradas.place(x=10 + x1, y = 200 + y1)
                    self.variablesx = ttk.Label(self.ventana, text = "x" + str(i), width = 5, font = ("Helvetica","10"))
                    self.variablesx.place(x=50 + x1,y=200 +y1)
                    x1 += 70
                self.botonIgual = ttk.Button(self.ventana, text = "≥", width = 3)
                self.botonIgual.place(x=20+x1,y=200+y1)
                self.igualA = ttk.Entry(self.ventana, width = 5)
                self.igualA.place(x=60+x1,y=200+y1)
                y1 += 40

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
        self.variables = Label(self.ventana, text = "Variables:",width = 15, font=("Helvetica","15"))
        self.variables.pack(anchor = NW)
        self.restricciones = Label(self.ventana, text = "Restricciones:", width = 15, font = ("Helvetica","15"))
        self.restricciones.pack(anchor = NW)

        #Entradas
        self.variablesEntrada = ttk.Entry(self.ventana)
        self.variablesEntrada.place(x=150,y=72)
        self.restriccionesEntrada = ttk.Entry(self.ventana)
        self.restriccionesEntrada.place(x=150,y=102)

        #Boton
        self.boton = ttk.Button(self.ventana, text = "Listo", command = self.crearTabla)
        self.boton.place(x=150, y=150)
        
        #Frame
        frame = Frame(self.ventana)
        frame.pack()

        
        
