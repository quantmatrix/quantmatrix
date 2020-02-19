# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_transaction():
    from quantmatrix.model.datasource.transaction.stock import init_stock
    init_stock()
