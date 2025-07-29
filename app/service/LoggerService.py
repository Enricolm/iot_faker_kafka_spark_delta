import os
import logging
from logging.handlers import RotatingFileHandler

class LoggerService:
    def __init__(self, logger_name, console_level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            
            error_dir = f"/log/error/{logger_name}"
            os.makedirs(error_dir, exist_ok=True)

            formatter = logging.Formatter(
                '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            file_handler = RotatingFileHandler(
                f"{error_dir}/{logger_name}.log", 
                maxBytes=5*1024*1024, 
                backupCount=3
            )

            file_handler.setLevel(logging.ERROR)

            file_handler.setFormatter(formatter)

            stream_handler = logging.StreamHandler()

            stream_handler.setLevel(console_level)

            stream_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger
