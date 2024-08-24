#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import abc
import enum


class ContextLoggerMessageType(enum.Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4


class ContextLogger(abc.ABC):
    """

    """

    def __init__(self):
        pass

    def _format_message(self, message_type, *messages):
        pass

    def _write_message(self, message_type, *messages):
        pass

    def info(self, *messages):
        """

        :param messages:
        :return:
        """
        self._format_message(ContextLoggerMessageType.INFO, *messages)

    def warn(self, *messages):
        """

        :param messages:
        :return:
        """
        self._format_message(ContextLoggerMessageType.WARNING, *messages)

    def error(self, *messages):
        """

        :param messages:
        :return:
        """
        self._format_message(ContextLoggerMessageType.ERROR, *messages)

    def debug(self, *messages):
        """

        :param messages:
        :return:
        """
        self._format_message(ContextLoggerMessageType.DEBUG, *messages)
