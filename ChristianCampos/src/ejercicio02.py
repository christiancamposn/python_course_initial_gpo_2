'''
Funciones
'''

def saludar(nombre: str = "Jona") -> None:
    '''
    Función para saludar al usuario por su nombre
    '''
    print(f"¡Hola, {nombre}!")

def saludo_personalizado(nombre: str) -> None:
    '''
    Función para saludar al usuario por su nombre
    '''
    print(f"¡Hola, {nombre}!")

# Tomar el valor por defecto
saludar()
# Pasar un valor diferente
saludar("Christian")

'''
Lambdas
'''

sumar = lambda num_1, num_2: num_1 + num_2
resultado: int = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}") 

'''
Maps
'''
lista = range(5)
operacion = lambda x: x**2
resultado = map(operacion,  lista)
#print(tuple(resultado))
def elevar_al_cuadrado(num: int) -> int:
    print(num)
    return num * num

print(list(map(elevar_al_cuadrado, tuple(range(5)))))

'''
Filters

'''
lista_pares = filter(lambda x: x%2 ==0, range(30))
print(list(lista_pares))