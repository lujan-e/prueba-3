# tienda.py

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print(f"\nProductos disponibles en {self.nombre}:")
        for i, producto in enumerate(self._productos, start=1):
            producto.mostrar_informacion()
            print(f"{i}. {producto._nombre}")  # Mostrar nombre para selección

    def seleccionar_productos(self):
        carrito = []
        while True:
            self.mostrar_productos()
            try:
                eleccion = input("Seleccione el número del producto a agregar al carrito (o 'q' para finalizar): ")
                if eleccion.lower() == 'q':
                    break
                index = int(eleccion) - 1
                if 0 <= index < len(self._productos):
                    carrito.append(self._productos[index])
                    print(f"Agregado: {self._productos[index]._nombre}")
                else:
                    print("Selección no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido o 'q' para salir.")
        
        return carrito

    def procesar_compra(self, carrito):
        if not carrito:
            print("El carrito está vacío. No se puede procesar la compra.")
            return
        total = sum(producto.precio for producto in carrito)
        print("\nTotal de la compra:")
        for producto in carrito:
            producto.mostrar_informacion()
        print(f"Total: {total}")

