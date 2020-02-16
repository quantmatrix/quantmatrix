# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

from sqlalchemy import Column
from sqlalchemy.types import String
from quantmatrix.model import ModelBase


class PumpTransaction(ModelBase):
    market = Column(
        String(100),
        default="",
        nullable=False,
        comment="市场"
    )
