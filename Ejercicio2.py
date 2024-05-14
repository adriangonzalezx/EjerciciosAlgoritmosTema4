class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def cargar_expresion_arbol(expresion):
    partes = expresion.split()
    pila = []
    raiz = None

    for parte in partes:
        if parte.isdigit():
            nodo = Nodo(int(parte))
        else:
            nodo = Nodo(parte)
        
        if len(pila) == 0:
            raiz = nodo
        else:
            padre = pila[-1]
            if padre.izquierda is None:
                padre.izquierda = nodo
            else:
                padre.derecha = nodo
                pila.pop()
        if parte in ['+', '-', '*', '/']:
            pila.append(nodo)
    
    return raiz

def barrido_preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        barrido_preorden(nodo.izquierda)
        barrido_preorden(nodo.derecha)

def barrido_inorden(nodo):
    if nodo:
        barrido_inorden(nodo.izquierda)
        print(nodo.valor, end=' ')
        barrido_inorden(nodo.derecha)

def barrido_postorden(nodo):
    if nodo:
        barrido_postorden(nodo.izquierda)
        barrido_postorden(nodo.derecha)
        print(nodo.valor, end=' ')

def resolver_expresion(nodo):
    if nodo.valor.isdigit():
        return int(nodo.valor)
    else:
        izquierda = resolver_expresion(nodo.izquierda)
        derecha = resolver_expresion(nodo.derecha)
        operador = nodo.valor
        if operador == '+':
            return izquierda + derecha
        elif operador == '-':
            return izquierda - derecha
        elif operador == '*':
            return izquierda * derecha
        elif operador == '/':
            return izquierda / derecha

# Expresión matemática de ejemplo
expresion = "5 + 3 * 2"

# Cargar la expresión en un árbol binario
arbol = cargar_expresion_arbol(expresion)

# Mostrar la expresión en diferentes órdenes
print("Expresión en orden preorden:")
barrido_preorden(arbol)
print("\nExpresión en orden inorden:")
barrido_inorden(arbol)
print("\nExpresión en orden postorden:")
barrido_postorden(arbol)

# Resolver la expresión matemática y mostrar el resultado
resultado = resolver_expresion(arbol)
print("\nResultado de la expresión:", resultado)

