import logging
from exceptions.exception import CustomError


logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/app.log'                
    )

def funcion_con_error(n1: int):
    if n1< 0:
        raise CustomError("Error: Número menor a cero")
    logging.info("El número es correcto")


try:
    funcion_con_error(5)
    funcion_con_error(-5)
except Exception as e:
    logging.error(f"Error: {e}")
else:
    logging.info("Ejecución correcta")
finally:
    logging.info("Ejecución finalizada")

