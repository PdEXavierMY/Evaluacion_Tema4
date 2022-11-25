from codigo_base.cola import *

class nodoArbol(object):
    def __init__(self, info, nodo_raiz=None):
        self.izq = None
        self.der = None
        self.info = info
        self.nodo_raiz = nodo_raiz


class ArbolBinario(object):
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion


class ArbolHuffman(object):
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor


def insertar_nodo(raiz, dato, nodo_raiz=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nodo_raiz)
    elif (raiz.info > dato):
        raiz.izq = insertar_nodo(raiz.izq, dato, nodo_raiz)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, nodo_raiz)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def busqueda(raiz, buscado):
    pos = None
    if(raiz is not None):
        if(raiz.info == buscado):
            pos = raiz
        elif (raiz.info > buscado):         
            pos = busqueda(raiz.izq, buscado)
        else:
            pos = busqueda(raiz.der, buscado)
    return pos

def arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x