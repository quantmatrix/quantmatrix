# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import os
import logging
import socket
import signal
import functools
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.escape
import tornado.netutil
import tornado.log
from typing import Any
from typing import List
from typing import Dict
from typing import Optional
from typing import Awaitable
from apscheduler.schedulers.tornado import TornadoScheduler

server: tornado.httpserver.HTTPServer
scheduler: TornadoScheduler = TornadoScheduler()


def authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.get_secure_cookie("auth"):
            raise tornado.web.HTTPError(403)
        return method(self, *args, **kwargs)

    return wrapper


class QuantMatrixRequestHandler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        return None

    def initialize(self):
        self.set_header('Server', 'QuantMatrixServer')
        self.set_header("Cache-Control", "private")
        self.set_header(
            "Version", open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'version.txt')).read().strip()
        )

    def render_json(self, data: Dict[str, Any] = None, code: int = 0, message: str = "success"):
        result: Dict[str, Any] = {
            "code": code,
            "message": message,
            "data": {} if data is None else data
        }
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(tornado.escape.json_encode(result))


class IndexHandler(QuantMatrixRequestHandler):
    def get(self):
        self.write("")


class QuantHandler(QuantMatrixRequestHandler):
    @authenticated
    def post(self):
        self.write("")


class InitHandler(QuantMatrixRequestHandler):
    def post(self):
        self.__init_data_source_path()

        self.__init_model()

        self.render_json()

    @classmethod
    def __init_data_source_path(cls):
        from quantmatrix.datasource import DATASOURCE, FUNDAMENTAL, NEWS, TRANSACTION

        # fundamental
        os.makedirs("%s/%s" % (tornado.options.options["data-source"], FUNDAMENTAL))

        # news
        os.makedirs("%s/%s" % (tornado.options.options["data-source"], NEWS))

        # transaction
        for merchandise, markets in DATASOURCE.get(TRANSACTION).items():
            for market in markets:
                directory = "%s/%s/%s/%s" % (tornado.options.options["data-source"], TRANSACTION, merchandise, market)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    os.makedirs("%s/file" % directory)

    @classmethod
    def __init_model(cls):
        from quantmatrix.model.system import init_system
        from quantmatrix.model.datasource import init_datasource
        from quantmatrix.model.quant import init_quant
        # system
        init_system()
        # datasource
        init_datasource()
        # quant
        init_quant()


class TestHandler(QuantMatrixRequestHandler):
    def get(self):
        self.write("")


class App(tornado.web.Application):
    def __init__(self):
        handlers: List[Any] = [
            (r"/", IndexHandler),
            (r"/quant", QuantHandler),
            (r"/init", InitHandler),
            (r"/test", TestHandler)
        ]

        # 股票
        # 中国A股
        from quantmatrix.datasource.input import transaction_stock_china
        scheduler.add_job(transaction_stock_china, "cron", day_of_week="0-4", hour=15, minute=3, second=0)

        settings: Any = {
            "debug": tornado.options.options["debug"],
            "template_path": "%s/web/%s" % (os.path.dirname(os.path.realpath(__file__)), "templates"),
            "static_path": "%s/web/%s" % (os.path.dirname(os.path.realpath(__file__)), "static"),
            "xsrf_cookies": False,
            'compress_response': False,
            "cookie_secret": "VcfW7jzUTKcT[33(ZdG#Xtxs12RzAPbYTWpvQKvEa8BKPfrKxz$diPB",
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    logging.warning('Caught frame: %s', frame)

    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    logging.info('Stopping quantmatrix ...')
    server.stop()
    tornado.ioloop.IOLoop.instance().stop()
    logging.info('Shutdown')


# Main program
def main():
    tornado.options.parse_command_line()

    tornado.log.enable_pretty_logging()

    global server
    server = tornado.httpserver.HTTPServer(App(), xheaders=True)
    server.add_sockets(tornado.netutil.bind_sockets(
        port=tornado.options.options["port"],
        address=tornado.options.options["address"],
        family=socket.AF_INET)
    )

    logging.info('quantmatrix start ...')

    scheduler.start()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    tornado.options.define("address", default="127.0.0.1", type=str, help="server address")
    tornado.options.define("port", default="8888", type=int, help="server port")
    tornado.options.define("data-source", default="./data", type=str, help="data source path")
    tornado.options.define("password", default="three", type=str, help="quantmatrix password")
    tornado.options.define("debug", default="false", type=bool, help="quantmatrix debug mode")

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    main()
