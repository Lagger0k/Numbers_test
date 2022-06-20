from datetime import date

from orders.models import Order
from orders.services.google_sheets_service import get_data_for_order_models


def get_order_models_from_db() -> list:
    """Возвращает актуальный список моделей orders, после всех изменений с учетом информации из таблицы"""
    _del_or_create_or_update_order_models()
    return Order.objects.all()


def get_delay_orders() -> list:
    """Возвращает список заказов, которые уже опаздывают по доставке"""
    today = date.today()
    orders_query = Order.objects.all()
    result = []
    for order in orders_query:
        print(order.delivery_date, today)
        if order.delivery_date < today:
            result.append(str(order.order_number))
    return result


def _del_or_create_or_update_order_models() -> None:
    """Создает, удаляет или обновляет модели orders на основе данных из таблицы"""
    data = get_data_for_order_models()
    if data:
        _del_orders_if_not_exist(data)
        for order in data:
            Order.objects.update_or_create(**order)


def _del_orders_if_not_exist(data: list) -> None:
    """Удаляет модели из БД, если они были удалены в таблице"""
    orders = Order.objects.all()
    if orders:
        for order in orders:
            tmp_dict = {
                "number": order.number,
                "order_number": order.order_number,
                "order_dollar_amount": order.order_dollar_amount,
                "delivery_date": order.delivery_date,
                "order_rub_amount": order.order_rub_amount}
            if tmp_dict not in data:
                order.delete()
