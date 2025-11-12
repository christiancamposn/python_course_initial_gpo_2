from src.ejercicio12 import Notificador

def test_enviar():
    print("test_enviar")
    notifica = Notificador()
    resultado = notifica.envia_mensaje("Hola Mundo")
    assert resultado == "Notificador: Hola Mundo"

def test_cancelar():
    print("test_cancelar")
    notifica = Notificador()
    resultado = notifica.cancelar("Adiós Mundo")
    assert resultado == "Notificador cancelado: Adiós Mundo"