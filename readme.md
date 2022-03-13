# <p align = center>Implementación de algoritmos de búsqueda</p>
## Aplicaciones: Resolución de laberintos y Escalas de Aeropuertos

- Juan Diego Londoño Chavarría
- Mario Alejandro Saldarriaga Álvarez

<br>

# Vamos a realizar la aplicación de 4 Algoritmos; 2 de búsqueda y 2 de recorrido
- Los algoritmos de búsqueda se encargarán de buscar, uno de ellos el camino más directo, el otro encontrará el camino más óptimo
    - Primero el mejor
    - A* <br>
    <br>

- Los algoritmos de recorrido unicamente recorrerán el grafo para encontrar el nodo que buscamos
    - Amplitud
    - Profundidad <br>
    <br>

# Aplicaciones:

## Laberinto
- En primer lugar le daremos solución a un Laberinto Sencillo, tomado de un <a href="https://repository.uaeh.edu.mx/revistas/index.php/huejutla/article/view/1089/4757">articulo </a> de la UAEH de México donde nos brindan una imagen del laberinto y un grafo con los nodos necesarios a recorrer como guía. La desventaja de esto es que su aplicación se limita al algoritmo "Primero el mejor" ya que los pesos para cada conexión serán iguales, haciendo que el recorrido A* y el recorrido Primero el mejor para este caso serán el mismo. <br><br> 
Cabe aclarar que este no es un grafo dirigido, si queremos ir del nodo 2,0 al nodo 4,3 podemos hacerlo sin problemas, por lo que, nuestro algoritmo puede dar solución no sólo a este caso particular, sino a cualquier laberinto. <br><br>



<br>

## <p align = center>Visualizacion:</p>
<p align="center">
    <img alt="Laberinto" src="Imagenes\Laberinto.png" width="800" height="400" />
</p>

<br><br><br>

## Aeropuertos
- En segundo lugar crearemos un grafo con costes de recorrido entre nodos, a estos mismos les asignaremos nombres de distintas ciudades, cada una simbolizando un aeropuerto distinto, con esto buscaremos el camino más barato para transportarse en avión desde una ciudad a otra, puesto que para una aerolínea suele ser más barato hacer escalas que un vuelo directo.

<br>

## <p align = "center">Visualizacion:</p>

<p align="center">
    <img alt="Ciudades" src="Imagenes\Ciudades.png" width="400" height="600" />
</p>

<br><br><br>

# Para crear los grafos:
- Trabajaremos en Python
- Importaremos las librerías de networkx y graphviz

# Instalación de librerías:
- pip install graphviz
- conda install -c alubbock pygraphviz
