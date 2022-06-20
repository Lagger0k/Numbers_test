
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from orders.bot.database import get_users_for_mailing_list, insert_telegram_user
from orders.bot.louder import dp


@dp.message_handler(Command("start"))
async def show_start_menu(message: Message):
    """Ловим команду старт и добавляем user_id в БД для рассылки оповещения о задержке доставки"""
    user_id = message.from_user.id
    try:
        insert_telegram_user(user_id)
        await message.answer('Ваш ID успешно добавлен в базу, '
                             'вы получите уведомление, если ваш заказ будет задерживаться')
    except Exception as err:
        await message.answer('Здравствуйте, рады снова Вас видеть')


@dp.message_handler(content_types='text')
async def quick_doctor_search(message: Message):
    """Отвечает на сообщения в чате бота"""
    await message.reply("Я вас не понимаю. Бот предназначен только для рассылки уведомлений")
