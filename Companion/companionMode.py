import json

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


class Need(object):
    def switch(self, option):
        method_name = 'mode_' + option
        method = getattr(self, method_name, lambda: 'Invalid')
        return method(exit)

    def mode_feat(self):
        use_spell_feat()
        return False

    def mode_dice(self):
        dice_roll()
        return False

    def mode_back(self):
        return True


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
    found_character = Json.Character
    [theres_character, found_character] = character_selection(characters)
    print(found_character.name)
    if theres_character:
        back = False
        while back:
            n = Need()
            back = n.switch("create")
    else:
        create_char()
