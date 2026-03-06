usuarios = {}

gastos = {
    "comida": [],
    "transporte": [],
    "entretenimiento": [],
    "otros": []
}

usuario_actual = ""

def registrar_usuario():
    print("\n---- Registrar Usuario ----")
    usuario = input("Ingrese su Usuario: ")
    if usuario in usuarios:
        print(f"El usuario '{usuario}' ya existe. Por favor, elija otro.")
    else:
        contrasena = input("Ingresa tu contraseña: ")
        nombre = input("Ingresa tu nombre: ")
        usuarios[usuario] = contrasena
        print(f"Usuario '{usuario}' registrado exitosamente.")

def iniciar_sesion():
    global usuario_actual
    print("\n ---- Iniciar Sesion -----")
    usuario = input("Ingrese su Usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario in usuarios:
        if usuarios[usuario] == contrasena:
            usuario_actual = usuario
            print(f"Bienvenido, {usuario}!")
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    else:
        print("Usuario no encontrado. Por favor, regístrate primero.")

def menu_principal():
    print("\n---- Menu Principal ----")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesion")
    print("3. Salir")

def menu_gastos():
    print("\n---- Menu de Gastos ----")
    print("1. Agregar Gasto")
    print("2. Ver Gastos por categoria")
    print("3. Ver todos los Gastos")
    print("4. Cerrar sesion")

def agregar_gasto():
    print("\nCategorias disponibles: comida, transporte, entretenimiento, otros")
    categoria = input("Ingrese la categoria del gasto: ")

    if categoria in gastos:
        monto = float(input("Cuanto Gastaste? $"))
        descripcion = input("Descripcion del gasto: ")

        gastos[categoria].append({"monto": monto, "descripcion": descripcion, "usuario": usuario_actual})
        print(f"Gasto de ${monto} agregado a la categoria '{categoria}'.")
    else:
        print("Categoria no valida. Por favor, elija una categoria existente.")


def ver_gastos():
    categoria = input("\nCategoria que desea ver? ").lower()
    if categoria in gastos:
        lista = [gasto for gasto in gastos[categoria] if gasto["usuario"] == usuario_actual]
        if len(lista) == 0:
            print(f"No hay gastos registrados en la categoria '{categoria}' para el usuario '{usuario_actual}'.")
        else:
            print(f"\n --- {categoria.upper()} ({usuario_actual}) ---")
            for gasto in lista:
                print(f"- ${gasto['monto']}: {gasto['descripcion']}")
    else:
        print("Categoria no valida. Por favor, elija una categoria existente.")

def ver_total():
    total_general = 0
    print(f"\n --- Resumen de Gastos para {usuario_actual} ---")
    for categoria, lista in gastos.items():
        total_categoria = sum(gasto["monto"] for gasto in lista if gasto["usuario"] == usuario_actual)
        total_general += total_categoria
        print(f" {categoria}: ${total_categoria:.2f}")
    print(f"\n Total General: ${total_general:.2f}")

opcion = ""
while opcion != "3":
    menu_principal()
    opcion = input("seleccione una opcion en el menu: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()

        if usuario_actual != "":
            opcion_gastos = ""
            while opcion_gastos != "4":
                menu_gastos()
                opcion_gastos = input("Seleccione una opcion en el menu de gastos: ")
                
                if opcion_gastos == "1":
                    agregar_gasto()
                elif opcion_gastos == "2":
                    ver_gastos()
                elif opcion_gastos == "3":
                    ver_total()
                elif opcion_gastos == "4":
                    print(f"Cerrando sesion de {usuario_actual}...")
                    usuario_actual = ""
                else:
                    print("Opcion no valida intente de nuevo")

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opcion no valida. Por favor, seleccione una opcion del menu.")

            



