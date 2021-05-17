from settings import TOKEN, PROXY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, я эхо бот. Чтобы ты не написал я отвечу тем-же')


def main():
    mybot = Updater(TOKEN, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
