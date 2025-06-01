
# Lista global para almacenar parcelas
parcelas = []

# Menú Principal
def MENU_PRINCIPAL():
    print("\n*** Bienvenidos al Centro de Monitoreo de Agro Tech Coop ***")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("1. AGREGAR PARCELA")
    print("2. MODIFICAR PARCELA")
    print("3. VER PARCELA")
    print("4. ELIMINAR PARCELA")
    print("5. SALIR")
    return input("Seleccione una opción: ")

# Submenú Agregar Parcela
def SUB_MENU2():
    print("\n--- AGREGAR NUEVA PARCELA ---")
    numero = input("1. Ingrese nuevo número para la nueva parcela: ")
    localidad = input("2. Inserte la localidad: ")
    superficie = input("3. Inserte la superficie en hectáreas: ")
    sensor = input("4. Activar sensor SI/NO: ")
    
    nueva_parcela = {
        "numero": numero,
        "localidad": localidad,
        "superficie": superficie,
        "sensor": sensor
    }
    parcelas.append(nueva_parcela)
    print("✅ Parcela agregada correctamente.")
    input("\nPresione ENTER para volver al menú...")

# Submenú Modificar Parcela
def SUB_MENU4():
    print("\n--- MODIFICAR PARCELA ---")
    if not parcelas:
        print("No hay parcelas para modificar.")
        input("\nPresione ENTER para volver al menú...")
        return

    for i, p in enumerate(parcelas, start=1):
        print(f"{i}. Parcela Nº {p['numero']} - {p['localidad']}")

    try:
        seleccion = int(input("Ingrese el número de parcela que desea modificar (por índice): "))
        if 1 <= seleccion <= len(parcelas):
            p = parcelas[seleccion - 1]
            print(f"\nParcela seleccionada: Nº {p['numero']} - {p['localidad']}")

            nuevo_numero = input(f"Nuevo número ({p['numero']}): ") or p['numero']
            nueva_localidad = input(f"Nueva localidad ({p['localidad']}): ") or p['localidad']
            nueva_superficie = input(f"Nueva superficie ({p['superficie']}): ") or p['superficie']
            nuevo_sensor = input(f"Sensor activo ({p['sensor']}): ") or p['sensor']

            p['numero'] = nuevo_numero
            p['localidad'] = nueva_localidad
            p['superficie'] = nueva_superficie
            p['sensor'] = nuevo_sensor

            print("✅ Parcela modificada correctamente.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")
    
    input("\nPresione ENTER para volver al menú...")

# Submenú Ver Parcela
def SUB_MENU():
    print("\n--- SUBMENÚ VER PARCELA ---")
    print("1. Ver todas las parcelas registradas")
    print("2. Volver al menú principal")
    return input("Seleccione una opción: ")

# Mostrar detalles de parcelas
def SUB_MENU1():
    if not parcelas:
        print("\nNo hay parcelas registradas.")
    else:
        print("\n--- DETALLES DE LAS PARCELAS ---")
        for i, p in enumerate(parcelas, start=1):
            print(f"\nParcela {i}")
            print(f"Número: {p['numero']}")
            print(f"Localidad: {p['localidad']}")
            print(f"Superficie: {p['superficie']} ha")
            print(f"Sensor activo: {p['sensor']}")
    
    input("\nPresione ENTER para volver al menú...")

# Submenú Eliminar Parcela
def SUB_MENU3():
    print("\n--- ELIMINAR PARCELA ---")
    if not parcelas:
        print("No hay parcelas para eliminar.")
        input("\nPresione ENTER para volver al menú...")
        return

    for i, p in enumerate(parcelas, start=1):
        print(f"{i}. Parcela Nº {p['numero']} - {p['localidad']}")

    try:
        seleccion = int(input("Ingrese el número de parcela que desea eliminar (por índice): "))
        if 1 <= seleccion <= len(parcelas):
            confirmacion = input("¿Está seguro que desea eliminar esta parcela? (SI/NO): ").strip().upper()
            if confirmacion == "SI":
                eliminada = parcelas.pop(seleccion - 1)
                print(f"✅ Parcela Nº {eliminada['numero']} eliminada.")
            else:
                print("Cancelado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

    input("\nPresione ENTER para volver al menú...")

# Programa Principal
while True:
    opcion = MENU_PRINCIPAL()

    if opcion == '1':
        SUB_MENU2()

    elif opcion == '2':
        SUB_MENU4()

    elif opcion == '3':
        sub_opcion = SUB_MENU()
        if sub_opcion == '1':
            SUB_MENU1()
        elif sub_opcion == '2':
            continue
        else:
            print("Opción inválida.")

    elif opcion == '4':
        SUB_MENU3()

    elif opcion == '5':
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
