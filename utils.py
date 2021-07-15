from telegram import ReplyKeyboardMarkup, KeyboardButton
from db import db_session, engine
from projects.mybot.models import UserToken


def main_keyboard():
    return ReplyKeyboardMarkup([['Полнолуние'],
                                [KeyboardButton('Где я?', request_location=True)],
                                ['Заполнить анекту'],
                                ['Авторизоваться через github']])


def get_token_from_db_by_chat_id(chat_id):
    token = db_session.query(UserToken).filter(user_id_github=chat_id)
    return token
