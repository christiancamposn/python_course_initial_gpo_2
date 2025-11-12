from typing import Dict

def calcular_precio_final(precio_base: float, iva: float) -> float:
    """
    Calcular el precio final de un producto aplicando el IVA.
    """
    precio_final = precio_base * (1 + iva)
    return precio_final

# Uso
precio = calcular_precio_final(1000.0, 0.16)
print(f"Precio final: {precio:.2f}")


def calcular_precio_producto(producto: Dict[str, float], iva: float) -> Dict[str, float]:
    """
    Recibe un producto con su precio base y devuelve un diccionario con el precio final.
    """
    precio_final = producto["precio_base"] * (1 + iva)
    return {
        "nombre": producto["nombre"],
        "precio_base": producto["precio_base"],
        "precio_final": precio_final
    }

# Uso
producto = {"nombre": "Laptop", "precio_base": 20000.0}
resultado = calcular_precio_producto(producto, 0.16)
print(resultado)
