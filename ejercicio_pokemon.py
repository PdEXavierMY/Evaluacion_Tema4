from codigo_base.cola import *
from codigo_base.archivo import *

class Pokemon(object):
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad


def inorden_pokemon_nombre(raiz, archivo):
    if raiz is not None:
        inorden_pokemon_nombre(raiz.izq, archivo)
        poke = leer(archivo, raiz.nodo_raiz)
        if poke.nombre:
            print(raiz.info,'-', poke.numero)
        inorden_pokemon_nombre(raiz.der, archivo)


def inorden_pokemon_numero(raiz, archivo):
    if raiz is not None:
        inorden_pokemon_numero(raiz.izq, archivo)
        poke = leer(archivo, raiz.nodo_raiz)
        if poke.numero:
            print(raiz.info,'-', poke.nombre)
        inorden_pokemon_numero(raiz.der, archivo)


def inorden_debilidad(raiz, archivo, clave):
    if raiz is not None:
        inorden_debilidad(raiz.izq, archivo, clave)
        poke = leer(archivo, raiz.nodo_raiz)
        if poke.debilidad.find(clave) > -1:
            print(raiz.info, 'presenta debilidad al tipo', clave, '-', poke.debilidad)
        inorden_debilidad(raiz.der, archivo, clave)

def busqueda_proximidad_pokemon(raiz, buscado):
    if raiz is not None:
        if raiz.info[0:len(buscado)] == buscado:
            print('Se encontro:', raiz.info)
        busqueda_proximidad_pokemon(raiz.izq, buscado)
        busqueda_proximidad_pokemon(raiz.der, buscado)

def inorden_tipo(raiz, archivo):
    if raiz is not None:
        inorden_tipo(raiz.izq, archivo)
        pokemon = leer(archivo, raiz.nodo_raiz)
        if pokemon.tipo.find('agua') > -1 or pokemon.tipo.find('fuego') > -1 or pokemon.tipo.find('planta') > -1 or pokemon.tipo.find('electrico') > -1:
            print(raiz.info,'es de tipo', pokemon.tipo)
        inorden_tipo(raiz.der, archivo)