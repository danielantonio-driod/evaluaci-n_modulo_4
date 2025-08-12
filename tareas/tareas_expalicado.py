# Este programa permite gestionar tareas simples desde la terminal.
# Puedes agregar tareas, verlas, marcarlas como completadas, eliminarlas
# y todo se guarda en un archivo de texto llamado tareas.txt

# -------------------------------
# FUNCIÓN PARA CARGAR LAS TAREAS
# -------------------------------
def cargar_tareas():
    # Abrimos el archivo en modo lectura
    archivo = open("tareas.txt", "r")
    tareas = []  # Lista donde guardaremos las tareas cargadas

    # Recorremos cada línea del archivo
    for linea in archivo:
        # Buscamos manualmente el separador " | " entre estado y nombre
        posicion = 0
        while posicion < len(linea) and linea[posicion] != "|":
            posicion += 1

        # Obtenemos la parte izquierda (estado) y derecha (nombre)
        estado = linea[:posicion - 1]  # Quitamos el espacio antes del "|"
        nombre = linea[posicion + 2:]  # Saltamos el espacio después del "|"
        nombre = nombre.replace("\n", "")  # Eliminamos el salto de línea final

        # Convertimos el estado en True o False
        if estado == "Completada":
            completada = True
        else:
            completada = False

        # Creamos un diccionario con la tarea y lo agregamos a la lista
        tarea = {"nombre": nombre, "completada": completada}
        tareas.append(tarea)

    # Cerramos el archivo después de leer
    archivo.close()
    return tareas  # Devolvemos la lista de tareas

# -------------------------------
# FUNCIÓN PARA GUARDAR LAS TAREAS
# -------------------------------
def guardar_tareas(tareas):
    # Abrimos el archivo en modo escritura (sobrescribe el archivo)
    archivo = open("tareas.txt", "w")

    # Recorremos cada tarea para guardarla en el archivo
    for tarea in tareas:
        if tarea["completada"] == True:
            estado = "Completada"
        else:
            estado = "Pendiente"

        # Armamos la línea con el formato "Estado | Nombre"
        linea = estado + " | " + tarea["nombre"] + "\n"
        archivo.write(linea)  # Escribimos la línea en el archivo

    # Cerramos el archivo al terminar
    archivo.close()

# ----------------------------
# FUNCIÓN PARA AGREGAR TAREAS
# ----------------------------
def agregar_tarea(tareas):
    print("Ingresa el nombre de la nueva tarea:")
    nombre = input()  # Solicitamos el nombre al usuario

    # Creamos un diccionario representando la tarea
    tarea = {"nombre": nombre, "completada": False}
    tareas.append(tarea)  # Agregamos la tarea a la lista

    guardar_tareas(tareas)  # Guardamos las tareas actualizadas
    print("✅ Tarea agregada.\n")

# --------------------------
# FUNCIÓN PARA VER TAREAS
# --------------------------
def ver_tareas(tareas):
    if len(tareas) == 0:
        print("📭 No hay tareas para mostrar.\n")
    else:
        print("📋 Lista de tareas:")
        for i in range(len(tareas)):
            tarea = tareas[i]
            # Mostramos un símbolo según el estado de la tarea
            if tarea["completada"]:
                estado = "✔ Completada"
            else:
                estado = "⏳ Pendiente"
            print(str(i + 1) + ". " + tarea["nombre"] + " [" + estado + "]")
        print("")  # Línea en blanco al final

# --------------------------------------
# FUNCIÓN PARA MARCAR UNA TAREA COMPLETA
# --------------------------------------
def completar_tarea(tareas):
    ver_tareas(tareas)  # Mostramos las tareas primero
    if len(tareas) > 0:
        print("Número de tarea a marcar como completada:")
        opcion = input()  # Pedimos un número al usuario
        indice = int(opcion) - 1  # Restamos 1 porque las listas empiezan en 0

        # Validamos que el número esté dentro del rango
        if indice >= 0 and indice < len(tareas):
            tareas[indice]["completada"] = True  # Marcamos como completada
            guardar_tareas(tareas)  # Guardamos cambios
            print("✅ Tarea marcada como completada.\n")
        else:
            print("❌ Número inválido.\n")

# -------------------------------
# FUNCIÓN PARA ELIMINAR UNA TAREA
# -------------------------------
def eliminar_tarea(tareas):
    ver_tareas(tareas)  # Mostramos la lista de tareas
    if len(tareas) > 0:
        print("Número de tarea a eliminar:")
        opcion = input()
        indice = int(opcion) - 1

        # Validamos el índice
        if indice >= 0 and indice < len(tareas):
            tareas.pop(indice)  # Quitamos la tarea de la lista
            guardar_tareas(tareas)  # Guardamos la nueva lista
            print("🗑 Tarea eliminada correctamente.\n")
        else:
            print("❌ Número inválido.\n")

# --------------------------
# MENÚ PRINCIPAL DEL PROGRAMA
# --------------------------
def menu():
    tareas = cargar_tareas()  # Cargamos las tareas al iniciar

    # Ciclo principal del menú
    while True:
        print("--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("Elige una opción:")
        opcion = input()  # Leemos la opción del usuario

        # Ejecutamos la opción seleccionada
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break  # Salimos del bucle
        else:
            print("❌ Opción inválida. Intenta otra vez.\n")

# --------------------------
# PUNTO DE INICIO DEL PROGRAMA
# --------------------------
menu()
