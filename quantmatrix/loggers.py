# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import logging
from pip._internal.utils.logging import ColorizedStreamHandler
from pythonjsonlogger.jsonlogger import JsonFormatter


class Logger(object):
    __instance = None
    logger = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.logger = logging.getLogger('quantmatrix')
        self.logger.setLevel(logging.DEBUG)
        console_handler = ColorizedStreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(JsonFormatter(
            '(name)s (asctime)s (threadName)s (levelname)s %(filename)s %(lineno)d %(message)s'))
        self.logger.addHandler(console_handler)


logger = Logger().logger
