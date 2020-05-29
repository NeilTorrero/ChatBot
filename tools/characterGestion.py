import json
import os
import random


def createCharacter(response, username):
    param = response.query_result.parameters
    if param['name'] != "":
        if os.path.exists("users_data/{}.json".format(username)):
            print("User already has a data.")
            with open("users_data/{}.json".format(username), 'r') as f:
                data = json.load(f)
                chara = None
                try:
                    for chars in data:
                        if chars['name'] == param['name'] or chars['name'] == param['name'].capitalize():
                            chara = chars
                            newChar = 0
                    if chara is None:
                        newChar = 1
                        with open('../characterTemplate.json', 'r') as temp:
                            template = json.load(temp)
                            chara = template[0]
                    chara['name'] = param['name']
                    chara['level'] = param['level']
                    chara['race'] = param['races']
                    chara['subrace'] = param['subraces']
                    chara['class'] = param['classes']
                    chara['subclass'] = param['subclasses']
                    langs = []
                    for lang in param['languages'].values:
                        langs.append(lang.string_value)
                    chara['languages'] = langs
                    if newChar == 1:
                        data.insert(0, chara)
                except:
                    pass
            with open("users_data/{}.json".format(username), 'w+') as f:
                json.dump(data, f, indent=4)
        else:
            print("User doesn't have a data, creating a new one")
            with open('../characterTemplate.json', 'r') as f:
                data = json.load(f)
                chara = data[0]
                chara['name'] = param['name']
                chara['level'] = param['level']
                chara['race'] = param['Races']
                chara['subrace'] = param['subraces']
                chara['class'] = param['classes']
                chara['subclass'] = param['subclasses']
                langs = []
                for lang in param['languages'].values:
                    langs.append(lang.string_value)
                chara['languages'] = langs
            with open("users_data/{}.json".format(username), 'w+') as f:
                json.dump(data, f, indent=4)


def addCharacterStats(response, username):
    with open("users_data/{}.json".format(username), 'r') as f:
        data = json.load(f)
        chara = None
        context = response.query_result.output_contexts[0].parameters
        param = response.query_result.parameters
        for chars in data:
            if chars['name'] == context['name'] or chars['name'] == param['name'].capitalize():
                chara = chars
        try:
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
    with open("users_data/{}.json".format(username), 'w+') as f:
        json.dump(data, f, indent=4)


def rollCharacterStats(response, username):
    with open("users_data/{}.json".format(username), 'r') as f:
        data = json.load(f)
        context = response.query_result.output_contexts[0].parameters
        response.query_result.fulfillment_text = "Here are your character stats:"
        for chars in data:
            if chars['name'] == context['name'] or chars['name'] == context['name'].capitalize():
                chara = chars
        for stat in list(chara['stats'].keys()):
            chara['stats'][stat] = random.randrange(3, 18)
            response.query_result.fulfillment_text += "\n\t\t{} = {}".format(stat.capitalize(), chara['stats'][stat])

    with open("users_data/{}.json".format(username), 'w+') as f:
        json.dump(data, f, indent=4)


def infoCharacter(response, username):
    # TODO(now only shows info of primary info like level, name , class, simple 1-1 properties)
    # to get the most recent added character gets the first one in the json list
    with open("users_data/{}.json".format(username), 'r') as f:
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
                if chars['name'] == param['name'] or chars['name'] == param['name'].capitalize():
                    chara = chars
        if chara is not None:
            response.query_result.fulfillment_text += "\n{}\'s {}:\t{}".format(chara['name'], param['properties'],
                                                                               chara[param['properties'].lower()])
        else:
            response.query_result.fulfillment_text = "Ups it seems you don't have the {} character added.".format(
                param['name'])


def editCharacter(response, username):
    with open("users_data/{}.json".format(username), 'r') as f:
        data = json.load(f)
        chara = None
        param = response.query_result.parameters
        if param['name'] == "":
            chara = data[0]
        else:
            for chars in data:
                if chars['name'] == param['name'] or chars['name'] == param['name'].capitalize():
                    chara = chars
        if chara is not None:
            intent = response.query_result.intent.display_name
            print(intent)
            if intent != "Modify":
                if intent.split(" - ")[0] == "Modify":
                    if intent.split(" - ")[1] == "properties":
                        chara[param['properties']] = param[param['properties']]
                        response.query_result.fulfillment_text = "properties"
                    elif intent.split(" - ")[1] == "equipment":
                        print("edit equipment")
                        response.query_result.fulfillment_text = "equip"
                    elif intent.split(" - ")[1] == "stats":
                        chara[param['stats']] = param['number']
                        response.query_result.fulfillment_text = "stats"
                    elif intent.split(" - ")[1] == "level":
                        chara[param['properties']] = param['level']
                        print("yey")
                        response.query_result.fulfillment_text = "level"
                    elif intent.split(" - ")[1] == "raw":
                        print("edit on dynamic info")
                        response.query_result.fulfillment_text = "raw"
                    with open("users_data/{}.json".format(username), 'w+') as fm:
                        json.dump(data, fm, indent=4)
                else:
                    response.query_result.fulfillment_text = "pass"
                    pass
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
