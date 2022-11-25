from ejercicio_Huffman import *
from ejercicio_pokemon import *
from codigo_base.arboles import *
from random import choice
from codigo_base.cola import Cola, arribo, atencion, cola_vacia
from introducir import solicitar_introducir_numero_extremo
import csv

def ejecutar():
    #ej1
    ej = solicitar_introducir_numero_extremo("Elige que ejercicio quieres ejecutar", 1, 3)
    if ej == 1:
        tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
        dic_codificacion = {'A':'00', '3':'01', '1':'100', 'T':'110', 'F':'111', '0':'1010', 'M':'1011'}

        tabla = ordenar_tabla_por_probabilidad(tabla)
        bosque = []
        for elemento in tabla:
            nodo = ArbolHuffman(elemento[0], elemento[1])
            bosque.append(nodo)
        #probar a ver la tabla ordenada
        print("")
        print("Tabla ordenada:")
        print("")
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
        print("")
        print("Tabla para decodificar:")
        print("")
        generar_Huffman(bosque[0])
        print("")
        print("A continuación se muestra un ejemplo con el funcionamiento del árbol de Huffman:")
        cadena = "MT1AT003FAT0113MATF3010"
        print("Cadena original: ", cadena)
        codificado = codificar(cadena, dic_codificacion)
        print("Cadena codificada: ", codificado)
        print("Decodificando...")
        print("Cadena decodificada: ", decodificar(codificado, bosque[0]))
        print("Ahora, ¿quieres probar a decodificar una cadena que no sea la original?")
        print("Introduce la cadena que quieras decodificar:")
        cadena = str(input())
        for element in cadena.split():
            if element != '0' and element != '1':
                print("La cadena no es válida, debe ser binaria")
                break
        print("Decodificando...")
        print("Cadena decodificada: ", decodificar(cadena, bosque[0]))
    #ej2   
    elif ej == 2:
        with open("Pokemon.csv", 'r') as f:
            reader = csv.reader(f)
            nombre = [row[1] for row in reader]
        tipo = ['agua', 'fuego', 'tierra', 'electrico', 'acero', 'hada', 'fantasma', 'volador', 'dragon', 'veneno', 'bicho', 'planta', 'roca', 'normal', 'lucha', 'psiquico', 'siniestro', 'hielo']
        pokemondebil = ['Jolteon', 'Lycanroc', 'Tyrantum']+[choice(nombre) for i in range(100)]
        debil = ['agua', 'fuego', 'tierra', 'electrico', 'acero', 'hada', 'fantasma', 'volador', 'dragon', 'veneno', 'bicho', 'planta', 'roca', 'normal', 'lucha', 'psiquico', 'siniestro', 'hielo']+pokemondebil
        id = [i+1 for i in range(1, len(nombre))]
        arbol_nombres = None
        arbol_tipo = None
        arbol_numero = None
        #apartado a
        for i in range (0, len(nombre)):
            pokemon = Pokemon(nombre[i], id[i], choice(tipo), choice(debil))
            arbol_nombres = insertar_nodo_pokemon(arbol_nombres, [pokemon, pokemon.nombre])
            arbol_tipo = insertar_nodo_pokemon(arbol_tipo, [pokemon, pokemon.tipo])
            arbol_numero = insertar_nodo_pokemon(arbol_numero, [pokemon, pokemon.numero])
ejecutar()