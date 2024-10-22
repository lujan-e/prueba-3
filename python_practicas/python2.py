productos = []

def añadir_producto():
    """Función para añadir un nuevo producto con validación."""
    while True:
        nombre = input("Introduce el nombre del producto (solo letras): ")
        if not nombre.replace(' ', '').isalpha():  # Verifica que el nombre solo contenga letras
            print("Error: El nombre solo debe contener letras. Intenta nuevamente.")
        else:
            break

    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número. Intenta nuevamente.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Intenta nuevamente.")

    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    """Función para ver todos los productos en la lista."""
    if productos:
        print("\nLista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos en la lista.")

def actualizar_producto():
    """Función para actualizar un producto con validaciones."""
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto que deseas actualizar: ")) - 1
            if 0 <= indice < len(productos):
                while True:
                    nuevo_nombre = input("Introduce el nuevo nombre del producto (solo letras): ")
                    if not nuevo_nombre.replace(' ', '').isalpha():
                        print("Error: El nombre solo debe contener letras. Intenta nuevamente.")
                    else:
                        break

                while True:
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio del producto: "))
                        break
                    except ValueError:
                        print("Error: El precio debe ser un número. Intenta nuevamente.")

                while True:
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad del producto: "))
                        break
                    except ValueError:
                        print("Error: La cantidad debe ser un número entero. Intenta nuevamente.")

                productos[indice] = {'nombre': nuevo_nombre, 'precio': nuevo_precio, 'cantidad': nueva_cantidad}
                print("Producto actualizado con éxito.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def eliminar_producto():
    """Función para eliminar un producto de la lista."""
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto que deseas eliminar: ")) - 1
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def guardar_datos():
    """Función para guardar los datos de los productos en un archivo de texto."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'.")

def cargar_datos():
    """Función para cargar los datos de productos desde un archivo de texto."""
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'.")
    except ValueError:
        print("Error al leer los datos del archivo.")

def menu():
    """Función principal para mostrar el menú y gestionar las opciones."""
    cargar_datos()  # Cargar los datos desde el archivo al iniciar el programa
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()





