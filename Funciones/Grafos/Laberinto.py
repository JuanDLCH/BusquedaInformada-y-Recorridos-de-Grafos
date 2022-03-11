import networkx as nx

def crearLaberinto():
    Lb = nx.Graph()
    #Crea los nodos con sus atributos (Heuristica (h))
    Lb.add_nodes_from([('30', {'h':12 }), ('31', {'h':11 }), ('32', {'h':8  }), ('33', {'h':9  }), ('34', {'h':4  }), ('35', {'h':1  }),
                       ('20', {'h':13 }), ('21', {'h':10 }), ('22', {'h':9  }), ('23', {'h':10 }), ('24', {'h':3  }), ('25', {'h':2  }),
                       ('40', {'h':9  }), ('41', {'h':8  }), ('42', {'h':7  }), ('43', {'h':6  }), ('44', {'h':5  }), ('45', {'h':0  }), 
                       ('10', {'h':16 }), ('11', {'h':13 }), ('12', {'h':12 }), ('13', {'h':11 }), ('14', {'h':12 }), ('15', {'h':3  }),
                       ('00', {'h':15 }), ('01', {'h':14 }), ('02', {'h':13 }), ('03', {'h':14 }), ('04', {'h':15 }), ('05', {'h':4  }) ])
    
    
    #Crea las conexiones entre los nodos con su respectivo peso
    #Para este caso el peso será igual para todos
    Lb.add_edge('40', '41', weight=1)
    Lb.add_edge('41', '42', weight=1)

    Lb.add_edge('42', '32', weight=1)
    Lb.add_edge('42', '43', weight=1)

    Lb.add_edge('32', '22', weight=1)
    Lb.add_edge('32', '33', weight=1)

    Lb.add_edge('22', '21', weight=1)
    Lb.add_edge('22', '23', weight=1)

    Lb.add_edge('21','31', weight=1)
    Lb.add_edge('31','30', weight=1)
    Lb.add_edge('30','20', weight=1)

    Lb.add_edge('23', '13', weight=1)

    Lb.add_edge('13', '12', weight=1)
    Lb.add_edge('13', '14', weight=1)

    Lb.add_edge('12', '11', weight=1)
    Lb.add_edge('12', '02', weight=1)

    Lb.add_edge('11', '01', weight=1)
    Lb.add_edge('01', '00', weight=1)
    Lb.add_edge('00', '10', weight=1)

    Lb.add_edge('02', '03', weight=1)
    Lb.add_edge('03', '04', weight=1)

    Lb.add_edge('43', '44', weight=1)
    Lb.add_edge('44', '34', weight=1)
    Lb.add_edge('34', '24', weight=1)
    Lb.add_edge('24', '25', weight=1)

    Lb.add_edge('25', '15', weight=1)
    Lb.add_edge('25', '35', weight=1)

    Lb.add_edge('15', '05', weight=1)
    Lb.add_edge('35', '45', weight=1)
    return Lb    