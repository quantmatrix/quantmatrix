# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

from quantmatrix.model import ModelBase
from quantmatrix.database import Database


def init_china():
    from quantmatrix.model.datasource.transaction.stock_certificate.china.stock_certificate import StockCertificate

    ModelBase.metadata.create_all(Database().get_quantmatrix_engine())
