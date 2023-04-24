import logging
import sys

def write_log(logger_name, level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    format_string = ("%(name)s :: %(asctime)s :: lvl: %(levelname)s :: line: %(lineno)d :: funcName: %(funcName)s :: %(message)s")
    log_format = logging.Formatter(format_string)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler("LOGS/"+logger_name+".log", mode='a')
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    return logger