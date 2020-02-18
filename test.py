# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import tushare

pro = tushare.pro_api(token="168b4b447dde788ee239fa8d5b93c34cde6609bedbae5e96e939ef21")
df = pro.adj_factor(ts_code='000001.SZ', trade_date='')

print(df)