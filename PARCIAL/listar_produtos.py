def listar_productos():
    if not inventario:
        print("📦 El inventario está vacío.")
        return
# FUNCIÓN LEN
    print(f"\n--- Lista de productos ({len(inventario)} en total) ---")
    for producto in inventario:
        print(f"Nombre: {producto['Nombre']} | Precio: ${producto['Precio']:.2f} | Cantidad: {producto['Cantidad']}")