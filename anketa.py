from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler

from projects.mybot.utils import main_keyboard


def anket_start(update, context):
    update.message.reply_text(
        f'Привет, как Вас зовут? Напишите имя и фамилию',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def anket_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text('Напишите имя и фамилию')
        return 'name'
    else:
        context.user_data['anket'] = {'name': user_name}
        reply_keyboard = [['1', '2', '3', '4', '5']]
        update.message.reply_text(
            'Оцените бота, где 1 говно, а 5 творение бога!',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return 'rating'


def anket_rating(update, context):
    context.user_data['anket']['rating'] = int(update.message.text)
    update.message.reply_text("Оставьте комментарий в свободной форме или пропустите этот шаг, введя /skip")
    return 'comment'


def anket_comment(update, context):
    context.user_data['anket']['comment'] = update.message.text
    print('comment' in context.user_data['anket'])
    user_text = anket_format(context.user_data['anket'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def comment_skip(update, context):
    print('comment' in context.user_data['anket'])
    user_text = anket_format(context.user_data['anket'])

    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def anket_format(anketa):
    user_text = f'''
<b>Имя и Фамилия: </b> {anketa['name']}
<b>Оценка: </b> {anketa['rating']}'''
    if 'comment' in anketa:
        user_text += f"\n<b>Комментарий: </b>{anketa['comment']}"
    return user_text


def anket_dontknow(update, context):
    update.message.reply_text('Я не понял!')
