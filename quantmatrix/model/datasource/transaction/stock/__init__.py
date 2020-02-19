# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_stock():
    from quantmatrix.model.datasource.transaction.stock.china import init_china
    init_china()
