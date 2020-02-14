# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

#
# from quantmatrix import config
# from quantmatrix.loggers import Logger
#
# c = config.Configure("../quantmatrix.yml")
#
# print(c.get_pump_market(config.MARKET_FOREX))
# print(c.get_pump_news())
#
# from datetime import datetime
# import os
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# def tick():
#     print('Tick! The time is: %s' % datetime.now())
#
#
# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#     scheduler.add_job(tick, 'interval', seconds=3)
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
#
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         pass
from typing import Optional, Awaitable

from quantmatrix.config import Configure
import quantmatrix.config
import tornado.ioloop
import tornado.web
import time


def coroutine_visit():
    print(321)
    time.sleep(60)
    print(123)


class QuantmatrixRequestHandler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class MainHandler(QuantmatrixRequestHandler):

    # def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
    #     print(123456)
    #     return None

    def get(self):
        tornado.ioloop.IOLoop.current().spawn_callback(coroutine_visit)

        self.write(Configure().get_all())


def get():
    Configure().reload()


class ReloadHandler(tornado.web.RequestHandler):
    pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/reload", ReloadHandler),
    ])


if __name__ == "__main__":
    Configure("/Users/zhangsan/Projects/quantmatrix/quantmatrix/quantmatrix.yml")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
