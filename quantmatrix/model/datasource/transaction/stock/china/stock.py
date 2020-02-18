# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.dialects.sqlite import TIMESTAMP
from quantmatrix.model import ModelBase


class Stock(ModelBase):
    """
    股票
    """
    code = Column(
        String(50),
        default="",
        nullable=False,
        comment="股票代码"
    )
    name = Column(
        String(500),
        default="",
        nullable=False,
        comment="名称"
    )
    exchange = Column(
        String(50),
        default="",
        nullable=False,
        comment="交易所"
    )
    offering_date = Column(
        TIMESTAMP,
        nullable=False,
        comment="上市日期"
    )
    last_transaction_date = Column(
        TIMESTAMP,
        nullable=False,
        comment="最后交易日期"
    )
