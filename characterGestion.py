import json
import os
import random


def createCharacter(response, username):
    param = response.query_result.parameters
    if param['name'] != "":
        if os.path.exists("{}.json".format(username)):
            print("User already has a data.")
            with open("{}.json".format(username), 'r') as f:
                data = json.load(f)
                chara = None
                try:
                    for chars in data:
                        if chars['name'] == param['name']:
                            chara = chars
                            newChar = 0
                    if chara is None:
                        newChar = 1
                        with open('characterTemplate.json', 'r') as temp:
                            template = json.load(temp)
                            chara = template[0]
                    chara['name'] = param['name']
                    chara['level'] = param['level']
                    chara['race'] = param['Races']
                    chara['subrace'] = param['Subraces']
                    chara['class'] = param['Classes']
                    chara['subclass'] = param['Subclasses']
                    langs = []
                    for lang in param['Languages'].values:
                        langs.append(lang.string_value)
                    chara['languages'] = langs
                    if newChar == 1:
                        data.insert(1, chara)
                except:
                    pass
            with open("{}.json".format(username), 'w+') as f:
                json.dump(data, f, indent=4)
        else:
            print("User doesn't have a data, creating a new one")
            with open('characterTemplate.json', 'r') as f:
                data = json.load(f)
                chara = data[0]
                chara['name'] = param['name']
                chara['level'] = param['level']
                chara['race'] = param['Races']
                chara['subrace'] = param['Subraces']
                chara['class'] = param['Classes']
                chara['subclass'] = param['Subclasses']
                langs = []
                for lang in param['Languages'].values:
                    langs.append(lang.string_value)
                chara['languages'] = langs
            with open("{}.json".format(username), 'w+') as f:
                json.dump(data, f, indent=4)


def addCharacterStats(response, username):
    with open("{}.json".format(username), 'r') as f:
        data = json.load(f)
        chara = None
        context = response.query_result.output_contexts[0].parameters
        param = response.query_result.parameters
        for chars in data:
            if chars['name'] == context['name']:
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
    with open("{}.json".format(username), 'w+') as f:
        json.dump(data, f, indent=4)


def rollCharacterStats(response, username):
    with open("{}.json".format(username), 'r') as f:
        data = json.load(f)
        context = response.query_result.output_contexts[0].parameters
        response.query_result.fulfillment_text = "Here are your character stats:"
        for chars in data:
            if chars['name'] == context['name']:
                chara = chars
        for stat in list(chara['stats'].keys()):
            chara['stats'][stat] = random.randrange(3, 18)
            response.query_result.fulfillment_text += "\n\t\t{} = {}".format(stat.capitalize(), chara['stats'][stat])

    with open("{}.json".format(username), 'w+') as f:
        json.dump(data, f, indent=4)


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
