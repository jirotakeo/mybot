def send_hello(context):
    context.bot.send_message(chat_id=939352301, text='Здаров отец!')
    # if context.job.interval > 15:
    #     context.bot.send_message(chat_id=939352301, text='Ok! хватит здороваться!')
    #     context.job.shedule_removal()
