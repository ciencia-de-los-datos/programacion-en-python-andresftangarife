"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4])
        
    return sum(v2)

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4])  

    lista = []
    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)

    v1_unique.sort()
    for i in v1_unique:
        lista.append((i, v1.count(i)))

    lista

    return lista


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4])

    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)
    
    data = [v1, v2, v3, v4, v5]
    lista = []
    v1_unique.sort()

    for letra in v1_unique:
        cuenta = 0
        tupla = ()
        for i in range(len(data[0])):
            if data[0][i] == letra:
                cuenta += data[1][i]
        tupla = (letra, cuenta)
        if tupla != ():
            lista.append(tupla)

    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    fechas = list(map(lambda x: x.split("-"), v3))
    meses = []
    for mes in range(len(fechas)):
        meses.append(fechas[mes][1])

    meses_unique = list(set(meses))

    lista = []
    meses_unique.sort()
    for i in meses_unique:
        lista.append((i, meses.count(i)))
    
    return lista


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 
    
    data = [v1, v2, v3, v4, v5]
    lista = []

    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)

    v1_unique.sort()

    for letra in v1_unique:
        x = letra
        x = []
        for i in range(len(data[0])):
            if data[0][i] == letra:
                x.append(data[1][i])
        tupla = (letra, max(x), min(x))
        if tupla != ():
            lista.append(tupla)

    return lista



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    lista_1 = []
    for i in range(0,len(v5)):
        lista_1.append(v5[i].strip("\n").split(","))


    lista_2 = []
    for sublista in lista_1:
        for j in sublista:
            lista_2.append(j)

    lista_l = []
    lista_n = []
    for i in lista_2:
        lista_l.append(i.split(":")[0])
        lista_n.append(int(i.split(":")[1]))

    claves_unique = list(set(lista_l))
    claves_unique.sort()

    lista = []
    for clave in claves_unique:
        x = []
        for i in range(len(lista_l)):
            if lista_l[i] == clave:
                x.append(lista_n[i])
        tupla = (clave, min(x), max(x))
        if tupla != ():
            lista.append(tupla)

    return lista


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)

    v2_unique = list(set(v2))
    v2_unique.sort()
    v2_unique

    resultado = []
    for index in v2_unique:
        lista = []
        for i in range(len(v2)):
            if v2[i] == index:
                lista.append(v1[i])
        resultado.append((index, lista))

    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)

    v2_unique = list(set(v2))
    v2_unique.sort()
    v2_unique

    resultado = []
    for index in v2_unique:
        lista = []
        for i in range(len(v2)):
            if v2[i] == index:
                lista.append(v1[i])
        lista_ord = list(set(lista))
        lista_ord.sort()
        resultado.append((index, lista_ord))
    
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    lista_1 = []
    for i in range(0,len(v5)):
        lista_1.append(v5[i].strip("\n").split(","))


    lista_2 = []
    for sublista in lista_1:
        for j in sublista:
            lista_2.append(j)

    lista_l = []
    lista_n = []
    for i in lista_2:
        lista_l.append(i.split(":")[0])
        lista_n.append(int(i.split(":")[1]))

    claves_unique = list(set(lista_l))
    claves_unique.sort()

    dicc = {}
    for clave in claves_unique:
        dicc[clave] = lista_l.count(clave)

    return dicc


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 

    l = []
    for i in range(len(v1)):
        t = (v1[i], len(v4[i].replace(",", "")), len(v5[i].split(",")))
        l.append(t)
    return l


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 
    
    nuevo_v4 = []
    for i in range(len(v4)):
        nuevo_v4.append(v4[i].split(","))

    v4_f, v2_ext = [], []
    for lista in range(len(nuevo_v4)):
        for i in range(len(nuevo_v4[lista])):
            v4_f.append(nuevo_v4[lista][i])
            v2_ext.append(v2[lista])

    v4_f_unique = list(set(v4_f))
    v4_f_unique.sort()

    lista = {}
    for letra in v4_f_unique:
        cuenta = 0
        for i in range(len(v4_f)):
            if v4_f[i] == letra:
                cuenta += v2_ext[i]
        lista[letra] = cuenta

    return lista


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos_prueba = open('data.csv', 'r')
    lineas = datos_prueba.readlines()
    v1, v2, v3, v4, v5 = [[],[],[],[],[]]
    for linea in lineas:
        data = linea.split("\t")
        v1.append(data[0])
        v2.append(int(data[1]))
        v3.append(data[2])
        v4.append(data[3])
        v5.append(data[4]) 
    
    lista = []
    v1_unique = []
    for i in v1:
        if i not in v1_unique:
            v1_unique.append(i)

    v1_unique.sort()

    lista_1 = []
    for i in range(0,len(v5)):
        lista_1.append(v5[i].strip("\n").split(","))

    lista_2, v1_ext = [], []
    for sublista in range(len(lista_1)):
        for j in lista_1[sublista]:
            lista_2.append(j)
            v1_ext.append(v1[sublista])

    lista_n = []
    for i in lista_2:
        lista_n.append(int(i.split(":")[1]))

    dicc_12 = {}
    for letra in v1_unique:
        cuenta = 0
        for i in range(len(v1_ext)):
            if v1_ext[i] == letra:
                cuenta += lista_n[i]
        dicc_12[letra] = cuenta

    return dicc_12
