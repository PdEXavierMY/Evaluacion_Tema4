from random import randint, choice
from codigo_base.arboles import *
from codigo_base.cola import *

class Pokemon(object):
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad