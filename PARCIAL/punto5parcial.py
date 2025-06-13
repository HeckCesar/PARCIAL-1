# INVENTARIO CON DIC ANIDADOS
inventario = [
    {"Nombre": "Monitor 24\"", "Precio": 85.50, "Cantidad": 10},
    {"Nombre": "Teclado gamer", "Precio": 45.00, "Cantidad": 5},
    {"Nombre": "Mouse óptico", "Precio": 15.75, "Cantidad": 20},
    {"Nombre": "Telefono celular usado", "Precio": 120000.00, "Cantidad": 3},
]
# FUNCION DEFINIDA PARA CARGA
def cargar_producto():
    Nombre = input("Ingrese el nombre del producto: ").strip()
    if not Nombre:
        print(" El nombre no puede estar vacío.")
        return

    try:
        Precio = float(input("Ingrese el precio unitario del producto: "))
        if Precio < 0:
            print(" El precio no puede ser negativo.")
            return
    except ValueError:
        print(" Precio inválido. Ingrese un número con decimales.")
        return
# CONTROLES DE ERRORES  Y EXCEPCIONES
    try:
        Cantidad = int(input("Ingrese la cantidad disponible: "))
        if Cantidad < 0:
            print(" La cantidad no puede ser negativa.")
            return
    except ValueError:
        print(" Cantidad inválida. Ingrese un número entero.")
        return

    producto = {
        "Nombre": Nombre,
        "Precio": Precio,
        "Cantidad": Cantidad
    }

    inventario.append(producto)
    print(" Producto agregado correctamente.")
# AQUI TENEMOS UN MODULO PARA LISTAR
def listar_productos():
    if not inventario:
        print("📦 El inventario está vacío.")
        return
# FUNCIÓN LEN
    print(f"\n--- Lista de productos ({len(inventario)} en total) ---")
    for producto in inventario:
        print(f"Nombre: {producto['Nombre']} | Precio: ${producto['Precio']:.2f} | Cantidad: {producto['Cantidad']}")

def buscar_producto():
    nombre_busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    for producto in inventario:
        if producto["Nombre"].lower() == nombre_busqueda.lower():
            print(f"✅ Producto encontrado: {producto['Nombre']} - Precio: ${producto['Precio']:.2f}, Cantidad: {producto['Cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print(" Producto no encontrado.")
# CALCULOS DE SUMA, MULTIPLICACIONES.
def calcular_valor_total():
    total = sum(producto["Precio"] * producto["Cantidad"] for producto in inventario)
    print(f"\n💰 Valor total del inventario: ${total:.2f}")
# FUNCION DE CONTROL MIENTRAS SE EJECUTA EL PROGRAMA
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Cargar producto")
        print("2. Listar productos")
        print("3. Buscar producto por nombre")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        #USO IF, ELIF, ELSE
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            calcular_valor_total()
        elif opcion == "5":
            print(" Saliendo del programa. ¡Vuelve pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# EJECUTA EL  MENU
menu()
#EL CRITERIO USADO PARA LAS VARIABLES SIEMPRE SUELE SER EL NOMBRE DE LO MAS APROXIMADO POSIBLE A LO QUE SE QUIERE REPRESENTAR.