import json

import Json
from Json import characters_from_dict


def character_selection(characters: Json):
    # Selection of characters from saved if none go to creationMode
    print("Characters:")
    # return character
    for character in characters:
        print(character.name)
    print("Which character do you want?")
    name = input()
    for character in characters:
        if name == character.name:
            return character


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
    character = character_selection(characters)

    back = False
    while back:
        n = Need()
        back = n.switch("create")
