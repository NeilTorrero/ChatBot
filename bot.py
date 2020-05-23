from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

from API import dialogflow

updater = Updater(token='1228506430:AAHhakTQS0moSjszpVzXC8yyXXHMqJ195OY', use_context=True)# Telegram API Token
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
def textMessage(update, context):
    response = dialogflow(update.message.text)
    context.bot.send_message(chat_id=update.message.chat_id, text=response.query_result.fulfillment_text)
    #context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
text_handler = MessageHandler(Filters.text & (~Filters.command), textMessage)
dispatcher.add_handler(text_handler)
updater.idle()
#updater.stop()