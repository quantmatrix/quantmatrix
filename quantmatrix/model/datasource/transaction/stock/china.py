# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import DATE, BOOLEAN, INTEGER, REAL, VARCHAR
from quantmatrix.model import ModelBase

STOCK_SQL: str = """
CREATE TABLE "Stock" (
    id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')) NOT NULL, 
    updated_at TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')) NOT NULL, 
    remove BOOLEAN NOT NULL, 
    code VARCHAR(50) NOT NULL, 
    name VARCHAR(500) NOT NULL, 
    exchange VARCHAR(50) NOT NULL, 
    offering_date DATE NOT NULL, 
    last_update_date DATE NOT NULL, 
    PRIMARY KEY (id), 
    CHECK (remove IN (0, 1))
)
"""


class Stock(ModelBase):
    """
    股票
    """
    code = Column(VARCHAR(50), default="", nullable=False, comment="股票代码")
    name = Column(VARCHAR(500), default="", nullable=False, comment="名称")
    exchange = Column(VARCHAR(50), default="", nullable=False, comment="交易所")
    offering_date = Column(DATE, nullable=False, comment="上市日期")
    last_update_date = Column(DATE, nullable=False, comment="最后数据更新日期")


class AdjustFactor(ModelBase):
    """
    每日股票复权因子
    """
    code = Column(VARCHAR(50), default="", nullable=False, comment="股票代码")
    date = Column(DATE, default="", nullable=False, comment="交易日期")
    factor = Column(REAL, default=0, nullable=False, comment="开盘价格")


class IndexDaily(ModelBase):
    """
    每日指数
    """
    code = Column(VARCHAR(50), default="", nullable=False, comment="指数代码")
    date = Column(DATE, default="", nullable=False, comment="交易日期")
    open = Column(REAL, default=0, nullable=False, comment="开盘指数")
    high = Column(REAL, default=0, nullable=False, comment="最高指数")
    low = Column(REAL, default=0, nullable=False, comment="最低指数")
    close = Column(REAL, default=0, nullable=False, comment="收盘指数")
    volume = Column(INTEGER, default=0, nullable=False, comment="成交量")


class StockDaily(ModelBase):
    """
    每日股票价格
    """
    code = Column(VARCHAR(50), default="", nullable=False, comment="股票代码")
    date = Column(DATE, default="", nullable=False, comment="交易日期")
    open = Column(REAL, default=0, nullable=False, comment="开盘价格")
    high = Column(REAL, default=0, nullable=False, comment="最高价格")
    low = Column(REAL, default=0, nullable=False, comment="最低价格")
    close = Column(REAL, default=0, nullable=False, comment="收盘价格")
    volume = Column(INTEGER, default=0, nullable=False, comment="成交量")
    tick = Column(BOOLEAN, default=False, nullable=False, comment="分笔数据")


def init_china():
    from quantmatrix.datasource import COUNTRY_CHINA, STOCK
    from quantmatrix.database import Database

    Database().get_transaction_instance(STOCK, COUNTRY_CHINA).execute(STOCK_SQL)
