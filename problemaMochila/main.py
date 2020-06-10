from Controlador import Controlador
from Vista import Aplicacion

class programacionBinaria():
    def __init__(self):
        v = Aplicacion()
        c = Controlador(v)

def main():
    programacionBinaria()
    return 0

if __name__ == '__main__':
    main()
