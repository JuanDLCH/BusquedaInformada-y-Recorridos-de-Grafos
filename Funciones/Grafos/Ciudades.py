import networkx as nx

def crearCiudades():

    Lb = nx.Graph()
    #Crea los nodos con sus atributos (Heuristica (h))
    Lb.add_nodes_from([('A', {'h':5 }), ('B', {'h':5 }), ('C', {'h':4  }), ('D', {'h':5  }), ('E', {'h':4  }), ('F', {'h':3  }),
                       ('G', {'h':4 }), ('H', {'h':3 }), ('I', {'h':2  }), ('J', {'h':3 }), ('K', {'h':3  }), ('L', {'h':4  }),
                       ('M', {'h':2  }), ('N', {'h':0  })])
    
    
    #Crea las conexiones entre los nodos con su respectivo peso
    #Para desplazamiento vertical asignamos un peso de 2
    #Para desplazamiento horizontal asignamos un peso de 1
    #Estos desplazamientos hablando del laberinto como una imagen
    
    Lb.add_edge('A', 'B', weight=3)
    Lb.add_edge('A', 'C', weight=5)
    Lb.add_edge('A', 'D', weight=2)
    
    Lb.add_edge('B', 'E', weight=3)
    Lb.add_edge('B', 'F', weight=2)
    Lb.add_edge('B', 'C', weight=2)
    
    Lb.add_edge('C', 'D', weight=2)
    Lb.add_edge('C', 'G', weight=3)
    Lb.add_edge('C', 'F', weight=4)
    Lb.add_edge('C', 'E', weight=2)
    
    Lb.add_edge('D', 'G', weight=5)
    Lb.add_edge('D', 'F', weight=1)
    
    Lb.add_edge('E', 'F', weight=2)
    Lb.add_edge('E', 'I', weight=3)
    Lb.add_edge('E', 'H', weight=4)
    
    Lb.add_edge('F', 'G', weight=2)
    Lb.add_edge('F', 'J', weight=5)
    Lb.add_edge('F', 'I', weight=2)
    Lb.add_edge('F', 'H', weight=1)
    
    Lb.add_edge('G', 'J', weight=2)
    Lb.add_edge('G', 'I', weight=3)
    
    Lb.add_edge('H', 'K', weight=2)
    Lb.add_edge('H', 'L', weight=1)
    Lb.add_edge('H', 'I', weight=4)
    
    Lb.add_edge('I', 'J', weight=3)
    Lb.add_edge('I', 'M', weight=1)
    Lb.add_edge('I', 'L', weight=6)
    Lb.add_edge('I', 'K', weight=2)
    
    Lb.add_edge('J', 'M', weight=5)
    Lb.add_edge('J', 'L', weight=4)
    
    Lb.add_edge('K', 'N', weight=3)
    Lb.add_edge('K', 'L', weight=2)
    
    Lb.add_edge('L', 'N', weight=4)
    Lb.add_edge('L', 'M', weight=4)
    
    Lb.add_edge('M', 'N', weight=2)
    
    return Lb  