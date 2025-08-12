import os

# Nombre del archivo donde se guardarán las tareas
archivo = "tareas.txt"

# Función para agregar una nueva tarea
def agregar_tarea():
    print("Ingresa el nombre de la nueva tarea:")
    tarea = input()
    # Agregamos la tarea con estado Pendiente al archivo usando os.system
    os.system(f'echo Pendiente - {tarea} >> {archivo}')
    print("✅ Tarea agregada.\n")

# Función para ver las tareas almacenadas
def ver_tareas():
    print("\n📋 Lista de tareas:")
    # Mostramos el contenido del archivo (usa 'type' para Windows)
    os.system(f"type {archivo}")
    print("")

# Función para marcar una tarea como completada
def completar_tarea():
    # Leemos las tareas en una lista
    archivo_lectura = open(archivo, "r")
    lineas = archivo_lectura.readlines()
    archivo_lectura.close()

    if len(lineas) == 0:
        print("No hay tareas para completar.\n")
        return

    # Mostramos las tareas con número
    print("Tareas disponibles:")
    for i in range(len(lineas)):
        print(f"{i + 1}. {lineas[i].strip()}")

    print("Escribe el número de la tarea que completaste:")
    opcion = input()
    indice = int(opcion) - 1

    if indice < 0 or indice >= len(lineas):
        print("❌ Número inválido.\n")
        return

    # Reemplazamos "Pendiente" por "Completada" solo en esa línea
    if "Pendiente - " in lineas[indice]:
        lineas[indice] = lineas[indice].replace("Pendiente - ", "Completada - ")
    else:
        print("La tarea ya está completada.\n")
        return

    # Sobrescribimos el archivo con los cambios
    archivo_escritura = open(archivo, "w")
    archivo_escritura.writelines(lineas)
    archivo_escritura.close()
    print("✅ Tarea marcada como completada.\n")

# Función para eliminar una tarea
def eliminar_tarea():
    # Leemos todas las líneas
    archivo_lectura = open(archivo, "r")
    lineas = archivo_lectura.readlines()
    archivo_lectura.close()

    if len(lineas) == 0:
        print("No hay tareas para eliminar.\n")
        return

    # Mostramos las tareas
    print("Tareas disponibles:")
    for i in range(len(lineas)):
        print(f"{i + 1}. {lineas[i].strip()}")

    print("Escribe el número de la tarea que deseas eliminar:")
    opcion = input()
    indice = int(opcion) - 1

    if indice < 0 or indice >= len(lineas):
        print("❌ Número inválido.\n")
        return

    # Quitamos la línea seleccionada
    eliminada = lineas.pop(indice)

    # Reescribimos el archivo sin esa tarea
    archivo_escritura = open(archivo, "w")
    archivo_escritura.writelines(lineas)
    archivo_escritura.close()
    print(f"🗑 Tarea eliminada: {eliminada.strip()}\n")

# Menú principal
def menu():
    while True:
        print("--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("Elige una opción:")
        opcion = input()

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción inválida.\n")

# Ejecutamos el menú
menu()
