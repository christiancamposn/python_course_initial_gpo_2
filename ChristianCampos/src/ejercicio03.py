'''
    Args y kwargs
'''

#args: argumentos posicionales
#def procesar_datos(*args) -> None:
#    print(f"Argumentos posicionales recibidos: {args}")

#procesar_datos(2, 3, 4)

#def saludos_dinamicos(**kwargs) -> None:
#    print(f"Argumentos nombrados recibidos: {kwargs}")

#saludos_dinamicos(nombre = "Jona", edad = 30)

#Generadores -> Para manejar grandes volúmenes de datos, utilizan yield en lugar de return

def generar_datos(limite:int):
    '''Generador que produce números hasta un límite dado'''
    print("Inicio del generador")
    for num in range(limite):
        print(f"Bucle en posición {num}")
        yield num
    print("Fin del generador")

def generar_datos_tradicional(limite:int):
    '''Generador que produce números hasta un límite dado'''
    print("Inicio de la función tradicional")
    resultado = []
    for num in range(limite):
        print(f"Bucle en posición {num}")
        resultado.append(num)
    print("Fin del generador")
    return resultado
print("Uso del generador")
#print(type(generador_datos))
generador = generar_datos(5)

for item in generador:
    print(f"Valor generado: {item}")

listaa = generar_datos_tradicional(5)

for item in listaa:
    print(f"Valor generado {item}")