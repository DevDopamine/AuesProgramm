import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        os.makedirs('logs', exist_ok=True)

        self.logger_en = logging.getLogger('logger_en')
        self.logger_en.setLevel(logging.INFO)
        handler = RotatingFileHandler('logs/en_logs.log', maxBytes=5*1024*1024, backupCount=5, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger_en.addHandler(handler)

    def log_messages(self, message, level='info'):
        if level == 'info':
            self.logger_en.info(message)
        elif level == 'warning':
            self.logger_en.warning(message)
        elif level == 'error':
            self.logger_en.error(message)
        elif level == 'debug':
            self.logger_en.debug(message)
        elif level == 'critical':
            self.logger_en.critical(message)
        else:
            self.logger_en.debug(message)
