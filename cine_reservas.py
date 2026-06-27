"""
==================================================================
 PROYECTO FINAL - SISTEMA DE RESERVAS DE CINE
 Asignatura: Logica de Programacion
 ------------------------------------------------------------------
 Este programa simula la reserva de asientos en una sala de cine.
 El usuario puede:
   1. Ver el mapa de asientos disponibles
   2. Reservar un asiento
   3. Cancelar una reserva
   4. Consultar la ocupacion de la sala
   5. Buscar una reserva (por asiento o por nombre del cliente)
   6. Salir del sistema

 La sala se representa con un diccionario, donde cada asiento
 (ejemplo: "A1") guarda si esta ocupado y el nombre del cliente.

 Nota del grupo: al principio pensamos en usar una lista con los
 numeros de los asientos, pero buscar un asiento especifico ahi
 hubiera sido mas lento (tocaria recorrerla toda). Por eso se opto
 por un diccionario: se llega directo al asiento usando su codigo
 como clave, sin recorrer nada de mas.
==================================================================
"""


# ------------------------------------------------------------------
# FUNCION: inicializar_sala
# Input:  no recibe nada
# Output: retorna un diccionario que representa la sala de cine,
#         con todos los asientos marcados como libres al inicio
# ------------------------------------------------------------------
def inicializar_sala():
    filas = ["A", "B", "C", "D"]       # filas de la sala
    asientos_por_fila = 5              # asientos en cada fila
    sala = {}                          # aqui se guarda toda la sala

    for fila in filas:
        for numero in range(1, asientos_por_fila + 1):
            codigo_asiento = fila + str(numero)   # ejemplo: A1, A2, B1...
            sala[codigo_asiento] = {
                "ocupado": False,
                "cliente": None
            }
    return sala


# ------------------------------------------------------------------
# FUNCION: mostrar_asientos
# Input:  sala (diccionario con todos los asientos)
# Output: no retorna nada, solo imprime en pantalla el mapa
#         de asientos con su estado (Libre u Ocupado)
# ------------------------------------------------------------------
def mostrar_asientos(sala):
    print("\n----- MAPA DE ASIENTOS -----")
    for codigo_asiento, info in sala.items():
        if info["ocupado"]:
            estado = "Ocupado (" + info["cliente"] + ")"
        else:
            estado = "Libre"
        print("  Asiento " + codigo_asiento + ": " + estado)
    print("-----------------------------\n")


# ------------------------------------------------------------------
# FUNCION: reservar_asiento
# Input:  sala (diccionario), codigo_asiento (texto), nombre_cliente (texto)
# Output: retorna True si la reserva se hizo bien, False si no se pudo
# ------------------------------------------------------------------
def reservar_asiento(sala, codigo_asiento, nombre_cliente):
    codigo_asiento = codigo_asiento.upper()   # para que no importe mayus/minus

    if codigo_asiento not in sala:
        print("El asiento " + codigo_asiento + " no existe en esta sala.")
        return False

    if sala[codigo_asiento]["ocupado"]:
        print("El asiento " + codigo_asiento + " ya esta ocupado, elige otro.")
        return False

    sala[codigo_asiento]["ocupado"] = True
    sala[codigo_asiento]["cliente"] = nombre_cliente
    print("Reserva realizada: asiento " + codigo_asiento + " para " + nombre_cliente + ".")
    return True


# ------------------------------------------------------------------
# FUNCION: cancelar_reserva
# Input:  sala (diccionario), codigo_asiento (texto)
# Output: retorna True si se logro cancelar, False si no se pudo
# ------------------------------------------------------------------
def cancelar_reserva(sala, codigo_asiento):
    codigo_asiento = codigo_asiento.upper()

    if codigo_asiento not in sala:
        print("El asiento " + codigo_asiento + " no existe en esta sala.")
        return False

    if not sala[codigo_asiento]["ocupado"]:
        print("El asiento " + codigo_asiento + " ya estaba libre.")
        return False

    cliente_anterior = sala[codigo_asiento]["cliente"]
    sala[codigo_asiento]["ocupado"] = False
    sala[codigo_asiento]["cliente"] = None
    print("Se cancelo la reserva de " + cliente_anterior + " en el asiento " + codigo_asiento + ".")
    return True


# ------------------------------------------------------------------
# FUNCION: consultar_ocupacion
# Input:  sala (diccionario)
# Output: no retorna nada, imprime cuantos asientos hay ocupados,
#         cuantos libres y el porcentaje de ocupacion de la sala
# ------------------------------------------------------------------
def consultar_ocupacion(sala):
    total_asientos = len(sala)
    ocupados = 0

    for info in sala.values():
        if info["ocupado"]:
            ocupados = ocupados + 1

    libres = total_asientos - ocupados
    porcentaje = (ocupados / total_asientos) * 100

    print("\n----- OCUPACION DE LA SALA -----")
    print("  Total de asientos: " + str(total_asientos))
    print("  Ocupados: " + str(ocupados))
    print("  Libres: " + str(libres))
    print("  Porcentaje de ocupacion: " + str(round(porcentaje, 1)) + "%")
    print("---------------------------------\n")


# ------------------------------------------------------------------
# FUNCION: buscar_reserva
# Input:  sala (diccionario), criterio (texto: puede ser un codigo
#         de asiento o el nombre de un cliente)
# Output: no retorna nada, imprime el resultado de la busqueda
# ------------------------------------------------------------------
def buscar_reserva(sala, criterio):
    criterio = criterio.upper()

    # Primero revisamos si el criterio es directamente un codigo de asiento
    if criterio in sala:
        info = sala[criterio]
        if info["ocupado"]:
            print("El asiento " + criterio + " esta reservado por " + info["cliente"] + ".")
        else:
            print("El asiento " + criterio + " esta libre.")
        return

    # Si no era un codigo de asiento, buscamos por nombre de cliente
    encontrado = False
    for codigo_asiento, info in sala.items():
        if info["cliente"] is not None and info["cliente"].upper() == criterio:
            print(info["cliente"] + " tiene reservado el asiento " + codigo_asiento + ".")
            encontrado = True

    if not encontrado:
        print("No se encontro ninguna reserva con ese dato.")


# ------------------------------------------------------------------
# FUNCION: mostrar_menu
# Input:  no recibe nada
# Output: no retorna nada, solo imprime las opciones del menu
# ------------------------------------------------------------------
def mostrar_menu():
    print("\n========= SISTEMA DE RESERVAS DE CINE =========")
    print("1. Ver asientos disponibles")
    print("2. Reservar un asiento")
    print("3. Cancelar una reserva")
    print("4. Consultar ocupacion de la sala")
    print("5. Buscar una reserva")
    print("6. Salir")
    print("=================================================")


# ------------------------------------------------------------------
# FUNCION: main
# Input:  no recibe nada
# Output: no retorna nada, controla el flujo principal del programa
# ------------------------------------------------------------------
def main():
    sala = inicializar_sala()   # se crea la sala con todos los asientos libres

    while True:
        mostrar_menu()

        # usamos try/except para que el programa no se caiga si el
        # usuario escribe una letra en vez de un numero (nos paso
        # varias veces probando el programa, por eso lo agregamos)
        try:
            opcion = int(input("Elige una opcion (1-6): "))
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue

        if opcion == 1:
            mostrar_asientos(sala)

        elif opcion == 2:
            codigo = input("Ingresa el codigo del asiento (ejemplo A1): ")
            cliente = input("Ingresa tu nombre: ")
            reservar_asiento(sala, codigo, cliente)

        elif opcion == 3:
            codigo = input("Ingresa el codigo del asiento a cancelar: ")
            cancelar_reserva(sala, codigo)

        elif opcion == 4:
            consultar_ocupacion(sala)

        elif opcion == 5:
            criterio = input("Ingresa el codigo de asiento o el nombre del cliente: ")
            buscar_reserva(sala, criterio)

        elif opcion == 6:
            print("Gracias por usar el sistema. Hasta luego!")
            break

        else:
            print("Esa opcion no existe, elige un numero del 1 al 6.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()