import json
import os


def createCharacter(response, username):
    if os.path.exists("{}.json".format(username)):
        print("User already has a data.")
        with open("{}.json".format(username), 'r') as f:
            data = json.load(f)
            chara = None
            param = response.query_result.parameters
            try:
                for chars in data:
                    if chars['name'] == param['name']:
                        chara = chars
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
            except:
                pass
        with open("{}.json".format(username), 'w+') as f:
            json.dump(data, f, indent=4)
    else:
        print("User doesn't have a data, creating a new one")
        with open('characterTemplate.json', 'r') as f:
            data = json.load(f)
            chara = data[0]
            param = response.query_result.parameters
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
                response.query_result.fulfillment_text = "{} {}".format(response.query_result.fulfillment_text,nextStat)
            else:
                response.query_result.fulfillment_text = "That's all the stats introduced!"
        except:
            response.query_result.fulfillment_text = "{} Strength".format(response.query_result.fulfillment_text)
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
