from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orders.bot.bot_tables import TelegramUsers, base


# костыли, чтобы не выносить бота в отдельный проект
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE_NAME = getenv('DB_NAME')
DATABASE_USER = getenv('DB_USER')
DATABASE_PASSWORD = getenv('DB_PASSWORD')
DATABASE_HOST = getenv('DB_HOST')
DATABASE_PORT = getenv('DB_PORT')
try:
    ENGINE = create_engine(
        f'postgresql+psycopg2://{DATABASE_USER}:'
        f'{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')
except Exception as err:
    ENGINE = create_engine('postgresql+psycopg2://numbers_user:123123@localhost:54321/numbers_db')

SESSION = sessionmaker()


def insert_telegram_user(user_id) -> None:
    """Заносит user_id подписавшегося на телеграм бота юзера в БД"""
    _create_tables()
    with _session_scope() as session:
        user = TelegramUsers(user_id=user_id)
        session.add(user)


def get_users_for_mailing_list() -> list:
    """Вынимает ез БД users_id для рассылки уведомлений об опоздании"""
    with _session_scope() as session:
        query = session.query(TelegramUsers)
        users_id = [user.user_id for user in query]
        return users_id


@contextmanager
def _session_scope() -> None:
    session = SESSION(bind=ENGINE)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def _create_tables() -> None:
    """Создаем объявленные таблицы в базе если их там еще нет"""
    base.metadata.create_all(ENGINE)
