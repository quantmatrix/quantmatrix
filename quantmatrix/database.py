# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import tornado.options
from typing import Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from quantmatrix.single import singleton


@singleton
class Database(object):
    __fundamental_engines: Dict[str, Any] = {}
    __fundamental_sessions: Dict[str, sessionmaker] = {}
    __news_engines: Dict[str, Any] = {}
    __news_sessions: Dict[str, sessionmaker] = {}
    __transaction_engines: Dict[str, Any] = {}
    __transaction_sessions: Dict[str, sessionmaker] = {}
    __quantmatrix_engine: Any = None
    __quantmatrix_session: sessionmaker = None

    def get_transaction_engine(self, merchandise: str, market: str) -> Any:
        k: str = "%s:%s" % (merchandise, market)
        if self.__transaction_engines.get(k) is None:
            engine_dir = "%s/transaction/%s/%s" % (tornado.options.options["data-source"], merchandise, market)
            self.__transaction_engines[k] = create_engine(
                "sqlite:///%s/%s.db?check_same_thread=False" % (engine_dir, market),
                encoding="utf8",
                echo=True
            )
        return self.__transaction_engines.get(k)

    def get_transaction_instance(self, merchandise: str, market: str) -> sessionmaker:
        k: str = "%s:%s" % (merchandise, market)
        if self.__transaction_sessions.get(k) is None:
            self.__transaction_sessions[k] = sessionmaker(bind=self.get_transaction_engine(merchandise, market))()
        return self.__transaction_sessions.get(k)

    def get_quantmatrix_engine(self) -> Any:
        if self.__quantmatrix_engine is None:
            self.__quantmatrix_engine = create_engine(
                "sqlite:///%s/quantmatrix.db?check_same_thread=False" % tornado.options.options["data-source"],
                encoding="utf8",
                echo=True
            )
        return self.__quantmatrix_engine

    def get_quantmatrix_instance(self):
        if self.__quantmatrix_session is None:
            self.__quantmatrix_session = sessionmaker(bind=self.get_quantmatrix_engine())()
        return self.__quantmatrix_session
