from Funciones.Grafos.Laberinto import *
from Funciones.Grafos.Ciudades import *
from Funciones.busquedaInformada import *
from Funciones.recorrido import *

Lb =  crearLaberinto()
Ciud = crearCiudades()



print('\n***************************************************************\n')

print("\tRESULTADOS PARA EL LABERINTO")

print('\n***************************************************************\n')

inicio = input("Inserte el punto de partida en el Laberinto: ")
destino = input("Inserte el punto de destino en el Laberinto: ")
print()

print('Recorrido del grafo por amplitud: ')
print(recorridoAmplitud(Lb, inicio, destino))
print()
print("\n******************************************************************\n")

print('Recorrido del grafo en profundidad: ')
print(recorridoProfundidad(Lb, inicio, destino))
print()
print("******************************************************************\n")

print('Búsqueda de camino más directo con Primero el Mejor: ')
print(primeroMejor(Lb, inicio, destino))
print()
print("******************************************************************\n")

print('Búsqueda del camino más óptimo con A*:')
print('Recorrido óptimo: ' + str(aStar(Lb, inicio, destino)))
print()
print("******************************************************************\n")

print('\n***************************************************************\n')

print("\tRESULTADOS PARA LAS CIUDADES")

print('\n***************************************************************\n')

inicio = input("Inserte el aeropuerto de partida: ")
destino = input("Inserte el aeropuerto de destino: ")

Pb = crearCiudades()
print('Recorrido en el grafo por amplitud: ')
print(recorridoAmplitud(Pb, inicio, destino))
print()
print("\n****************************************************************\n")
print('Recorrido en el grafo en profundidad: ')
print(recorridoProfundidad(Pb, inicio, destino))
print()
print("\n*****************************************************************\n")

print('Camino más directo con Primero el Mejor: ')
print(primeroMejor(Pb, inicio, destino))
print()
print("******************************************************************\n")

print('Camino más óptimo con A*:')
print('Recorrido óptimo: ' + str(aStar(Pb, inicio, destino)))
