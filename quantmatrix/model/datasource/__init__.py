# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_datasource():
    from quantmatrix.model.datasource.transaction import init_datasource_transaction_bond
    from quantmatrix.model.datasource.transaction import init_datasource_transaction_forex
    from quantmatrix.model.datasource.transaction import init_datasource_transaction_futures
    from quantmatrix.model.datasource.transaction import init_datasource_transaction_stock

    init_datasource_transaction_bond()
    init_datasource_transaction_forex()
    init_datasource_transaction_futures()
    init_datasource_transaction_stock()
