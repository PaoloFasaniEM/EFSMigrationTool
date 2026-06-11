# services/logger.py

from enum import Enum


class LogLevel(Enum):
    INFO    = "white"
    OK      = "green"
    WARN    = "orange"
    ERROR   = "red"


class Logger:

    _instance = None
    _log_fn = None

    @classmethod
    def init(cls, log_fn):
        cls._log_fn = log_fn

    @classmethod
    def log(cls, message: str, level: LogLevel = LogLevel.INFO):
        if cls._log_fn is None:
            print(message)
            return
        cls._log_fn(message, level)

    @classmethod
    def info(cls, message: str):
        cls.log(message, LogLevel.INFO)

    @classmethod
    def ok(cls, message: str):
        cls.log(message, LogLevel.OK)

    @classmethod
    def warn(cls, message: str):
        cls.log(message, LogLevel.WARN)

    @classmethod
    def error(cls, message: str):
        cls.log(message, LogLevel.ERROR)