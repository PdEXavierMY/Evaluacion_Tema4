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

def busqueda_proximidad_pokemon(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[1])
        busqueda_proximidad_pokemon(raiz.izq, buscado)
        busqueda_proximidad_pokemon(raiz.der, buscado)

def busqueda_proximidad_pokemon_tipo(raiz, buscado):
            if(raiz is not None):
                if(raiz.info[1][0:len(buscado)] == buscado):
                    print(raiz.info[0].nombre)
                busqueda_proximidad_pokemon_tipo(raiz.izq, buscado)
                busqueda_proximidad_pokemon_tipo(raiz.der, buscado)

def inorden_numero2(raiz):
            if(raiz is not None):
                inorden_numero2(raiz.izq)
                print(raiz.info[0])
                inorden_numero2(raiz.der)