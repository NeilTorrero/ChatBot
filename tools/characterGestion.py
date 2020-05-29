import json
import os
import random


def createCharacter(response, username):
    param = response.query_result.parameters
    if param['name'] != "":
        if os.path.exists('usersdata/{}.json'.format(username)):
            print("User already has a data.")
            with open('usersdata/{}.json'.format(username), 'r') as f:
                data = json.load(f)
                chara = None
                try:
                    for chars in data:
                        if chars['name'] == param['name'] or chars['name'].lower() == param['name'].lower():
                            chara = chars
                            newChar = 0
                    if chara is None:
                        newChar = 1
                        with open('characterTemplate.json', 'r') as temp:
                            template = json.load(temp)
                            chara = template[0]
                    chara['name'] = param['name']
                    chara['level'] = param['level']
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
                except:
                    pass
            with open('usersdata/{}.json'.format(username), 'w+') as f:
                json.dump(data, f, indent=4)
        else:
            print("User doesn't have a data, creating a new one")
            with open('characterTemplate.json', 'r') as f:
                data = json.load(f)
                chara = data[0]
                chara['name'] = param['name']
                chara['level'] = param['level']
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
        param = response.query_result.parameters
        for chars in data:
            if chars['name'] == context['name'] or chars['name'].lower() == context['name'].lower():
                chara = chars
        try:
            # TODO(accepts multiple stats but only one value)
            # If wants multiple value, change in dialoglow to values to list and control here the order of assigment
            for stat in param['stats'].values:
                chara['stats'][stat.string_value.lower()] = param['value']
            nextStat = ""
            for stat in list(chara['stats'].keys()):
                if chara['stats'][stat] == 0 and nextStat == "":
                    print(nextStat)
                    nextStat = stat
            if nextStat != "":
                response.query_result.fulfillment_text = "{} {}".format(response.query_result.fulfillment_text,
                                                                        nextStat)
            else:
                response.query_result.fulfillment_text = "That's all the stats introduced!"
        except:
            response.query_result.fulfillment_text = "{} Strength".format(response.query_result.fulfillment_text)
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
        for stat in list(chara['stats'].keys()):
            chara['stats'][stat] = random.randrange(3, 18)
            response.query_result.fulfillment_text += "\n\t\t{} = {}".format(stat.capitalize(), chara['stats'][stat])
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
            response.query_result.fulfillment_text = "Ups it seems you don't have the {} character added.".format(
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
        if chara is not None:
            intent = response.query_result.intent.display_name
            print(intent)
            if intent != "Modify":
                # TODO(spells, skills, saving throws, inventory, languages, proficiencies not considered)
                if intent.split(" - ")[0] == "Modify":
                    if intent.split(" - ")[1] == "properties":
                        print(param['properties'])
                        print(param[param['properties']])
                        chara[param['properties'].lower()] = param[param['properties']]
                        response.query_result.fulfillment_text = "properties"
                    elif intent.split(" - ")[1] == "equipment":
                        # TODO (add equipment)
                        print("edit equipment")
                        response.query_result.fulfillment_text = "equip"
                    elif intent.split(" - ")[1] == "stats":
                        response.query_result.fulfillment_text = "Previous {} value {},".format(param['stats'].lower(), chara['stats'][param['stats'].lower()])
                        chara['stats'][param['stats'].lower()] = param['number']
                        response.query_result.fulfillment_text += " changed to {}".format(param['number'])
                    elif intent.split(" - ")[1] == "level":
                        chara[param['properties'].lower()] = param['level']
                        response.query_result.fulfillment_text = "Previous level {},".format(chara['level'])
                        response.query_result.fulfillment_text += " changed to {}".format(param['number'])
                    elif intent.split(" - ")[1] == "raw":
                        # TODO (add info that does no have the properties parameter i only has the name of what to edit)
                        print("edit on dynamic info")
                        response.query_result.fulfillment_text = "raw"
                    with open('usersdata/{}.json'.format(username), 'w+') as fm:
                        json.dump(data, fm, indent=4)
                else:
                    response.query_result.fulfillment_text = "pass"
                    pass
        else:
            response.query_result.fulfillment_text = "Ups it seems you don't have the {} character added.".format(
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
        if chara is not None:
            # TODO (only implemente throws of stats and saving throws)
            i = 0
            for pro in param['properties']:
                if pro == "saving_throws":
                    i = 1
                    break

            if i == 0:
                dice = random.randrange(1, 20)
                valor = int((chara['stats'][param['stats'].lower()]-10)/2)

                response.query_result.fulfillment_text += "\nRolled {}: {}".format(param['stats'], dice + valor)
            else:
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
        else:
            response.query_result.fulfillment_text = "Ups it seems you don't have the {} character added.".format(
                param['name'])


"""
if os.path.exists('test.json'):
    print("yey")
if not os.path.exists('fvrec.json'):
    print("Doesn't exists path: {}\n".format('fvrec.json'))

with open('characterTemplate.json', 'r') as f:
    data = json.load(f)
    chara = data[0]
    chara['name'] = "Juan"
    data.insert(1, chara)

with open('test.json', 'w+') as f:
    json.dump(data, f, indent=4)
"""
