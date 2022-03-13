from Funciones.Grafos.metodos import *

#Primero el mejor
#Recibe como parámetros el Grafo, el Origen y el Destino
#Usamos como base el algoritmo por profundidad.
#Por ende, en caso de eurísticas iguales empezamos por el vecino "Izquierdo"
def primeroMejor(G, origen, destino):
    pila = []
    visitados = []
    recorrido = []
    pila.append(origen)
    
    while pila:
        actual = pila.pop()
        if actual not in visitados:
            recorrido.append(actual)
            if actual == destino:
                return recorrido #En caso tal de encontrar el nodo destino, retorna los nodos recorridos hasta el momento
            visitados.append(actual)
        vecinos = obtenerVecinos(G, actual) #El metodo Obtener vecinos sólo nos retorna el valor de los vecinos, no sus atributos
        vecinosAux = [] #Usamos una lista auxiliar de diccionarios para poder asignarles las heurísticas 
        
        for neighbor in vecinos:
            if neighbor not in visitados:
                vecinosAux.append({'n': neighbor, 'h': G.nodes[neighbor]["h"]})
        
        #El propósito de ponerlos en una lista es usar la función lambda para ordenarlos por heurística en orden ascendente
        vecinosAux = sorted(vecinosAux, key = lambda i: i['h'])
        i=0
        vecinos = [] #La lista de vecinos no la necesitamos más, por lo que la vaciamos para reutilizarla
        
        for item in vecinosAux:
            if i == 0:
                minh = item['h'] #Como la lista está ordenada por heurística asumimos que el primero es el de más baja
                i+=1
                
            if item['h'] == minh:
                #Hacemos uso de la lista vecinos que vaciamos antes del ciclo
                #Le guardaremos los nodos con la menor heurística
                vecinos.append(item) #Igual debemos seguir recorriendo la lista para validar nodos con heurística igual a la menor
            else:
                break #Si enconramos un nodo con heurística mayor, no es necesario seguir recorriendo la lista, seguirán siendo mayores
        for i in vecinos:
            if i['n'] not in visitados:
                pila.append(i['n'])
        pila = pila[::-1]
    return 'Sin solucion'



#A* o A Star
#Recibe como parámetros el Grafo, el Origen y el Destino
#Usamos como base el algoritmo Primero el Mejor.
#Por ende, en caso de costes iguales empezamos por el vecino "Izquierdo"
def aStar(G, origen, destino):
    pila = []
    visitados = []
    recorrido = []
    pila.append(origen)
    costes = 0
    predecesores = {origen: 'N/A'} #Iremos guardando los nodos predecesores para al final hacer una regresión por el camino más óptimo
    
    while pila:
        actual = pila.pop()
        vecinos = obtenerVecinos(G, actual)
        vecinosAux = []
        if actual not in visitados:
            recorrido.append(actual)
            for neighbor in vecinos:
                if neighbor in visitados:
                    predecesores[actual] = neighbor #Si el vecino está en los visitados asumimos que este es el predecesor
            if actual == destino:
                print('Nodos recorridos' + str(recorrido)) #Imprimimos el recorrido
                return recorridoOptimo(predecesores) #Con base en los predecesores retornamos el recorrido óptimo
            visitados.append(actual)
        for neighbor in vecinos:
            if neighbor not in visitados:
                #El coste de ir de un nodo a otro se irá acumulando con los costes totales del recorrido
                vecinosAux.append({'n': neighbor, 't': G.nodes[neighbor]["h"] + G[actual][neighbor]["weight"]})
        vecinosAux = sorted(vecinosAux, key = lambda i: i['t']) #Ordenamos ahora por el coste total de ir de un nodo a otro + la heurística
        i=0
        vecinos = []
        
        for item in vecinosAux:
            if i == 0:
                minh = item['t'] 
                i+=1  
                
            #Le damos el mismo trato que en el algoritmo anterior, ya no con la heurística sino con el coste total
            if item['t'] == minh:
                vecinos.append({'n': item['n'], 't': item['t']})
            else:
                break
                
        for i in vecinos:
            if i['n'] not in visitados:
                pila.append(i['n'])
        pila = pila[::-1]
    return 'Sin solucion'
