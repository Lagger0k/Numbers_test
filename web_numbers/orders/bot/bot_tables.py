from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger

base = declarative_base()


class TelegramUsers(base):
    __tablename__ = "telegram_users"

    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id
