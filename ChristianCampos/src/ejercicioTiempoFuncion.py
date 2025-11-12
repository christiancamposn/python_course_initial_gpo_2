import time 

def decorador(func):
    def envoltura(*arg, ** kwargs):
        inicio = time.time()
        ejecucion = func(*arg, ** kwargs)
        print(ejecucion)
        fin = time. time()
        print(f"Tiempo de Inicio: {inicio}")
        print(f"Tiempo de finalizacion: {fin}")
        print(f"Tiempo de ejecucion: {fin - inicio}")
        return ejecucion
    return envoltura

@decorador
def enchular():
    time.sleep(1)
    return "Finalizado"

enchular()