# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import yaml
from typing import Dict
from typing import List
from typing import Any
from quantmatrix.single import singleton

UNIX_HTTP_SERVER: str = "unix_http_server"
PUMP: str = "pump"
QUANT: str = "quant"


@singleton
class Configure(object):
    __config: Dict[str, Any]
    __file: str

    def __init__(self, file: str):
        if file != "":
            self.__file = file
            self.reload()
        else:
            raise Exception("quantmatrix.yml not found")

    def reload(self):
        with open(self.__file, encoding="utf-8") as f:
            self.__config = yaml.safe_load(f)

    def get_all(self) -> Dict[str, Any]:
        return self.__config

    def debug(self) -> bool:
        return self.__config.get("debug", None) is not None

    def get_data_path(self) -> str:
        return self.__config.get("data_path", "")

    def get_unix_http_server(self, k: str) -> str:
        try:
            return self.__config.get(UNIX_HTTP_SERVER).get(k, "")
        except Exception as e:
            raise e

    def get_pump_market(self, t: str) -> List[str]:
        result = []

        if t in MARKETS:
            try:
                for market in self.__config.get(PUMP).get(t, []):
                    if t == MARKET_FOREX:
                        if market in FOREXES:
                            result.append(market)
                    else:
                        if market in COUNTRIES:
                            result.append(market)
            except Exception as e:
                raise e

        return result

    def get_pump_news(self) -> List[str]:
        result = []
        try:
            for n in self.__config.get(PUMP).get("news"):
                if n in NEWS_LIST:
                    result.append(n)
        except Exception as e:
            raise e

        return result
