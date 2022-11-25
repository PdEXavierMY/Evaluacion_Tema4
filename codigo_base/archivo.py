import shelve


def abrir(ruta):
    return shelve.open(ruta)


def cerrar(archivo):
    archivo.close()


def leer(archivo, pos):
    return archivo[str(pos)]


def guardar(archivo, reg):
    archivo[str(len(archivo))] = reg

def modificar(archivo, pos, reg):
        archivo[str(pos)] = reg