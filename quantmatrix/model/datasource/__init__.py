# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


def init_datasource():
    from quantmatrix.model.datasource.fundamental import init_fundamental
    from quantmatrix.model.datasource.news import init_news
    from quantmatrix.model.datasource.transaction import init_transaction
    init_fundamental()
    init_news()
    init_transaction()
