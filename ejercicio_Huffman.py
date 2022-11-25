from codigo_base.arboles import insertar_nodo, por_nivel

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
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
print(ordenar_tabla_por_probabilidad(tabla))