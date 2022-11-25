from ejercicio_Huffman import *
from codigo_base.arboles import *

#ej1 
tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
dic_codificacion = {'A':'10', '3':'11', '1':'000', 'T':'010', 'F':'011', '0':'0010', 'M':'0011'}
tabla = ordenar_tabla_por_probabilidad(tabla)
bosque = []
for elemento in tabla:
    nodo = ArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)
#probar a ver la tabla ordenada
for elemento in bosque:
    print(elemento.info, elemento.valor)
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = ArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque = ordenar_nodo_por_probabilidad(bosque)
generar_Huffman(bosque[0])