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
    <img alt="Ciudades" src="Imagenes\Ciudades.png" width="600" height="800" />
</p>

Puede que se dificulte el entendimiento del grafo a primera vista, pero básicamente tenemos que el viaje a cada ciudad tiene un coste distinto (Que podría relacionarse con combustible, distnacia, etc); la heurística en este caso la podemos interpretar como el costo que genera el uso de cada aeropuerto y, aunque no se ve en el grafo, ella está presente y la definimos así:
    
## Heurísticas:
- Medellín: 5
- Caracas: 4
- Dallas: 5
- Estanbul: 4
- Florianapolis: 3
- Guayaquil: 4
- Houston: 3
- Ixtapa: 2
- Jaco: 3
- Kansas city: 3
- Leticia: 4
- Mendoza: 2
- New Orleans: 0

<cite><u>Al ingresar los nombres en el algoritmo, se deben ingresar mayusculas y minusculas como está definido en esta lista, al igual que los espacios</u></cite>

Donde podemos decir que New Orleans puede ser la sede de la aerolinea dado que el costo que genera el aeropuerto de esta ciudad es minimo.

Así, teninendo en cuenta estas variables, es posible decir que el Algoritmo A* nos entrega el camino más óptimo, teniendo en cuenta tanto costes de aeropuesto como costes de combustibe, mientras que el algoritmo Primero el mejor, nos genera un recorrido más directo, que puede ser más caro en costes de aeropuertos pero usa menos combustible.

Podemos concluir entonces que el algoritmo A* es más equilibrado para estos casos, ya que tiene en cuenta ambas variables.
<br><br><br>

# Para crear los grafos:
- Trabajaremos en Python
- Importaremos las librerías de networkx y graphviz

# Instalación de librerías:
- pip install graphviz

# Dibujado de grafos:
- [http://mxwell.github.io](http://mxwell.github.io/draw-graph/?q=graph{Medellin--Bogota[label="3"];Medellin--Caracas[label="5"];Medellin--Dallas[label="2"];Bogota--Estanbul[label="3"];Bogota--Florianiapolis[label="2"];Bogota--Caracas[label="2"];Dallas--Guayaquil[label="5"];Dallas--Florianapolis[label="1"];Estanbul--Forianapolis[label="2"];Estanbul--Ixtapa[label="3"];Estanbul--Houston[label="4"];Florianapolis--Guayaquil[label="2"];Florianapolis--Jaco[label="5"];Florianapolis--Ixtapa[label="2"];Florianapolis--Houston[label="1"];Guayaquil--Jaco[label="2"];Guayaquil--Ixtapa[label="3"];Houston--Kansas_city[label="2"];Houston--Leticia[label="1"];Houston--Ixtapa[label="4"];Ixtapa--Jaco[label="3"];Ixtapa--Mendoza[label="1"];Ixtapa--Leticia[label="6"];Ixtapa--Kansas_city[label="2"];Kansas_city--New_Orleans[label="3"];Kansas_city--Leticia[label="4"];Leticia--New_Orleans[label="4"];Leticia--Mendoza[label="4"];Mendoza--New_Orleans[label="2"]}#)
