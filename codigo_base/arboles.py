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

def altura(raiz):
    if(raiz is None):
        return -1
    else:
        return raiz.altura

def actualizar_altura(raiz):
    if(raiz is not None):
        altura_i = altura(raiz.izq)
        altura_d = altura(raiz.der)
        raiz.altura = (altura_i if altura_i > altura_d else altura_d) + 1

def balancear(raiz):
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return

def rotar_simple(raiz, control):
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def insertar_nodo_pokemon(raiz, dato, nodo_raiz=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nodo_raiz)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nodo_raiz)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nodo_raiz)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
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