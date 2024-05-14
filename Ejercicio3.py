class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class NodoNario:
    def __init__(self, valor):
        self.valor = valor
        self.hijo = []

def cargar_indice_desde_archivo(archivo):
    indice = None
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            partes = linea.split()
            nivel = len(partes) - 1
            nodo = NodoNario(partes[nivel])
            if nivel == 0:
                indice = nodo
            else:
                padre = nodo_padre(indice, partes[:nivel])
                padre.hijo.append(nodo)
    return indice

def nodo_padre(raiz, ruta):
    nodo = raiz
    for valor in ruta:
        encontrado = False
        for hijo in nodo.hijo:
            if hijo.valor == valor:
                nodo = hijo
                encontrado = True
                break
        if not encontrado:
            nuevo_nodo = NodoNario(valor)
            nodo.hijo.append(nuevo_nodo)
            nodo = nuevo_nodo
    return nodo

def knuth_transform(raiz_nario):
    if not raiz_nario:
        return None
    raiz_binaria = NodoBinario(raiz_nario.valor)
    for hijo in raiz_nario.hijo:
        hijo_transformado = knuth_transform(hijo)
        if raiz_binaria.izquierda is None:
            raiz_binaria.izquierda = hijo_transformado
        else:
            ultimo = raiz_binaria.izquierda
            while ultimo.derecha:
                ultimo = ultimo.derecha
            ultimo.derecha = hijo_transformado
    return raiz_binaria

def listar_indice(raiz):
    if not raiz:
        return
    print(raiz.valor)
    listar_indice(raiz.izquierda)
    listar_indice(raiz.derecha)

def encontrar_subtitulo(raiz, subtitulo):
    if not raiz:
        return None
    if raiz.valor == subtitulo:
        return raiz
    encontrado_izquierda = encontrar_subtitulo(raiz.izquierda, subtitulo)
    if encontrado_izquierda:
        return encontrado_izquierda
    return encontrar_subtitulo(raiz.derecha, subtitulo)

def almacenar_pagina(raiz, pagina):
    if not raiz:
        return
    raiz.pagina = pagina
    almacenar_pagina(raiz.izquierda, pagina)
    almacenar_pagina(raiz.derecha, pagina)

def contar_capitulos(raiz):
    if not raiz:
        return 0
    return 1 + contar_capitulos(raiz.izquierda) + contar_capitulos(raiz.derecha)

def encontrar_temas_con_palabras(raiz, palabras):
    if not raiz:
        return []
    temas = []
    for palabra in palabras:
        if palabra.lower() in raiz.valor.lower():
            temas.append(raiz.valor)
            break
    temas += encontrar_temas_con_palabras(raiz.izquierda, palabras)
    temas += encontrar_temas_con_palabras(raiz.derecha, palabras)
    return temas

# Cargar el índice desde el archivo
raiz_nario = cargar_indice_desde_archivo("indice.txt")

# Transformar el árbol n-ario en un árbol binario no balanceado
raiz_binaria = knuth_transform(raiz_nario)

# Listar el índice en su orden original
print("Índice en su orden original:")
listar_indice(raiz_nario)

# Mostrar la parte del índice correspondiente al subtítulo "Diseño de software de tiempo real"
subtitulo = encontrar_subtitulo(raiz_binaria, "Diseño de software de tiempo real")
if subtitulo:
    print("\nParte del índice correspondiente al subtítulo 'Diseño de software de tiempo real':")
    listar_indice(subtitulo)
else:
    print("\nEl subtítulo 'Diseño de software de tiempo real' no se encuentra en el índice.")

# Almacenar la página asociada a cada tema
pagina = 1
almacenar_pagina(raiz_binaria, pagina)

# Determinar cuántos capítulos tiene
numero_capitulos = contar_capitulos(raiz_binaria)
print("\nNúmero de capítulos:", numero_capitulos)

# Determinar todos los temas que contengan las palabras "modelo" y "métrica"
temas_modelo_metrica = encontrar_temas_con_palabras(raiz_binaria, ["modelo", "métrica"])
if temas_modelo_metrica:
    print("\nTemas que contienen las palabras 'modelo' y 'métrica':")
    for tema in temas_modelo_metrica:
        print(tema)
else:
    print("\nNo se encontraron temas que contengan las palabras 'modelo' y 'métrica' en el índice.")
