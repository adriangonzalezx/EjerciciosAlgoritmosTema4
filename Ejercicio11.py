class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos(arbol):
    if arbol is None:
        return 0
    contador = 1
    for hijo in arbol.hijos:
        contador += contar_nodos(hijo)
    return contador

def contar_hojas(arbol):
    if arbol is None:
        return 0
    if len(arbol.hijos) == 0:
        return 1
    contador = 0
    for hijo in arbol.hijos:
        contador += contar_hojas(hijo)
    return contador

def mostrar_hojas(arbol):
    if arbol is None:
        return
    if len(arbol.hijos) == 0:
        print(arbol.valor)
    for hijo in arbol.hijos:
        mostrar_hojas(hijo)

def encontrar_padre(arbol, valor_nodo):
    if arbol is None:
        return None
    if arbol.valor == valor_nodo:
        return None
    for hijo in arbol.hijos:
        if hijo.valor == valor_nodo:
            return arbol.valor
        padre = encontrar_padre(hijo, valor_nodo)
        if padre is not None:
            return padre
    return None

def encontrar_altura(arbol):
    if arbol is None:
        return 0
    if len(arbol.hijos) == 0:
        return 1
    altura_maxima = 0
    for hijo in arbol.hijos:
        altura = encontrar_altura(hijo)
        if altura > altura_maxima:
            altura_maxima = altura
    return altura_maxima + 1

# Ejemplo de uso
arbol = Nodo(1)
arbol.hijos.append(Nodo(2))
arbol.hijos.append(Nodo(3))
arbol.hijos[0].hijos.append(Nodo(4))
arbol.hijos[0].hijos.append(Nodo(5))
arbol.hijos[1].hijos.append(Nodo(6))

print("Número de nodos:", contar_nodos(arbol))
print("Número de hojas:", contar_hojas(arbol))
print("Nodos hojas:")
mostrar_hojas(arbol)
print("Padre de 6:", encontrar_padre(arbol, 6))
print("Altura del árbol:", encontrar_altura(arbol))
