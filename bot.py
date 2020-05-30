from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from tools.API import dialogflow, getInfoAPI
from tools.characterGestion import *
from tools.infoTreatment import *
from tools.characterGestion import createCharacter, addCharacterStats, rollCharacterStats

updater = Updater(token='1228506430:AAHhakTQS0moSjszpVzXC8yyXXHMqJ195OY', use_context=True)  # Telegram API Token
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def infoTreatment(response, username):
    print(response)
    intent = response.query_result.intent.display_name
    if intent == "Master-Mode - Monsters":
        # La informació dels monstres està reservada al master
        if response.query_result.action == "Master-Mode.Master-Mode-Monsters":
            param = response.query_result.parameters
            # Si no existe el índice, petará. Ge de comprovar qué índices hay
            monster = param["monsters"]
            data = getInfoAPI("monsters", monster)
            out = "this monster's "
            if param["monster-properties"].lower() == "immunities":
                response.query_result.fulfillment_text += "\n" + write_immunities(data, out)
            else:
                response.query_result.fulfillment_text += "\n" + write_monster_properties(data, out, param)

        # getInfoAPI()
        print("master")
    elif response.query_result.action.split("-")[0] == "Info.Info":
        if response.query_result.action.split("-")[1] == "Class":
            param = response.query_result.parameters
            _class = param["classes"]
            try:
                level = param["ordinal"]
            except:
                level = 0
            data = getInfoAPI("classes", _class)
            out = "This class' "
            response.query_result.fulfillment_text += "\n" + write_class_properties(data, out, param, level)

        elif response.query_result.action.split("-")[1] == "Race":
            param = response.query_result.parameters
            race = param["races"]
            data = getInfoAPI("races", race)
            out = "This race's "
            response.query_result.fulfillment_text += "\n" + write_race_properties(data, out, param)
        elif response.query_result.action.split("-")[1] == "Equipment":
            param = response.query_result.parameters
            equipment = param["equipment"]
            data = getInfoAPI("equipment", equipment)
            out = "This equipment's "
            response.query_result.fulfillment_text += "\n" + write_equipment_properties(data, out, param)
        elif response.query_result.action.split("-")[1] == "Spells":
            param = response.query_result.parameters
            spells = param["spells"]
            data = getInfoAPI("spells", spells)
            out = "This Spells' "
            response.query_result.fulfillment_text += "\n" + write_spell_properties(data, out, param)
        elif response.query_result.action.split("-")[1] == "Traits":
            param = response.query_result.parameters
            features = param["features"]
            data = getInfoAPI("features", features)
            out = "This Trait's "
            response.query_result.fulfillment_text += write_trait_properties(data, out, param)
        elif response.query_result.action.split("-")[1] == "Features":
            param = response.query_result.parameters
            traits = param["traits"]
            data = getInfoAPI("traits", traits)
            out = "This Trait's "
            response.query_result.fulfillment_text += write_features_properties(data, out, param)

    elif intent == "create - stats":
        print("Adding stats")
        todo = response.query_result.parameters['cosesafer']
        if "yes" in response.query_result.query_text:
            rollCharacterStats(response, username)
        elif "no" in response.query_result.query_text:
            addCharacterStats(response, username)
        elif todo == "combat":
            rollCharacterStats(response, username)
        else:
            addCharacterStats(response, username)
    else:
        try:
            if intent == "create":
                print("create")
                createCharacter(response, username)
            if "Modify" in intent:
                print("edit")
                editCharacter(response, username)
            if intent == "InfoCharacter":
                print("info of users characters")
                infoCharacter(response, username)
            if intent == "Rolls":
                print("combat")
                rollData(response, username)
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


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
text_handler = MessageHandler(Filters.text & (~Filters.command), textMessage)
dispatcher.add_handler(text_handler)
updater.idle()
# updater.stop()
