from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from API import dialogflow, getInfoAPI
from characterGestion import createCharacter, addCharacterStats
from tools.infoTreatment import *

updater = Updater(token='1228506430:AAHhakTQS0moSjszpVzXC8yyXXHMqJ195OY', use_context=True)  # Telegram API Token
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def infoTreatment(response, username):
    print(response)
    intent = response.query_result.intent.display_name
    if intent == "Master-Mode":
        # TODO: Buscar info en la API con lo que nos pida el usuario
        # Monster, race, spell, equipment, class
        #Properties: skill, stat
        if response.query_result.action == "Master-Mode.Master-Mode-Monsters":
            param = response.query_result.parameters
            #Si no existe el índice, petará. Ge de comprovar qué índices hay
            monster = param["Monsters"]
            data = getInfoAPI("monsters", monster)
            out = "this monster's "
            if param["Monster-Properties"].lower == "immunities":
                write_immunities(data, out)
            else:
                info = data[param["Monster-Properties"].lower]
                for a in param["Monster-Properties"].split("_"):
                    out += " " + a.lower
                out += "is:"

        #getInfoAPI()
        print("master")
    # elif response.query_result.intent.display_name == "create":
    #    print("creating")
    elif intent == "create - stats":
        print("Adding stats")
        addCharacterStats(response, username)
    else:
        try:
            todo = response.query_result.parameters['cosesafer']
            print(todo)
            if todo == "create":
                print("create")
                createCharacter(response, username)
            if todo == "edit":
                print("edit")
            if todo == "info":
                print("info")  # diferenciar por intent la info de character con info en general
            if todo == "combat":
                print("combat")
        except ValueError:
            pass


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def textMessage(update, context):
    # Sends user input to dialogflow and recieves response
    response = dialogflow(update.message.text, update.message.chat_id)
    # Call to python database gestion
    infoTreatment(response, update.message.chat.username)
    # Telegram bot writes response of dialogflow
    context.bot.send_message(chat_id=update.message.chat_id, text=response.query_result.fulfillment_text)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
text_handler = MessageHandler(Filters.text & (~Filters.command), textMessage)
dispatcher.add_handler(text_handler)
updater.idle()
# updater.stop()
