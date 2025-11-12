# Cálculo de Fibonnaci para el cálculo de la serie usando yield (generador)
def calculo_fibonacci():
    '''
    Generador de la serie de Fibonacci
    '''
    valor_a = 0
    valor_b = 1
    while True:
        yield valor_a   # Devuelve el valor actual
        temp = valor_a 
        # Actualiza los valores
        valor_a = valor_b
        valor_b = temp + valor_b 

#Se crea el generador
fibo = calculo_fibonacci()
#Entrada del usuario
elementos = int(input("¿Cuántos términos de Fibonacci se generarán?_"))
print(f"Se muestran los primeros [n] términos de la serie de Fibonacci")
for j in range(elementos):
    print(next(fibo), end= "; ")