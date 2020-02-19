# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_transaction():
    from quantmatrix.model.datasource.transaction.bond import init_bond
    from quantmatrix.model.datasource.transaction.forex import init_forex
    from quantmatrix.model.datasource.transaction.futures import init_futures
    from quantmatrix.model.datasource.transaction.stock import init_stock
    init_bond()
    init_forex()
    init_futures()
    init_stock()
