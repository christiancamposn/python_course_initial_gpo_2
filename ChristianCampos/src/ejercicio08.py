'''
Herencia y composición
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hacer un sonido")
    
class Perro(Animal):
    def __init__(self, nombre="Perro"):
        super().__init__(nombre)

    def hablar(self):
        print(self.nombre)
        print("¡Gua, gua!")

#animalito = Animal( )
perrito = Perro()

#animalito.hablar()
perrito.hablar()