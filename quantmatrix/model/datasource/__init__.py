# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_datasource():
    from quantmatrix.model.datasource.transaction import init_transaction
    init_transaction()
