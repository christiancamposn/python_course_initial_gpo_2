class Producto:
    _nombre = ""

    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter 
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
productito = Producto("Monitor LG Curvo 32 pulgadas")
print(f"El nombre del producto es: {productito.nombre}")
productito.nombre = "x"
print(f"El nombre del producto es: {productito.nombre}")