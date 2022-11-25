from codigo_base.arboles import insertar_nodo, por_nivel

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