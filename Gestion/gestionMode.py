import json
import random
import re
import time

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
    if theres_character:
        print(found_character.name)
        back = True
        random.seed(None, 2)
        while back:
            print("What do yo need?")
            print("1- Open editable sheet")
            print("2- Level Up")
            need = input()
            result = re.match(need, "1", re.IGNORECASE)
            if result:
                webbrowser.open_new(r'5E_CharacterSheet_Fillable.pdf')
                break

            result = re.match(need, "2", re.IGNORECASE)
            if result:
                x = input("Select posible next level: ")
                if found_character.character_class == 'Barbarian':
                    dice = random.randrange(1, 12)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Bard':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Cleric':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Druid':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Fighter':
                    dice = random.randrange(1, 10)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Monk':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Paladin':
                    dice = random.randrange(1, 10)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Ranger':
                    dice = random.randrange(1, 10)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Rogue':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Sorcerer':
                    dice = random.randrange(1, 6)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Warlock':
                    dice = random.randrange(1, 8)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)

                if found_character.character_class == 'Wizard':
                    dice = random.randrange(1, 6)
                    print('Rolling dice...')
                    time.sleep(1)
                    print(dice)
    else:
        create_char()

    return 0

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
