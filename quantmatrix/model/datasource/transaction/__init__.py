# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_datasource_transaction_bond():
    pass


def init_datasource_transaction_forex():
    pass


def init_datasource_transaction_futures():
    pass


def init_datasource_transaction_stock():
    from quantmatrix.model.datasource.transaction.stock import init_china
    init_china()
