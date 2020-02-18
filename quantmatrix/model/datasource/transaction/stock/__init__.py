# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

from quantmatrix.model import ModelBase
from quantmatrix.database import Database


def init_china():
    from quantmatrix.model.datasource.transaction.stock.china.adjust_factor import AdjustFactor
    from quantmatrix.model.datasource.transaction.stock.china.index_daily import IndexDaily
    from quantmatrix.model.datasource.transaction.stock.china.stock_daily import StockDaily

    ModelBase.metadata.create_all(Database().get_quantmatrix_engine())
