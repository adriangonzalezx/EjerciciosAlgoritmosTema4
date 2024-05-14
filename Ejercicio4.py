class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def hijo_izquierdo(nodo):
    if nodo:
        return nodo.izquierda
    else:
        return None

def hijo_derecho(nodo):
    if nodo:
        return nodo.derecha
    else:
        return None

# Ejemplo de uso
nodo_raiz = NodoBinario(1)
nodo_izquierdo = NodoBinario(2)
nodo_derecho = NodoBinario(3)

nodo_raiz.izquierda = nodo_izquierdo
nodo_raiz.derecha = nodo_derecho

print("Hijo izquierdo de la raíz:", hijo_izquierdo(nodo_raiz).valor)
print("Hijo derecho de la raíz:", hijo_derecho(nodo_raiz).valor)

