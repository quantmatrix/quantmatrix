# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import logging
import socket
import signal
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.escape
import tornado.netutil
import tornado.log
from typing import Any
from typing import List
from typing import Optional
from typing import Awaitable

server: tornado.httpserver.HTTPServer


class QuantMatrixRequestHandler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        return None


class MainHandler(QuantMatrixRequestHandler):
    def get(self):
        self.write("hello quantmatrix   ")


class App(tornado.web.Application):
    def __init__(self):
        handlers: List[Any] = [
            (r"/", MainHandler)
        ]
        settings: Any = {
            "debug": tornado.options.options["debug"],
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    logging.warning('Caught frame: %s', frame)

    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    logging.info('Stopping QuantMatrix ...')
    server.stop()
    tornado.ioloop.IOLoop.instance().stop()
    logging.info('Shutdown')


# Main program
def main():
    tornado.options.parse_command_line()

    tornado.log.enable_pretty_logging()

    tornado.log.LogFormatter(fmt="(name)s (asctime)s (threadName)s (levelname)s %(filename)s %(lineno)d %(message)s")

    global server
    server = tornado.httpserver.HTTPServer(App(), xheaders=True)
    server.add_sockets(tornado.netutil.bind_sockets(
        port=tornado.options.options["port"],
        address=tornado.options.options["address"],
        family=socket.AF_INET)
    )

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    tornado.options.define("address", default="127.0.0.1", type=str, help="server address")
    tornado.options.define("port", default="8888", type=int, help="server port")
    tornado.options.define("data-source", default="./data", type=str, help="data source path")
    tornado.options.define("username", default="three", type=str, help="quantmatrix username")
    tornado.options.define("password", default="three", type=str, help="quantmatrix password")
    tornado.options.define("debug", default="false", type=bool, help="quantmatrix debug mode")

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    main()
