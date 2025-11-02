'''
Implementa una función llamada ingresar_calificaciones() que permita al usuario introducir el nombre de una materia y su calificación correspondiente. 
Esta funcion es la que tomara las materias y calificaciones que quiera el usuario
Solicitar al usuario que ingrese el nombre de la materia
Solicitar la calificación (validando que sea un número entre 0 y 10)
Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
Preguntar si desea continuar ingresando más materias
Retornar ambas listas cuando el usuario decida terminar

Crea una función calcular_promedio(calificaciones) que reciba una lista de calificaciones y devuelva el promedio de todas ellas.
Desarrolla una función determinar_estado(calificaciones, umbral) que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.
Implementa una función encontrar_extremos(calificaciones) que identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.
En la función principal (main), llama a la función ingresar_calificaciones() para obtener los datos del usuario.
Utiliza las funciones creadas para calcular el promedio general, determinar materias aprobadas/reprobadas y encontrar las materias con calificaciones extremas.
Muestra un resumen final que incluya:
Todas las materias con sus calificaciones
El promedio general
Las materias aprobadas y reprobadas
La materia con mejor calificación y su valor
La materia con peor calificación y su valor
Asegúrate de manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.
Finaliza el programa con un mensaje de despedida e implementa la estructura if __name__ == "__main__": para ejecutar la función principal.
'''
        
def ingresar_calificaciones():
        
    #Inicializacion
    #Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
    lista_materias = []
    lista_calificaciones = []
    LIMITE_INFERIOR = 0
    LIMITE_SUPERIOR = 10

    while True:
        #Solicitar al usuario que ingrese el nombre de la materia

        while True:
            materia = input("Nombre de la materia: ").strip().lower()
               
            if not materia:
                # Si está vacío, imprime error y el bucle interno vuelve a pedir la materia
                print("El nombre de la materia no puede estar vacío. Inténtalo de nuevo.")
            else:
                # Si no está vacío, sale del bucle interno de validación
                lista_materias.append(materia)
                break
           
        while True:
            #Solicitar la calificación 
            calificacion_cadena = input(f"Calificación para {materia}, por favor valor entre 0 y 10: ")
            #(validando que sea un número entre 0 y 10)
            try:
                calificacion = float(calificacion_cadena)
              
                if  LIMITE_INFERIOR <= calificacion <= LIMITE_SUPERIOR:
                    lista_calificaciones.append(calificacion)
                    break #Fuera del buble de calificaciones
                else:
                    print ("La calificacion debe ser un numero entre 0 y 10, ambos incluidos")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
        contestacion = input("Desea introducir otra materia N o n para finalizar: ").strip().lower()
        #Fin interrumpe while, el mas externo
        if contestacion == 'n':
            print("Registro de calificaciones finalizado.")
            #break #Fin de los dos bucles
            #Retornar ambas listas cuando el usuario decida terminar
            return lista_materias, lista_calificaciones
        

#Crea una función calcular_promedio(calificaciones) que reciba una lista de calificaciones y devuelva el promedio de todas ellas.
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones) 
    return promedio
        

#Desarrolla una función determinar_estado(calificaciones, umbral) que reciba la lista 
#de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: 
# una con los índices de las materias aprobadas y otra con los índices de las reprobadas.
def determinar_estado (calificaciones, umbral):
    lista_reprobadas = []
    lista_aprobadas = []
    if not umbral:
        umbral=5.0
    for i in range (len(calificaciones)):
            if calificaciones[i]<umbral:
                lista_reprobadas.append(i)
            else:
                lista_aprobadas.append(i)
    return lista_aprobadas, lista_reprobadas
    
#Implementa una función encontrar_extremos(calificaciones) que identifique 
# el índice de la calificación más alta y el índice de la más baja en la lista de 
# calificaciones.
def encontrar_extremos (calificaciones):
    valor_maximo = max(calificaciones)
    califiacion_alta = calificaciones.index(valor_maximo)
    valor_minimo = min(calificaciones)
    calificacion_baja = calificaciones.index(valor_minimo)
    return califiacion_alta, calificacion_baja

def main():
    UMBRAL = 5.0
    materias, calificaciones= ingresar_calificaciones()
    if not materias:
        print("No se ingresaron materias. Programa terminado.")
        return
    promedio = calcular_promedio(calificaciones)
    maximo, minimo = encontrar_extremos(calificaciones)
    aprobadas, reprobadas= determinar_estado(calificaciones,UMBRAL)

    #Resumen
    #Todas las materias con sus calificaciones
    print("Resumen asignaturas y calificaciones")
    for i in range(len(materias)):
        materia = materias[i]
        calificacion = calificaciones[i]
        print(f"{materia} - {calificacion}")
    #El promedio general
    print(f"La nota promedio es {promedio}")
    #Las materias aprobadas y reprobadas
    print("Las asignaturas aprobadas")
    for i in aprobadas:
        print(f"{materias[i]}")
    print("Las asignaturas reprobadas")
    for i in reprobadas:
        print(f"{materias[i]}")
    #La materia con mejor calificación y su valor
    print(f"La asignatura con mejor calificacion {materias[maximo]} - {calificaciones[maximo]}")
    #La materia con peor calificación y su valor
    print(f"La asignatura con peor calificacion {materias[minimo]} - {calificaciones[minimo]}")
    #Finaliza el programa con un mensaje de despedida
    print(f"Ha sido un placer, programa terminado")

if __name__ == "__main__": main()