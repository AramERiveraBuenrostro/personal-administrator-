tareas = []

# Funciones del programa 
def agregar_tarea(lista):
    # Entrada de tarea
    tarea = input("Escribe la tarea que deseas agregar: ")
    
    # Añadir la tarea al final de la lista
    lista.append(tarea)
 
    # Informe de tarea añadida 
    print("\nLa tarea ya se añadió a la lista de pendientes:\n")
    
    # Imprime la tarea añadida 
    print(f"La tarea añadida es: {tarea}")
    
    # Informa el número de tarea  
    print(f"La tarea se añadió en la posición {len(lista)}\n")

def ver_tareas(lista):
    # Condicional que evalúa si algo está en la lista
    # Si hay algo en la lista se presenta
    if lista:
        print("\n**** ---- Lista de Tareas ---- ****")
        for indice, tarea in enumerate(lista, 1):
            print(f"{indice}. {tarea}")
    # Si la lista está vacía avisa de ello
    else:
        print("No hay pendientes")
    # Mensaje de fin de listado
    print("--- FIN DEL LISTADO DE TAREAS ---")

def tarea_completada(lista):
    # Llamamos a la función ver_tareas()
    ver_tareas(lista)
    # Entrada para que el usuario introduzca una tarea 
    try:
        completada = int(input("Introduzca el número de la tarea a marcar como completada: "))
        # Condicional para marcar tareas completadas
        if 0 < completada <= len(lista):
            # Condicional para evaluar si la tarea ya estaba completada 
            # Si la tarea ya está completada
            if "(Completada)" in lista[completada - 1]:
                print("La tarea ya está completada.")
            # En cambio, si no está...
            else:
                lista[completada - 1] = "(Completada) " + lista[completada - 1]
                print("Se marcó la tarea como completada.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Por favor, introduce un número válido.")

def eliminar_tarea(lista):
    # Si la lista contiene algo 
    if lista:
        # Llamamos a la función ver_tareas()
        ver_tareas(lista)
        # Entrada para que el usuario introduzca la tarea
        try:
            tarea = int(input("Introduzca el número de la tarea a eliminar: "))
            # Opción inválida si la tarea no está en el rango de la lista
            if 0 < tarea <= len(lista):
                tarea_eliminada = lista.pop(tarea - 1)
                print(f"Se eliminó la tarea: {tarea_eliminada}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    # Si la lista está vacía se avisa de ello 
    else:
        print("No hay tareas.")
