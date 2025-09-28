import logging
import os

def setup_logger() -> logging.Logger:
    """Function to setup a logger; creates log directory if it doesn't exist."""
    name = "holiday_planner"
    level = logging.DEBUG
    log_file = "logs/holiday_planner.log"
    log_directory = os.path.dirname(log_file)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=0)  # 5MB, no backups
    handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()