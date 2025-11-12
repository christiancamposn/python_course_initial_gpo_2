# Comentario en línea

'''
Comentario
multilínea
'''

# Tipos de datos
mi_variable = 10
print(type(mi_variable))

mi_variable = 10.5
print(type(mi_variable))

mi_variable = "¡Hola, Mundo!"
print(type(mi_variable))

mi_variable = True
print(type(mi_variable))

#Estructuras de datos

#Listas
mi_lista: list = [1, 2, 3, "Hola", True, 4.5]
print("Mi lista antes de la modificación", mi_lista)
mi_lista[2] = 4 #Modificando un elemento de la lista
print("Mi lista después de la modificación", mi_lista)
print(type(mi_lista))

#Tuplas
mi_tupla: tuple = (1,2,3)
#mi_tupla(2) = 4
print(type(mi_tupla))

#Diccionarios
mi_diccionario: dict = {"clave1": "valor1", "clave2": "valor2"}
print(type(mi_diccionario))

#Sets o conjuntos
mi_set: set = {1,2,3}

#f-strings
nombre: str = "Jona"

print("Hola, " + nombre) #Concatenación tradicional
print(f"Hola, {nombre}") #Usando f-string
'''
Compresiones
'''

#Listas
cuadrados = [x * x for x in range(5)]
print(cuadrados)

#Break y Continue y else