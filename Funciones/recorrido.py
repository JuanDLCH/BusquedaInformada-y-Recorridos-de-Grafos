from Funciones.Grafos.metodos import *

#Recorrido por amplitud
#Recibe por parametros el Grafo, el Origen y el Destino
def recorridoAmplitud(G, origen, destino):
    visitados = []
    cola = [] #La escencia del recorrido por amplitud es una cola
    recorrido = [] #Vamos a guardar cada nodo recorrido
    cola.append(origen)
    
    while cola:
        actual = cola.pop(0) #LIFO
        
        if actual not in visitados:
            recorrido.append(actual)
            if actual == destino:
                return recorrido
            visitados.append(actual)
        vecinos = obtenerVecinos(G, actual)
        for i in vecinos:
            if i not in visitados:
                cola.append(i)
    return 'Sin solucion'


#Recorrido en profundidad
#Recibe por parámetros el Grafo, Origen y Destino
def recorridoProfundidad(G, origen, destino):
    pila = [] #La escencia del recorrido en profundidad es la Pila
    visitados = []
    recorrido = []
    pila.append(origen)
    
    while pila:
        actual = pila.pop() #FIFO
        if actual not in visitados:
            recorrido.append(actual)
            if(actual == destino):
                return recorrido
            visitados.append(actual)
        vecinos = obtenerVecinos(G, actual)
        vecinos = vecinos[::-1] #Invierte la lista de vecinos, para obtener primero el izquierdo
        for i in vecinos:
            if i not in visitados:
                pila.append(i)
    return 'Sin solucion'
