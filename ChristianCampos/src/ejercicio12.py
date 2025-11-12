class Notificador:
    def envia_mensaje(self, mensaje: str):
        return f"Notificador: {mensaje}"
    
    def cancelar(self, new_mensaje: str):
        return f"Notificador cancelado: {new_mensaje}"  