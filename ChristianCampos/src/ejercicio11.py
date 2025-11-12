from dataclasses import dataclass 

@dataclass
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

@dataclass
class Rueda:
    def __init__(self, tamano):
        self.tamano = tamano 

@dataclass
class Coche:
    def __init__(self, marca:str, motor:Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas

    def __str__(self):
        return  (f"Coche marca: {self.marca}\n"
                f"Tipo de motor: {self.motor.tipo}\n"
                f"Número de ruedas: {len(self.ruedas)}")
        
    def description(self):
        print(f"Coche marca: {self.marca}")
        print(f"Tipo de motor: {self.motor.tipo}")
        print(f"Número de ruedas: {len(self.ruedas)}")

auto_uno = Coche("VM", motor=Motor("Diesel"), ruedas = [Rueda(2), Rueda(2)])
print(auto_uno)