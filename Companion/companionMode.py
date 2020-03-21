import json
import re

import Json
from Creation.creationMode import create_char
from Json import characters_from_dict


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
    return [found, found_character]


def use_spell_feat():
    print("Spell")


def dice_roll():
    print("Dice")


def companion_mode():
    print("Please select your character:")
    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    # JSON get characters
    [theres_character, found_character] = character_selection(characters)
    print(found_character.name)
    if theres_character:
        back = True
        while back:
            need = input()
            result = re.match(need, "dice", re.IGNORECASE)
            if result:
                dice_roll()

            result = re.match(need, "feature|spell", re.IGNORECASE)
            if result:
                use_spell_feat()

            result = re.match(need, "back|return|exit", re.IGNORECASE)
            if result:
                back = False
    else:
        create_char()
