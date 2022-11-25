class Pokemon(object):
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad


def inorden_numero(raiz):
            if(raiz is not None):
                inorden_numero(raiz.izq)
                print(raiz.info[1], raiz.info[0])
                inorden_numero(raiz.der)