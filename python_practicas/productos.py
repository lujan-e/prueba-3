# productos.py

from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrar_informacion(self):
        pass

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio

class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_informacion(self):
        print(f"Camisa - Nombre: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}")

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_informacion(self):
        print(f"Pantalon - Nombre: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}")

class Zapatos(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_informacion(self):
        print(f"Zapatos - Nombre: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}")

