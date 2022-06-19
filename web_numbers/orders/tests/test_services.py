from django.test import TestCase
from datetime import datetime

from orders.services.central_bank_service import get_currency_from_central_bank
from orders.services.google_sheets_service import _prepare_data


class BankServiceTestCase(TestCase):

    def test_get_currency_from_central_bank(self):
        currency = get_currency_from_central_bank()
        self.assertEqual(float, type(currency))


class GoogleSheetsTestCase(TestCase):

    def test_prepare_data(self):
        data = [
            ['12', '1077923', '508', '01.06.2022']
        ]
        expected_result = [{
            "number": '12',
            "order_number": 1077923,
            "order_dollar_amount": 508.00,
            "delivery_date": datetime.strptime('01.06.2022', "%d.%m.%Y"),
            "order_rub_amount": round(50800.00, 2)
        }]
        result = _prepare_data(data, 100.00)
        self.assertEqual(expected_result, result)
