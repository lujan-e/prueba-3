import uuid
import json
import time
from pj import personajes
 
class Personaje():
def __init__(self, nombre, raza, clase, vida, mana):
self.nombre = nombre
self.raza = raza
self.clase = clase
self.vida = vida
self.mana = mana
 
def configurarPersonaje(self):
print("""\n ¿Qué personaje deseas crear?\n
1) Humanos
2) Orcos""")
raza = input("\n> ")
if raza == '1':
raza = "Humanos"
print("""\n¿Qué clase de humano deseas crear?\n
1) Guerrero
2) Jinete
3) Mago """)
clase = input("\n>")
if clase == '1':
clase = 'Guerrero'
#Llamaremos un método que cree el personaje
elif clase == '2':
clase = 'Jinete'
#Llamaremos un método que cree el personaje
elif clase == '3':
clase = 'Mago'
#Llamaremos un método que cree el personaje
elif raza == '2':
raza = "Orcos"
print("""\n¿Qué clase de orco deseas crear?\n
1) Guerrero
2) Chamán
3) Jinete """)
clase = input("\n> ;")
if clase == '1':
clase = 'Guerrero'
#Llamaremos un método que cree el personaje
elif clase == '2':
clase = 'Chamán'
#Llamaremos un método que cree el personaje
elif clase == '3':
clase = 'Jinete'
#Llamaremos un método que cree el personaje
else:
print("\nHas introducido un comando inválido")
pj = Personaje("Forking2412", "Humano", "Guerrero", "1200", "850")