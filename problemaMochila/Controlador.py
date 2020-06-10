from Vista import Aplicacion

class Controlador():
    def __init__(self,vista):
        self.app = vista
        self.app.ventana.mainloop()

