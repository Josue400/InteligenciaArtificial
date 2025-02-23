Ejercicio 1


-Clase SemaforoInteligente:

 Esta clase mantiene el estado actual del semáforo, utlizamos la funcion detectar_vehiculos() para simular la cantidad de vehículos en espera y luego la funcion cambiar_estado() la cual maneja la logica de transicion entre los colores.
para esto utilizamos 

-Duración de tiempos:
  El rojo tiene un tiempo fijo de 4 segundos el cual lo declaramos aca "time.sleep(4)".
  El verde varía entre 4 y 10 segundos según el tráfico detectado, el cual lo definimos de la siguiente forma para que oscile entre los 4 y 10 segundos duracion_verde = max(4, min(10, vehiculos))
  El amarillo siempre dura 2 segundos, por lo que lo definimos como en el rojo  time.sleep(2)


Ejercicio 2

AgenteBuscadorDeObjetos:

Se crea una cuadrícula de 5x5 llena de puntos ( " . " ) en la cual al agente inicia en la posicion (0,0).
Para el Objeto,  coloca el objeto en una posicion aleatoria. luego el agegente de posicion en posicion va despazandose, lo cual funciona de la siguiente manera

1. En cada iteración, el agente se mueve un paso hacia el objeto.
2. La posición anterior se borra (" . "), y la nueva se marca (" A ").
3. Se muestra la cuadrícula en cada movimiento.
4.Finalización:

El ciclo se detiene cuando el agente encuentra el objeto y cuando lo encuentrra manda a imprimir  "¡Objeto encontrado!".


Ejercicio 3.

SistemasExpertoParaDiagnosticoSimple

Este ejercicio consta de algunas reglas con las que debe de cumplir, primero tenemos un diccionario de posibles sintomas y a que enfermedad se le atribuyen

Definición de reglas de diagnóstico:

Se analizan síntomas comunes como fiebre, tos y dolor de cabeza.
Se establecen condiciones para diagnosticar posibles enfermedades.


Interacción con el usuario:

El usuario ingresa síntomas separados por comas.
Se estandariza la entrada (eliminando espacios y pasando a minúsculas) para poder comparar.

Salida del sistema:

Se imprime un diagnóstico basado en los síntomas ingresados.
Si no hay coincidencias, se recomienda consultar a un especialista.



Ejercicio 4

RecomendacionDePeliculas

Para realizar este se crea un diccionario peliculas, donde las claves son los géneros y los valores son listas de películas pertenecientes a cada género el cual esta establecido en las primera parte del codigo.

Se ejecuta el codigo y solicitamos al usuario que ingrese cual es su genero favorito para que entre a nuestra funcion recomendar_pelicula(genero), 
esta función recibe el género ingresado por el usuario y busca una película en el diccionario.
Se imprime la película recomendada.
Si hay un error, se captura y se muestra un mensaje de error.
