class nodoCola(object):
    def __init__(self):
        self.info, self.sig = None, None

class Cola(object):
    def __init__(self):
        self.frente, self.final, self.tamanio = None, None, 0


def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if(cola.final is None):
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if(cola.frente is None):
        cola.final = None
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    return cola.frente is None


def tamanio(cola):
    return cola.tamanio

def en_frente(cola):
    return cola.frente.info

def mover_final(cola):
    dato = atencion(cola)
    arribo(cola, dato)
    return dato