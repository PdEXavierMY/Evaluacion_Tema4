from ejercicio_Huffman import *
from ejercicio_pokemon import *
from codigo_base.arboles import *
from codigo_base.grafos import *
from codigo_base.archivo import *
from random import choice, randint
from codigo_base.cola import Cola, arribo, atencion, cola_vacia
from introducir import solicitar_introducir_numero_extremo, solicitar_introducir_cadena
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
        pokemon_csv = [['Bulbasaur', 1, 'planta/veneno', 'fuego/psiquico'],
         ['Bulivysaur', 2, 'planta/veneno', 'fuego/psiquico'], 
         ['Charmander', 4, 'fuego', 'agua/tierra'],
         ['Charizard', 6, 'fuego/volador', 'agua/electrico'], 
         ['Squirtle', 7, 'agua', 'planta/electrico'], 
         ['Butterfree', 12, 'bicho/volador', 'fuego/electrico/hielo'], 
         ['Pidgeotto', 17, 'normal/volador', 'hielo/roca'], 
         ['Rattata', 19, 'normal', 'lucha'], 
         ['Weedle', 13, 'bicho/veneno', 'fuego/psiquico/volador'], 
         ['Pikachu', 25, 'electrico', 'tierra'], 
         ['Raichu', 26, 'electrico', 'tierra'], 
         ['Meowth', 52, 'normal', 'lucha'],
         ['Growlithe', 58, 'fuego', 'agua/roca'], 
         ['Tentacool', 72, 'agua/veneno', 'psiquico/electrico'], 
         ['Weepinbell', 70, 'planta/veneno', 'fuego/volador/hielo']] 
        arbol = None
        arbol_nombres = None
        arbol_tipo = None
        arbol_numero = None
        fichero = abrir('pokemon')
        for pokemon in pokemon_csv:
            x = Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3])
            guardar(fichero, x)

        #apartado a
        pos = 0
        while pos < len(pokemon_csv):
            poke = leer(fichero, pos)
            arbol = insertar_nodo(arbol, [poke.nombre, poke.numero, poke.tipo, poke.debilidad], pos)
            arbol_nombre = insertar_nodo(arbol_nombre, poke.nombre, pos)
            arbol_numero = insertar_nodo(arbol_numero, poke.numero, pos)
            arbol_tipo = insertar_nodo(arbol_tipo, poke.tipo, pos)
            pos += 1
        cerrar(fichero)

        #apartado b
        print('')
        nombre_pokemonabuscar = solicitar_introducir_cadena('Ingrese el nombre parcial o total del pokemon que quieres buscar')
        print('')
        busqueda_proximidad_pokemon(arbol_nombre, nombre_pokemonabuscar)
        print('')

        #apartado c
        file = abrir('pokemon')
        print('Pokemone de tipo agua, fuego, planta o electrico:')
        print('')
        inorden_tipo(arbol_nombre, file)
        print('')

        #apartado d
        print('Barrido pokemon por nombre:')
        print('')
        inorden_pokemon_nombre(arbol_nombre, file)
        print('')
        print('Barrido pokemon por numero:')
        print('')
        inorden_pokemon_numero(arbol_numero, file)
        print('')
        print('Barrido pokemon por nivel:')
        print('')
        por_nivel(arbol_nombre)
        print('')

        #apartado e
        debilidad = input('Ingrese tipo de debilidad: ')
        print('')
        inorden_debilidad(arbol_nombre, file, debilidad)
        print('')
        cerrar(file)

        '''#apartado f
        contador = 0
        print('Listado de pokemon y su tipo:')
        print('')
        contador = inorden_tipo(arbol_nombres, contador)
        print('')
        print('Cantidad del tipo fuego:',contador)'''

    elif ej == 3:
        g = Grafo(dirigido=False)
        # las maravillas naturales
        g.insertar_vertice('T', datos={'tipo': 'a', 'pais': 'egipto'})
        g.insertar_vertice('Z', datos={'tipo': 'a', 'pais': 'francia'})
        g.insertar_vertice('F', datos={'tipo': 'a', 'pais': 'china'})
        g.insertar_vertice('X', datos={'tipo': 'a', 'pais': 'india'})
        g.insertar_vertice('R', datos={'tipo': 'a', 'pais': 'eeuu'})
        g.insertar_vertice('K', datos={'tipo': 'a', 'pais': 'brasil'})
        # las maravillas arquitectonicas
        g.insertar_vertice('L', datos={'tipo': 'n', 'pais': 'argentina-brasil-paragauy'})
        g.insertar_vertice('J', datos={'tipo': 'n', 'pais': 'indonesia'})
        g.insertar_vertice('I', datos={'tipo': 'n', 'pais': 'sudafrica'})
        g.insertar_vertice('M', datos={'tipo': 'n', 'pais': 'india'})
        g.insertar_vertice('S', datos={'tipo': 'n', 'pais': 'china'})
        g.insertar_vertice('Y', datos={'tipo': 'n', 'pais': 'brasil'})

        g.insertar_arista('L', 'J', 6)
        g.insertar_arista('L', 'I', 3)
        g.insertar_arista('I', 'M', 8)
        g.insertar_arista('M', 'S', 2)
        g.insertar_arista('M', 'Y', 2)
        g.insertar_arista('Y', 'I', 9)
        g.insertar_arista('T', 'X', 6)
        g.insertar_arista('T', 'F', 3)
        g.insertar_arista('T', 'R', 8)
        g.insertar_arista('F', 'X', 2)
        g.insertar_arista('F', 'R', 2)
        g.insertar_arista('X', 'Z', 9)
        g.insertar_arista('R', 'Z', 4)
        g.insertar_arista('K', 'Z', 3)
        g.insertar_arista('R', 'X', 5)


        paises = g.contar_maravillas()
        print('Los paises con una maravilla y su tipo son los siguientes:')
        print('')
        for pais in paises:
            print(pais, paises[pais])

        arbol_min = g.kruskal()
        arbol_min = arbol_min[0].split('-')
        peso_total = 0
        print('')
        print('El arbol minimo es el siguiente:')
        print('')
        for nodo in arbol_min:
            nodo = nodo.split(';')
            peso_total += int(nodo[2])
            print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
        print('')
        print(f"El peso total del recorrido es {peso_total}")
        print('')
        print('Vamos a probar a encontrar un camino de T a Z.')
        print('')
        if g.existe_paso('T', 'Z'):
            resultados1 = g.dijkstra('T')
            camino = g.camino(resultados1, 'T', 'Z')
            print(camino)
        else:
            print('no se puede llega de T a Z')
            g.eliminar_arista('A', 'C')
            g.eliminar_vertice('C')