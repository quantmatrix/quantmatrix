# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


from typing import Any
from typing import Dict

FUNDAMENTAL = "fundamental"
NEWS = "news"
TRANSACTION = "transaction"

NEWS_YAHOO = "yahoo"
NEWS_GOOGLE = "google"

BOND: str = "bond"
FOREX: str = "forex"
FUTURES: str = "futures"
STOCK_CERTIFICATE: str = "stock_certificate"

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

FOREX_AUSTRALIAN_DOLLAR = "aud"  # 澳元
FOREX_CAD = "cad"  # 加元
FOREX_DOLLAR = "usd"  # 美元
FOREX_EURO = "eur"  # 欧元
FOREX_NEW_ZEALAND_DOLLAR = "nzd"  # 纽元
FOREX_POUND = "gbp"  # 英镑
FOREX_SWISS_FRANC = "chf"  # 瑞士法郎
FOREX_YEN = "jpy"  # 日元

DATASOURCE: Dict[str, Any] = {
    FUNDAMENTAL: {},
    NEWS: [
        NEWS_YAHOO, NEWS_GOOGLE
    ],
    TRANSACTION: {
        BOND: [
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
        ],
        FOREX: [
            FOREX_AUSTRALIAN_DOLLAR,
            FOREX_CAD,
            FOREX_DOLLAR,
            FOREX_EURO,
            FOREX_NEW_ZEALAND_DOLLAR,
            FOREX_POUND,
            FOREX_SWISS_FRANC,
            FOREX_YEN,
        ],
        FUTURES: [
            COUNTRY_AMERICA,
            COUNTRY_BRITAIN,
            COUNTRY_HONG_KONG,
            COUNTRY_SINGAPORE,
        ],
        STOCK_CERTIFICATE: [
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
    }
}
