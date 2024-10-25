# main.py

from productos import Camisa, Pantalon, Zapatos
from tienda import Tienda

# Crear instancias de productos
camisa1 = Camisa("Camisa Blanca", 20.0, "M")
pantalon1 = Pantalon("Pantalón Negro", 35.0, "L")
zapatos1 = Zapatos("Zapatos Deportivos", 50.0, 42)

# Crear una instancia de tienda y agregar productos
mi_tienda = Tienda("La Boutique")
mi_tienda.agregar_producto(camisa1)
mi_tienda.agregar_producto(pantalon1)
mi_tienda.agregar_producto(zapatos1)

# Seleccionar productos y procesar la compra
carrito = mi_tienda.seleccionar_productos()
mi_tienda.procesar_compra(carrito)

