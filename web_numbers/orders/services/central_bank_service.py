import pytz as pytz
import requests
import datetime
import xml.etree.ElementTree as ElementTree
from web_numbers import settings
from typing import Optional


def get_currency_from_central_bank() -> Optional[float]:
    """Получает курс доллара к рублю на сегодня или на последний день выставления"""

    data = _get_data_from_central_bank()
    if data:
        currency = _search_currency(data=data, currency_id="R01235")
        return float(currency)
    else:
        return None


def _get_data_from_central_bank() -> Optional[str]:
    """Получает XML файл с курсами валют от центрального банка, на сегодня, если сегодня курсы не выставлялись,
    то получает последний выставленный"""

    time_zone = pytz.timezone("Europe/Moscow")
    date = datetime.datetime.now(time_zone).strftime("%d/%m/%Y")
    url = settings.CENTRAL_BANK_URL + date

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def _search_currency(data: str, currency_id: str) -> str:
    """Находит курс искомой валюты из файла XML со всеми валютами,
     узнать код нужной вам валюты можно на сайте ЦБ https://www.cbr.ru/development/SXML/"""

    root = ElementTree.fromstring(data)
    for block in root.iter("Valute"):
        if block.get('ID') == currency_id:
            cur = block.find("Value").text
            return cur.replace(',', '.')
