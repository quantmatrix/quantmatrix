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

server: tornado.httpserver.HTTPServer


def authenticated(method):
    """Decorate methods with this to require that the user be logged in.

    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.

    If you configure a login url with a query parameter, Tornado will
    assume you know what you're doing and use it as-is.  If not, it
    will add a `next` paHTTPErrorrameter so the login page knows where to send
    you once you're logged in.
    """

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

    def render_json(self, data: Dict[str, Any], code: int, message: str):
        result: Dict[str, Any] = {
            "code": code,
            "message": message,
            "data": data
        }
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(tornado.escape.json_encode(result))


class IndexHandler(QuantMatrixRequestHandler):
    def get(self):
        self.write("hello quantmatrix")


class App(tornado.web.Application):
    def __init__(self):
        handlers: List[Any] = [
            (r"/", IndexHandler)
        ]
        settings: Any = {
            "debug": tornado.options.options["debug"],
            "template_path": "%s/web/%s" % (os.path.dirname(os.path.realpath(__file__)), "templates"),
            "static_path": "%s/web/%s" % (os.path.dirname(os.path.realpath(__file__)), "static"),
            "xsrf_cookies": True,
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

    tornado.log.LogFormatter(fmt="(name)s (asctime)s (threadName)s (levelname)s %(filename)s %(lineno)d %(message)s")

    global server
    server = tornado.httpserver.HTTPServer(App(), xheaders=True)
    server.add_sockets(tornado.netutil.bind_sockets(
        port=tornado.options.options["port"],
        address=tornado.options.options["address"],
        family=socket.AF_INET)
    )

    logging.info('quantmatrix start ...')
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
