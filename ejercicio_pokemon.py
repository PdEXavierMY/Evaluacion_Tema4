from codigo_base.cola import *

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

def inorden_nombre(raiz):
            if(raiz is not None):
                inorden_nombre(raiz.izq)
                print(raiz.info[0])
                inorden_nombre(raiz.der)

def por_nivel_nombre(raiz):
            cola = Cola()
            arribo(cola, raiz)
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info[0])
                if(nodo.izq is not None):
                    arribo(cola, nodo.izq)
                if(nodo.der is not None):
                    arribo(cola, nodo.der)

def busqueda_proximidad_pokemon_debilesa(raiz, buscado):
            if(raiz is not None):
                if(raiz.info[0].debilidad[0:len(buscado)] == buscado):
                    print(raiz.info[0].nombre)
                busqueda_proximidad_pokemon_debilesa(raiz.izq, buscado)
                busqueda_proximidad_pokemon_debilesa(raiz.der, buscado)

def inorden_tipo(raiz, contador):
            if(raiz is not None):
                if raiz.info[0].tipo == 'fuego':
                    contador += 1
                inorden_tipo(raiz.izq, contador)
                print(raiz.info[0].nombre, raiz.info[0].tipo)
                inorden_tipo(raiz.der, contador)
            return contador