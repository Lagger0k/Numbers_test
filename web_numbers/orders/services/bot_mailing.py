import requests

from orders.bot.database import get_users_for_mailing_list


def send_message(text: str) -> None:
    """Отправляет сообщение пользователю из списка рассылки о задержке поставки"""
    token = '5403902997:AAHzLZZd04MMKSx7RKRe9Nmdkw6H8IKplmQ'
    users_id = get_users_for_mailing_list()
    for user in users_id:
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + str(user) + "&text=" + text
        results = requests.get(url_req)
        print(results.json())
