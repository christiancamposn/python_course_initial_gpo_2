class Procesador:
    def __init__(self, marca:str, nucleos:int):
        self.nucleos = nucleos
    
class Memoria:
    def __init__(self, tamano: int, velocidad:float):
        self.tamano = tamano
        self.velocidad = velocidad

class Computadora:
    def __init__(self, procesador: Procesador, memoria: Memoria):
        self.procesador = procesador
        self.memoria = memoria
    
    def descripcion(self):
        ast = "******************************"
        print(f"{ast}")
        print("Procesador")
        print(f"     Marca: {self.procesador.marca}")
        print(f"     Núcleos: {self.procesador.nucleos}")
        print("Memoria")
        print(f"     Tamaño: {self.memoria.martamanoca}")
        print(f"{ast}")

pc1 = Computadora(procesador=Procesador(marca="Intel", nucleos=8), memoria=Memoria(tamano=10, velocidad=1100000.00))
pc1.descripcion()