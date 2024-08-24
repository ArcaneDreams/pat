#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import logging
import os
from logging import Logger
import logging.handlers
from pat import __project__

from pat.helpers.helpers_date import get_current_date

_logger = None


def get_default_log_path() -> str:
    """
    Get the absolute path to where the log files should be stored.
    :return:
    """
    if __debug__:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    else:
        return os.path.abspath(os.path.join(os.getcwd(), 'logs'))


def get_default_log_filepath() -> str:
    """
    Get the absolute path to where the log file is stored.
    :return: Returns the absolute path to where the log file is stored.
    """
    return os.path.join(get_default_log_path(), f"pat-log-{get_current_date()}.log")


def get_logger() -> logging.Logger:
    """
    Get the logger instance
    :return:
    """
    return


def _create_log_file_hanlder() -> logging.handlers.RotatingFileHandler:
    """
    Instantiate a new log file handler instance and return it
    :return:
    """
    file_handler = logging.handlers.RotatingFileHandler(get_default_log_filepath())
    return file_handler


def get_or_create_logger() -> logging.Logger:
    """
    Get or create the logger if it doesn't exist.
    :return:
    """
    global _logger
    if _logger is None:
        _logger = create_logger()

    return _logger


def create_logger() -> logging.Logger:
    """

    :return:
    """
    global _logger
    _logger = Logger(__project__)
    _logger.addHandler(logging.StreamHandler())
    _logger.addHandler(logging.StreamHandler())

    return _logger
