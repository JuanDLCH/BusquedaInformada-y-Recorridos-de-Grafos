import networkx as nx

def crearCiudades():

    Lb = nx.Graph()
    #Crea los nodos con sus atributos (Heuristica (h))
    Lb.add_nodes_from([('Medellin', {'h':5 }), ('Bogota', {'h':5 }), ('Caracas', {'h':4  }), ('Dallas', {'h':5  }), ('Estanbul', {'h':4  }), ('Florianiapolis', {'h':3  }),
                       ('Guayaquil', {'h':4 }), ('Houston', {'h':3 }), ('Ixtapa', {'h':2  }), ('Jaco', {'h':3 }), ('Kansas city', {'h':3  }), ('Leticia', {'h':4  }),
                       ('Mendoza', {'h':2  }), ('New Orleans', {'h':0  })])
    
    
    #Crea las conexiones entre los nodos con su respectivo peso
    #Para desplazamiento vertical asignamos un peso de 2
    #Para desplazamiento horizontal asignamos un peso de 1
    #Estos desplazamientos hablando del laberinto como una imagen
    
    Lb.add_edge('Medellin', 'Bogota', weight=3)
    Lb.add_edge('Medellin', 'Caracas', weight=5)
    Lb.add_edge('Medellin', 'Dallas', weight=2)
    
    Lb.add_edge('Bogota', 'Estanbul', weight=3)
    Lb.add_edge('Bogota', 'Florianiapolis', weight=2)
    Lb.add_edge('Bogota', 'Caracas', weight=2)
    
    Lb.add_edge('Caracas', 'Dallas', weight=2)
    Lb.add_edge('Caracas', 'Guayaquil', weight=3)
    Lb.add_edge('Caracas', 'Florianiapolis', weight=4)
    Lb.add_edge('Caracas', 'Estanbul', weight=2)
    
    Lb.add_edge('Dallas', 'Guayaquil', weight=5)
    Lb.add_edge('Dallas', 'Florianiapolis', weight=1)
    
    Lb.add_edge('Estanbul', 'Florianiapolis', weight=2)
    Lb.add_edge('Estanbul', 'Ixtapa', weight=3)
    Lb.add_edge('Estanbul', 'Houston', weight=4)
    
    Lb.add_edge('Florianiapolis', 'Guayaquil', weight=2)
    Lb.add_edge('Florianiapolis', 'Jaco', weight=5)
    Lb.add_edge('Florianiapolis', 'Ixtapa', weight=2)
    Lb.add_edge('Florianiapolis', 'Houston', weight=1)
    
    Lb.add_edge('Guayaquil', 'Jaco', weight=2)
    Lb.add_edge('Guayaquil', 'Ixtapa', weight=3)
    
    Lb.add_edge('Houston', 'Kansas city', weight=2)
    Lb.add_edge('Houston', 'Leticia', weight=1)
    Lb.add_edge('Houston', 'Ixtapa', weight=4)
    
    Lb.add_edge('Ixtapa', 'Jaco', weight=3)
    Lb.add_edge('Ixtapa', 'Mendoza', weight=1)
    Lb.add_edge('Ixtapa', 'Leticia', weight=6)
    Lb.add_edge('Ixtapa', 'Kansas city', weight=2)
    
    Lb.add_edge('Jaco', 'Mendoza', weight=5)
    Lb.add_edge('Jaco', 'Leticia', weight=4)
    
    Lb.add_edge('Kansas city', 'New Orleans', weight=3)
    Lb.add_edge('Kansas city', 'Leticia', weight=2)
    
    Lb.add_edge('Leticia', 'New Orleans', weight=4)
    Lb.add_edge('Leticia', 'Mendoza', weight=4)
    
    Lb.add_edge('Mendoza', 'New Orleans', weight=2)
    
    return Lb  