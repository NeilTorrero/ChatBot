import json
import re
import Json
import webbrowser
from Creation.creationMode import create_char
from Json import characters_from_dict


def gestion_mode():
    print("Please select your character:")
    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    # JSON get characters
    [theres_character, found_character] = character_selection(characters)
    print(found_character.name)
    print("What do yo need?")
    print("1- Open editable sheet")
    print("2- Level Up")

    if theres_character:
        back = True
        while back:
            need = input()
            result = re.match(need, "1", re.IGNORECASE)
            if result:
                webbrowser.open_new(r'5E_CharacterSheet_Fillable.pdf')
                break

            result = re.match(need, "2", re.IGNORECASE)
            if result:
                print("Select posible next level")
    else:
        create_char()

def character_selection(characters):
    # Selection of characters from saved if none go to creationMode
    found_character = Json.Character
    print("Characters:")
    # return character
    for character in characters:
        print(character.name)
    print("Which character do you want?")
    name = input()
    found = False
    for character in characters:
        if name == character.name:
            found = True
            found_character = character
            break
    return [found, found_character]
