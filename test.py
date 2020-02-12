# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


from quantmatrix import config
from quantmatrix.loggers import Logger

c = config.Configure("quantmatrix.yml")

print(c.get_pump_market(config.MARKET_FOREX))
print(c.get_pump_news())
