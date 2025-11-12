from abc import ABC, abstractmethod
'''
    Inyección de dependencias
'''
# Inyección por constructor
class ServiceEmail:
    def enviar_email(self, mensaje):
        print("Email enviado - {mensaje}")

class Notificador:
    def __init__(self, service: ServiceEmail):
        self.service = service
    
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)

service_email = ServiceEmail()
notificador = Notificador(service=service_email)

notificador.notificar("Contenido")

#Inyección por setter

class ServiceEmail:
    def enviar_email(self, mensaje):
        print("Email enviado - {mensaje}")

class Notificador:

    def set_email_service(self, service_email):
        self.service = service_email

    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)

service_email = ServiceEmail()
notifica = Notificador()
notifica.set_email_service(service_email=service_email)
notifica.notificar("Contenido setter")

class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendido eléctrico")

class MotorGasolina(MotorBase):
    def encender(self):
        print("Encendido gasolina")

class Auto:
    def __init__(self, motor_base: MotorBase):
        self.motor = motor_base
    
    def arrancar(self):
        self.motor.encender()

auto_electrico = Auto(MotorElectrico())
auto_gasolina = Auto(MotorGasolina())
auto_electrico.arrancar()
auto_gasolina.arrancar()