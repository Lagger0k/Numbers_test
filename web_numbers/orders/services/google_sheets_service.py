from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from orders.services.central_bank_service import get_currency_from_central_bank
from web_numbers import settings
from typing import Optional

from datetime import datetime


def get_data_for_order_models() -> Optional[list]:
    """Получает данные на основе которых будут созданы или обновлены модели orders в БД"""
    google_sheet_data = _get_data_from_googlesheets()
    currency = get_currency_from_central_bank()
    if google_sheet_data and currency:
        data = _prepare_data(data=google_sheet_data, currency=currency)
        return data
    return None


def _get_data_from_googlesheets() -> Optional[list]:
    """Получает данные из GoogleSheets"""
    creds = Credentials.from_authorized_user_file('token.json', settings.SCOPES)
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=settings.SPREADSHEET_ID,
                                    range=settings.RANGE_NAME).execute()
        values = result.get('values', [])
        return values if values else None

    except HttpError as err:
        print(err)


def _prepare_data(data: list, currency: float) -> list:
    """Подготавливает данные для создания моделей orders, построчно читая данные из таблицы"""
    result = []
    for row in data:
        data_dict = {
            "number": row[0],
            "order_number": int(row[1]),
            "order_dollar_amount": float(row[2].replace(',', '.')),
            "delivery_date": datetime.strptime(row[3], "%d.%m.%Y"),
            "order_rub_amount": round((float(row[2].replace(',', '.')) * currency), 2)}
        result.append(data_dict)
    return result
