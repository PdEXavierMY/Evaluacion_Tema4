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

def generar_Huffman(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_Huffman(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_Huffman(raiz.der, cadena)

def decodificar(cadena, huffman):
    cadena_i = ''
    raiz_aux = huffman
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_i += raiz_aux.info
            raiz_aux = huffman
        cadena_i
    return cadena_i

def codificar(cadena, dic):
    cadena_cod = ''
    for split in cadena:
        cadena_cod += dic[split]
    return cadena_cod