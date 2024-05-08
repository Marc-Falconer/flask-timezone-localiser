import time
import logging
from logging.handlers import TimedRotatingFileHandler

def timed_rotating_log_helper(file_path, datetime_format="%Y-%m-%d %H:%M:%S",
                                backup_count=5, log_level=logging.INFO):
    # Set up logging format.
    log_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt=datetime_format if datetime_format else '%Y-%m-%d %H:%M:%S'
    )
    #Set logging path.
    log_file = file_path
    
    # Create a timed rotating log file handler
    rotating_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',
        interval=1,
        backupCount=backup_count if backup_count else 5 
    )
    # Set sufix for rotated log file and log levels
    rotating_handler.suffix = '%Y-%m-%d'
    rotating_handler.setFormatter(log_formatter)
    rotating_handler.setLevel(log_level)
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Add the rotating file handler to the logger
    logger.addHandler(rotating_handler)