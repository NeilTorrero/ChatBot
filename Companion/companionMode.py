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
    string = re.compile("(attack|skill|dc)", re.IGNORECASE)
    result = string.match(kind)
    if result:
        string = re.compile("(attack)", re.IGNORECASE)
        result = string.match(kind)
        if result:
            print("roll attack")
        string = re.compile("(skill|dc)", re.IGNORECASE)
        result = string.match(kind)
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
    if theres_character:
        print("What do you need?")
        print("- Use a spell or feature?")
        print("- Do dice rolls?")
        print("- Or go back to some of the other functionalities?")
        back = True
        while back:
            need = input()
            string = re.compile("(dice|feature|spell|other|functionalities|back|return|exit)", re.IGNORECASE)
            result = string.match(need)
            if result:
                string = re.compile("(dice)", re.IGNORECASE)
                result = string.match(need)
                if result:
                    dice_roll()

                string = re.compile("(feature|spell)", re.IGNORECASE)
                result = string.match(need)
                if result:
                    use_spell_feat()

                string = re.compile("(other|functionalities|back|return|exit)", re.IGNORECASE)
                result = string.match(need)
                if result:
                    back = False
            else:
                print("Sorry but I don't have that option.")
                print("Please choose one of the options I have offered to you.")
    else:
        create_char()
