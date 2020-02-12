# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import yaml
from typing import Dict
from typing import List
from typing import Any
from quantmatrix.single import singleton

MARKET_BOND: str = "bond"
MARKET_FOREX: str = "forex"
MARKET_FUTURES: str = "futures"
MARKET_STOCK: str = "stock"

MARKETS: List[str] = [
    MARKET_BOND, MARKET_FOREX, MARKET_FUTURES, MARKET_STOCK
]

NEWS_YAHOO = "yahoo"
NEWS_GOOGLE = "google"

NEWS_LIST: List[str] = [
    NEWS_YAHOO,
    NEWS_GOOGLE
]

COUNTRY_AMERICA: str = "us"  # 美国
COUNTRY_BRITAIN: str = "uk"  # 英国
COUNTRY_CANADA: str = "ca"  # 加拿大
COUNTRY_CHINA: str = "cn"  # 中国
COUNTRY_FRANCE: str = "fr"  # 法国
COUNTRY_GERMANY: str = "de"  # 德国
COUNTRY_HONG_KONG: str = "hk"  # 香港
COUNTRY_JAPAN: str = "jp"  # 日本
COUNTRY_SINGAPORE: str = "sg"  # 新加坡
COUNTRY_SWITZERLAND: str = "ch"  # 瑞士

COUNTRIES: List[str] = [
    COUNTRY_AMERICA,
    COUNTRY_BRITAIN,
    COUNTRY_CANADA,
    COUNTRY_CHINA,
    COUNTRY_FRANCE,
    COUNTRY_GERMANY,
    COUNTRY_HONG_KONG,
    COUNTRY_JAPAN,
    COUNTRY_SINGAPORE,
    COUNTRY_SWITZERLAND,
]

FOREX_AUSTRALIAN_DOLLAR = "aud"  # 澳元
FOREX_CAD = "cad"  # 加元
FOREX_DOLLAR = "usd"  # 美元
FOREX_EURO = "eur"  # 欧元
FOREX_NEW_ZEALAND_DOLLAR = "nzd"  # 纽元
FOREX_POUND = "gbp"  # 英镑
FOREX_SWISS_FRANC = "chf"  # 瑞士法郎
FOREX_YEN = "jpy"  # 日元

FOREXES = [
    FOREX_AUSTRALIAN_DOLLAR,
    FOREX_CAD,
    FOREX_DOLLAR,
    FOREX_EURO,
    FOREX_NEW_ZEALAND_DOLLAR,
    FOREX_POUND,
    FOREX_SWISS_FRANC,
    FOREX_YEN,
]


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

    def get_data_path(self) -> str:
        return self.__config.get("data_path", "")

    def get_pump_market(self, t: str) -> List[str]:
        result = []

        if t in MARKETS:
            try:
                for market in self.__config.get("qmpump").get("market").get(t, []):
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
            for n in self.__config.get("qmpump").get("news"):
                if n in NEWS_LIST:
                    result.append(n)
        except Exception as e:
            raise e

        return result
