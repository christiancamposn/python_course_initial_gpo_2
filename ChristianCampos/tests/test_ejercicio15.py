from src.ejercicio15 import Servicio

class LoggerMock:
    def info(self, msg):
        print("Message Log Mock")

def test_servicio(mocker):
    mock_logger = mocker.Mock()

    service = Servicio(logger=mock_logger)
    service.procesar_data()
    mock_logger.info.assert_called_once_with("Procesando data...")