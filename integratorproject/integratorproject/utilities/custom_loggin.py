import logging


class CustomLogging():

    def CreateLogger(self, file_name: str, streamer: bool = False) -> logging:

        # Indicamos que tome el nombre del modulo
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)  # Configuramos el nivel de logging

        formatter = logging.Formatter(
            '%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')  # Creamos el formato

        # Indicamos el nombre del archivo
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)  # Configuramos el formato
        logger.addHandler(file_handler)  # Agregamos el archivo

        if (streamer):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger
