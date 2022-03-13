import matplotlib.pyplot as plt

#Definimos algunos métodos generales

#Obtiene los vecinos de un nodo determinado y los retorna a modo de lista
#El G[n] retorna los vecinos empezando por la derecha
def obtenerVecinos(G, n):
    vecinos = G[n]
    lista = []
    for k, d in vecinos.items():
        lista.append(str(k))    
    return lista

    
# {'A': 'N/A', 'D': 'A', 'F': 'D', 'I': 'F', 'H': 'I', 'M': 'I', 'L': 'M', 'N': 'M'}
# Regresa desde el nodo final por cada predecesor para encontrar el camino óptimo a recorrer
def recorridoOptimo(predecesores):
    lista = list()
    p = list(predecesores.keys())[-1]
    lista.append(p)
    while p != 'N/A':
        lista.append(predecesores[p])
        p = predecesores[p]
    lista.remove('N/A')
    return lista[::-1]
    