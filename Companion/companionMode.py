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
    print("What kind of roll you want to do?")
    kind = input()
    result = re.match(kind, "attack|skill|dc",  re.IGNORECASE)
    if result:
        result = re.match(kind, "attack", re.IGNORECASE)
        if result:
            print("roll attack")
        result = re.match(kind, "skill|dc", re.IGNORECASE)
        if result:
            print("roll skill")
    else:
        print("Sorry but I don't have that rolling option.")


def companion_mode():
    print("Please select your character:")
    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    # JSON get characters
    [theres_character, found_character] = character_selection(characters)
    print(found_character.name)
    print("What do you need?")
    print("Use a spell or feature?")
    print("Do dice rolls?")
    print("Or maybe do some of the other functionalities?")
    if theres_character:
        back = True
        while back:
            need = input()
            result = re.match(need, "dice|feature|spell|back|return|exit", re.IGNORECASE)
            if result:
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
                print("Sorry but I don't have that option.")
                print("Please choose one of the options I have offered to you.")
    else:
        create_char()
