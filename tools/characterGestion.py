import json
import os
import random
from tools.autoProperties import *

def createCharacter(response, username):
    param = response.query_result.parameters
    if param['name'] != "":
        if os.path.exists('usersdata/{}.json'.format(username)):
            print("User already has a data.")
            with open('usersdata/{}.json'.format(username), 'r') as f:
                data = json.load(f)
                chara = None
                #try:
                for chars in data:
                    if chars['name'] == param['name'] or chars['name'].lower() == param['name'].lower():
                        chara = chars
                        newChar = 0
                        break
                if chara is None:
                    newChar = 1
                    with open('characterTemplate.json', 'r') as temp:
                        template = json.load(temp)
                        chara = template[0]
                chara['name'] = param['name']
                chara['level'] = int(param['level'])
                if chara['level'] > 20:
                    chara['level'] = 20
                    response.query_result.fulfillment_text += "\nThe level was assigned 20 being that the maximum.\n"
                chara['races'] = param['races']
                chara['subraces'] = param['subraces']
                chara['classes'] = param['classes']
                chara['subclasses'] = param['subclasses']
                langs = []
                for lang in param['languages'].values:
                    langs.append(lang.string_value)
                chara['languages'] = langs
                if newChar == 1:
                    data.insert(0, chara)
                #except:
                #    print("Some value was wrong")
            with open('usersdata/{}.json'.format(username), 'w+') as f:
                json.dump(data, f, indent=4)
        else:
            print("User doesn't have a data, creating a new one")
            with open('characterTemplate.json', 'r') as f:
                data = json.load(f)
                chara = data[0]
                chara['name'] = param['name']
                chara['level'] = int(param['level'])
                if chara['level'] > 20:
                    chara['level'] = 20
                    response.query_result.fulfillment_text += "\nThe level was assigned 20 being that the maximum.\n"
                chara['races'] = param['races']
                chara['subraces'] = param['subraces']
                chara['classes'] = param['classes']
                chara['subclasses'] = param['subclasses']
                langs = []
                for lang in param['languages'].values:
                    langs.append(lang.string_value)
                chara['languages'] = langs
            with open('usersdata/{}.json'.format(username), 'w+') as f:
                json.dump(data, f, indent=4)


def addCharacterStats(response, username):
    with open('usersdata/{}.json'.format(username), 'r') as f:
        data = json.load(f)
        chara = None
        for cont in response.query_result.output_contexts:
            if "create-followup" in cont.name:
                context = cont.parameters
                break
        param = response.query_result.parameters
        for chars in data:
            if chars['name'] == context['name'] or chars['name'].lower() == context['name'].lower():
                chara = chars
                break
        #try:
        response.query_result.fulfillment_text = ""
        num = []
        for val in param['value'].values:
            num.append(val.number_value)
        i = 0
        for stat in param['stats'].values:
            chara['stats'][stat.string_value.lower()] = num[i]
            if num[i] > 20:
                chara['stats'][stat.string_value.lower()] = 20
                response.query_result.fulfillment_text += "\nThe {} was assigned 20 being that the maximum.\n".format(stat.string_value)
            i += 1
            if i >= len(num):
                i -= 1
        nextStat = ""
        for stat in list(chara['stats'].keys()):
            if chara['stats'][stat] == 0 and nextStat == "":
                print(nextStat)
                nextStat = stat
        if nextStat != "":
            response.query_result.fulfillment_text += "{} {}".format(response.query_result.fulfillment_text,
                                                                    nextStat)
        else:
            skillsAndSTCreation(chara)
            lifeCalculator(chara)
            response.query_result.fulfillment_text += "That's it, all the stats have been introduced!"
        #except:
        #    print("Some value was wrong")
    with open('usersdata/{}.json'.format(username), 'w+') as f:
        json.dump(data, f, indent=4)


def rollCharacterStats(response, username):
    with open('usersdata/{}.json'.format(username), 'r') as f:
        data = json.load(f)
        for cont in response.query_result.output_contexts:
            if "create-followup" in cont.name:
                context = cont.parameters
        response.query_result.fulfillment_text = "Here are your character stats:"
        for chars in data:
            if chars['name'] == context['name'] or chars['name'].lower() == context['name'].lower():
                chara = chars
                break
        for stat in list(chara['stats'].keys()):
            chara['stats'][stat] = int(random.randrange(3, 18))
            response.query_result.fulfillment_text += "\n\t\t{} = {}".format(stat.capitalize(), chara['stats'][stat])
        skillsAndSTCreation(chara)
        lifeCalculator(chara)
    with open('usersdata/{}.json'.format(username), 'w+') as f:
        json.dump(data, f, indent=4)


def infoCharacter(response, username):
    # to get the most recent added character gets the first one in the json list
    with open('usersdata/{}.json'.format(username), 'r') as f:
        data = json.load(f)
        chara = None
        param = response.query_result.parameters
        if param['userInfo'] == "character":
            response.query_result.fulfillment_text = "Here you have your characters:"
            for chars in data:
                response.query_result.fulfillment_text += "\n\t\t{}".format(chars['name'])
        if param['name'] == "":
            chara = data[0]
        else:
            for chars in data:
                if chars['name'] == param['name'] or chars['name'].lower() == param['name'].lower():
                    chara = chars
                    break
        if chara is not None:
            if param['properties'] != "":
                response.query_result.fulfillment_text += "\n{}\'s {}:".format(chara['name'], param['properties'])
                if param['properties'] == "skills" or param['properties'] == "saving_throws":
                    for sk in list(chara[param['properties'].lower()].keys()):
                        response.query_result.fulfillment_text += "\n\t\t{} = {}".format(sk.capitalize(), chara[param['properties'].lower()][sk])
                else:
                    # get info from spells, equipment, inventory, languages and proficiencies as list
                    if isinstance(chara[param['properties'].lower()], list):
                        for x in chara[param['properties'].lower()]:
                            response.query_result.fulfillment_text += "\n\t\t{}".format(x)
                    else:
                        response.query_result.fulfillment_text += "\t{}".format(chara[param['properties'].lower()])
            else:
                if param['stats'] != "":
                    if param['stats'] == "stats":
                        response.query_result.fulfillment_text += "\n{}\'s {}:".format(chara['name'], param['stats'])
                        for stat in list(chara['stats'].keys()):
                            response.query_result.fulfillment_text += "\n\t\t{} = {}".format(stat.capitalize(), chara['stats'][stat])
                    else:
                        response.query_result.fulfillment_text += "\n{}\'s {}:\t{}".format(chara['name'], param['stats'], chara['stats'][param['stats'].lower()])
        else:
            response.query_result.fulfillment_text = "Oops it seems you don't have the {} character added.".format(
                param['name'])


def editCharacter(response, username):
    with open('usersdata/{}.json'.format(username), 'r') as f:
        data = json.load(f)
        chara = None
        param = response.query_result.parameters
        if param['name'] == "":
            chara = data[0]
        else:
            for chars in data:
                if chars['name'] == param['name'] or chars['name'].lower() == param['name'].lower():
                    chara = chars
                    break
        if chara is not None:
            intent = response.query_result.intent.display_name
            print(intent)
            if intent != "Modify":
                if intent.split(" - ")[0] == "Modify":
                    if intent.split(" - ")[1] == "properties":
                        if isinstance(chara[param['properties'].lower()], list):
                            chara[param['properties'].lower()].append(param[param['properties']])
                            skillsAndSTCreation(chara)
                            response.query_result.fulfillment_text = "Added {} to {}".format(param[param['properties']], param['properties'])
                        else:
                            response.query_result.fulfillment_text = "Previous {} {},".format(param['properties'], chara[param['properties'].lower()])
                            chara[param['properties'].lower()] = param[param['properties']]
                            skillsAndSTCreation(chara)
                            lifeCalculator(chara)
                            response.query_result.fulfillment_text += " changed to {}".format(param[param['properties']])
                    elif intent.split(" - ")[1] == "equipment":
                        chara['equipment'].append(param['equipment'])
                        response.query_result.fulfillment_text = "{} added to equipment.".format(param['equipment'])
                    elif intent.split(" - ")[1] == "stats":
                        response.query_result.fulfillment_text = "Previous {} value {},".format(param['stats'].lower(), chara['stats'][param['stats'].lower()])
                        chara['stats'][param['stats'].lower()] = int(param['number'])
                        if chara['stats'][param['stats'].lower()] > 20:
                            chara['stats'][param['stats'].lower()] = 20
                        skillsAndSTCreation(chara)
                        lifeCalculator(chara)
                        response.query_result.fulfillment_text += " changed to {}".format(param['number'])
                    elif intent.split(" - ")[1] == "level":
                        chara[param['properties'].lower()] = int(param['level'])
                        if chara['level'] > 20:
                            chara['level'] = 20
                        skillsAndSTCreation(chara)
                        lifeCalculator(chara)
                        response.query_result.fulfillment_text = "Previous level {},".format(chara['level'])
                        response.query_result.fulfillment_text += " changed to {}".format(param['number'])
                    elif intent.split(" - ")[1] == "races":
                        response.query_result.fulfillment_text = "Previous race {},".format(chara['races'])
                        chara['races'] = param['races']
                        response.query_result.fulfillment_text += " changed to {}".format(param['races'])
                    elif intent.split(" - ")[1] == "spells":
                        chara['spells'].append(param['spells'])
                        response.query_result.fulfillment_text = "{} added to spells.".format(param['spells'])
                    elif intent.split(" - ")[1] == "subclasses":
                        response.query_result.fulfillment_text = "Previous subclass {},".format(chara['subclasses'])
                        chara['subclasses'] = param['subclasses']
                        response.query_result.fulfillment_text += " changed to {}".format(param['subclasses'])
                    elif intent.split(" - ")[1] == "subraces":
                        response.query_result.fulfillment_text = "Previous subrace {},".format(chara['subraces'])
                        chara['subraces'] = param['subraces']
                        response.query_result.fulfillment_text += " changed to {}".format(param['subraces'])
                    elif intent.split(" - ")[1] == "inventory":
                        chara['inventory'].append(param['inventory'])
                        response.query_result.fulfillment_text = "{} added to inventory.".format(param['inventory'])
                    elif intent.split(" - ")[1] == "languages":
                        chara['languages'].append(param['languages'])
                        response.query_result.fulfillment_text = "{} added to languages.".format(param['languages'])
                    elif intent.split(" - ")[1] == "classes":
                        response.query_result.fulfillment_text = "Previous class {},".format(chara['classes'])
                        chara['classes'] = param['classes']
                        skillsAndSTCreation(chara)
                        lifeCalculator(chara)
                        response.query_result.fulfillment_text += " changed to {}".format(param['classes'])
                    elif intent.split(" - ")[1] == "proficiencies":
                        chara['proficiencies'].append(param['proficiencies'])
                        skillsAndSTCreation(chara)
                        response.query_result.fulfillment_text = "{} added to proficiencies.".format(param['proficiencies'])
                    elif intent.split(" - ")[1] == "name":
                        response.query_result.fulfillment_text = "Previous name {},".format(chara['name'])
                        chara['name'] = param['newname']
                        response.query_result.fulfillment_text += " changed to {}".format(param['newname'])
                    with open('usersdata/{}.json'.format(username), 'w+') as fm:
                        json.dump(data, fm, indent=4)
                else:
                    response.query_result.fulfillment_text = "Sorry I can't do that."
                    pass
        else:
            response.query_result.fulfillment_text = "Oops it seems you don't have the {} character added.".format(
                param['name'])


def rollData(response, username):
    # to get the most recent added character gets the first one in the json list
    with open('usersdata/{}.json'.format(username), 'r') as f:
        data = json.load(f)
        chara = None
        param = response.query_result.parameters
        if param['name'] == "":
            chara = data[0]
        else:
            for chars in data:
                if chars['name'] == param['name'] or chars['name'].lower() == param['name'].lower():
                    chara = chars
                    break
        if chara is not None:
            i = 0
            for pro in param['properties']:
                if pro == "saving_throws":
                    i = 1
                    break
                elif pro == "skills":
                    i = 2
                    break
                elif pro == "initiative":
                    i = 3
                    break
                elif pro == "attack":
                    i = 4
                    break

            if i == 0:
                dice = random.randrange(1, 20)
                valor = int((chara['stats'][param['stats'].lower()]-10)/2)

                response.query_result.fulfillment_text += "\nRolled {}: {}".format(param['stats'], dice + valor)
            elif i == 1:
                dice = random.randrange(1, 20)
                if dice >= 10 and dice != 20:
                    response.query_result.fulfillment_text += "\nRolled +1 saved point"
                elif dice < 10:
                    val = 1
                    if dice == 1:
                        val = 2
                    response.query_result.fulfillment_text += "\nRolled -{} failed points".format(val)
                else:
                    response.query_result.fulfillment_text += "\nRolled 20 and you are saved!"
            elif i == 2:
                dice = random.randrange(1, 20)
                valor = int((chara['skills'][param['skills'].lower()]-10)/2)
                response.query_result.fulfillment_text += "\nRolled {}: {}".format(param['skills'], dice + valor)
            elif i == 3:
                dice = random.randrange(1, 20)
                valor = int((chara['stats']['dexterity']-10)/2)
                response.query_result.fulfillment_text += "\nRolled: {}".format(dice + valor)
            elif i == 4:
                if param['equipment'] == "":
                    dice = random.randrange(1, 20)
                    valor = int((chara['stats']['strength']-10)/2)
                    response.query_result.fulfillment_text += "\nRolled impact: {}".format(dice + valor)
                    dice = 1
                    valor = int((chara['stats']['strength']-10)/2)
                    response.query_result.fulfillment_text += "\nRolled damage: {}".format(dice + valor)
                else:
                    dice = random.randrange(1, 20)
                    valor = int((chara['stats']['strength']-10)/2)
                    response.query_result.fulfillment_text += "\nRolled impact: {}".format(dice + valor)
                    data = getInfoAPI("equipment", param['equipment'])
                    dice = random.randrange(1, int(data['damage']['damage_dice'][2]))
                    valor = int((chara['stats']['strength']-10)/2)
                    response.query_result.fulfillment_text += "\nRolled damage: {}".format(dice + valor)

        else:
            response.query_result.fulfillment_text = "Oops it seems you don't have the {} character added.".format(
                param['name'])
