from codigo_base.arboles import insertar_nodo, por_nivel, ArbolHuffman

def ordenar_tabla_por_probabilidad(lista):
    tabla_ordenada = []
    while len(lista) > 0:
        min = [None, 1]
        for element in lista:
            if element[1] < min[1]:
                min = element
        tabla_ordenada.append(min)
        lista.remove(min)
    return tabla_ordenada

def ordenar_nodo_por_probabilidad(lista):
    tabla_ordenada = []
    while len(lista) > 0:
        min = ArbolHuffman(None, 1.01)
        for i in range(len(lista)):
            if lista[i].valor < min.valor:
                min = ArbolHuffman(None, lista[i].valor)
                posicion = i
        tabla_ordenada.append(lista[posicion])
        lista.pop(posicion)
    return tabla_ordenada