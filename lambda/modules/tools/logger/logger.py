import os
import sys
import logging

LOGGER_FORMAT = '%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)


def get_level(level):
    return {
        'CRITICAL': logging.CRITICAL,
        'DEBUG': logging.DEBUG,
        'ERROR': logging.ERROR,
        'FATAL': logging.FATAL,
        'INFO': logging.INFO,
        'NOTSET': logging.NOTSET
        }.get(level, logging.INFO)


def add_console_handler(logger):
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)
    return handler


def get_logger():
    level = os.environ.get('LOG_LEVEL')
    logger = logging.getLogger(__name__)
    logger.setLevel(get_level(level))
    return logger
