# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

from quantmatrix.database import Database
from quantmatrix.model import ModelBase


def init_system():
    from quantmatrix.model.system.pump_transaction import PumpTransaction
    
    ModelBase.metadata.create_all(Database().get_quantmatrix_engine())
