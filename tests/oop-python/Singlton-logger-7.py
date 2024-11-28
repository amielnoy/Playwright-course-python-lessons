import logging
import os
from datetime import datetime

class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        """Initialize the logger configuration."""
        self.logger = logging.getLogger("SingletonLogger")
        self.logger.setLevel(logging.DEBUG)

        # Create a directory for logs if it doesn't exist
        log_directory = "./logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Create file handler that logs messages to a file
        log_file = os.path.join(log_directory, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create console handler for logging to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Usage example
if __name__ == "__main__":
    logger1 = SingletonLogger()
    logger1.info("This is an info message.")

    logger2 = SingletonLogger()
    logger2.debug("This is a debug message.")

    # Both logger1 and logger2 are the same instance
    assert logger1 is logger2

    logger1.error("This is an error message.")
