# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import logging
from pip._internal.utils.logging import ColorizedStreamHandler
from pythonjsonlogger.jsonlogger import JsonFormatter
from quantmatrix.single import singleton


@singleton
class Logger(object):
    __logging: logging.Logger

    def __init__(self):
        self.__logging = logging.getLogger("quantmatrix")
        self.__logging.setLevel(logging.DEBUG)
        console_handler = ColorizedStreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(JsonFormatter(
            "(name)s (asctime)s (threadName)s (levelname)s %(filename)s %(lineno)d %(message)s")
        )
        self.__logging.addHandler(console_handler)

    def get_logging(self) -> logging.Logger:
        return self.__logging
