# Catálogo de productos de la startup deportiva
catalogo = {
    1: {"nombre": "Balón de Vóley profesional", "precio": 120.0},
    2: {"nombre": "Rodilleras deportivas", "precio": 45.0},
    3: {"nombre": "Zapatillas de entrenamiento", "precio": 250.0},
    4: {"nombre": "Botella térmica 1L", "precio": 60.0},
    5: {"nombre": "Camiseta deportiva", "precio": 75.0}
}

def mostrar_catalogo():
    """Muestra los productos disponibles de forma ordenada."""
    print("\n" + "="*40)
    print("       CATÁLOGO - SPORTSTARTUP")
    print("="*40)
    print("ID | Producto                  | Precio (S/)")
    print("-" * 40)
    for id_prod, info in catalogo.items():
        print(f"{id_prod:<2} | {info['nombre']:<25} | S/ {info['precio']:.2f}")
    print("="*40)

def iniciar_tienda():
    """Controla la lógica principal de la tienda y el carrito."""
    carrito = []
    total_general = 0.0
    
    print("¡Bienvenido a tu simulador de Startup Deportiva!")
    
    while True:
        mostrar_catalogo()
        opcion = input("Ingresa el ID del producto que deseas comprar (o escribe '0' para finalizar): ")
        
        if opcion == '0':
            break
        
        if opcion.isdigit():
            id_prod = int(opcion)
            if id_prod in catalogo:
                cantidad_str = input(f"¿Cuántas unidades de '{catalogo[id_prod]['nombre']}' deseas?: ")
                if cantidad_str.isdigit():
                    cantidad = int(cantidad_str)
                    subtotal = catalogo[id_prod]['precio'] * cantidad
                    
                    # Guardamos en el carrito
                    carrito.append({
                        "nombre": catalogo[id_prod]['nombre'], 
                        "cantidad": cantidad, 
                        "subtotal": subtotal
                    })
                    total_general += subtotal
                    print(f"-> ¡Agregado! Subtotal parcial: S/ {subtotal:.2f}\n")
                else:
                    print("[!] Error: Ingresa un número válido para la cantidad.\n")
            else:
                print("[!] Error: El ID del producto no existe. Intenta de nuevo.\n")
        else:
            print("[!] Error: Por favor ingresa un número válido.\n")

    # Ticket de compra / Resumen final
    print("\n" + "="*40)
    print("          RESUMEN DE TU COMPRA")
    print("="*40)
    if not carrito:
        print("No se registraron compras.")
    else:
        for item in carrito:
            print(f"- {item['cantidad']}x {item['nombre']} : S/ {item['subtotal']:.2f}")
        print("-" * 40)
        print(f"Total a pagar: S/ {total_general:.2f}")
        print("¡Gracias por apoyar esta iniciativa!")
    print("="*40)

if __name__ == "__main__":
    iniciar_tienda()