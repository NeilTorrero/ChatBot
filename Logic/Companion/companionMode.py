import json
import random
import re
import time

import Json
from Logic.Creation.creationMode import create_char
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
        if name.lower() == character.name.lower():
            found = True
            found_character = character
    return [found, found_character]


def use_spell_feat(character):
    spell_list = character.spells
    if len(spell_list) != 0:
        print("What spell is going to be cast?")
        print("Character spells:")
        for spell in spell_list:
            print("-" + spell.name)
        found = False
        while not found:
            name = input()
            spell_selected = Json.Spell
            for spell in spell_list:
                if name.lower() == spell.name.lower():
                    found = True
                    spell_selected = spell
            if found:
                print("Rolling a " + spell_selected.damage + "...")
                dvalue = spell_selected.damage[2:None]
                dice = random.randrange(1, int(dvalue))
                time.sleep(1)
                print("The dice choose: " + str(dice))
            else:
                print("Your character doesn't have that spell.")
                print("Please enter a spell your character has.")
    else:
        print("You either have no spells or you are not a spellcaster Harry.")


def roll_attack(character):
    attack_list = character.equipment
    if len(attack_list) != 0:
        print("What attack are you going to do?")
        print("Character equipment:")
        for attack in attack_list:
            print("-" + attack.name)
        found = False
        while not found:
            name = input()
            attack_selected = Json.Equipment
            for attack in attack_list:
                if name.lower() == attack.name.lower():
                    found = True
                    attack_selected = attack
            if found:
                print("Rolling a " + attack_selected.damage + "...")
                dvalue = attack_selected.damage[2:None]
                dice = random.randrange(1, int(dvalue))
                time.sleep(1)
                print("The dice choose: " + str(dice))
            else:
                print("Your character doesn't have that attack.")
                print("Please enter a attack your character has.")
    else:
        print("You don't have equipment.")


def roll_skill(character):
    skill_list = character.skills
    if len(skill_list) != 0:
        print("What skill are you going to use?")
        print("Character skills:")
        for skill in skill_list:
            print("-" + skill)
        found = False
        while not found:
            name = input()
            skill_selected = 0
            for skill in skill_list:
                if name.lower() == skill.lower():
                    found = True
                    skill_selected = skill
            if found:
                print("Rolling a 1d20...")
                dice = random.randrange(1, 20)
                time.sleep(1)
                print("The dice choose: " + str(dice))
                fvalue = dice + skill_list[skill_selected]
                print("The final value is the dice + skill = " + str(fvalue))
            else:
                print("Your character doesn't have that skill.")
                print("Please enter a skill your character has.")
    else:
        print("You don't have skills.")


def dice_roll(character):
    print("What kind of roll you want to do?")
    kind = input()
    string = re.compile("(attack|skill|dc)", re.IGNORECASE)
    result = string.match(kind)
    if result:
        string = re.compile("(attack)", re.IGNORECASE)
        result = string.match(kind)
        if result:
            roll_attack(character)
        string = re.compile("(skill|dc)", re.IGNORECASE)
        result = string.match(kind)
        if result:
            roll_skill(character)
    else:
        print("Sorry but I don't have that rolling option.")


def companion_mode():
    print("Please select your character:")
    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    # JSON get characters
    theres_character = False
    while not theres_character:
        [theres_character, found_character] = character_selection(characters)
        if theres_character:
            back = True
            while back:
                print("What do you need?")
                print("- Use a spell or feature?")
                print("- Do dice rolls?")
                print("- Or go back to some of the other functionalities?")
                need = input()
                string = re.compile("(dice|roll|rolls|feature|spell|other|functionalities|back|return|exit)", re.IGNORECASE)
                result = string.match(need)
                if result:
                    string = re.compile("(dice|roll|rolls)", re.IGNORECASE)
                    result = string.match(need)
                    if result:
                        dice_roll(found_character)

                    string = re.compile("(feature|spell)", re.IGNORECASE)
                    result = string.match(need)
                    if result:
                        use_spell_feat(found_character)

                    string = re.compile("(other|functionalities|back|return|exit)", re.IGNORECASE)
                    result = string.match(need)
                    if result:
                        back = False
                else:
                    print("Sorry but I don't have that option.")
                    print("Please choose one of the options I have offered to you.")
        else:
            print("That character doesnt exist.")
            print("Do want to create one?")
            need = input()
            string = re.compile("(yes|ok|create)", re.IGNORECASE)
            result = string.match(need)
            if result:
                create_char()
            else:
                print("Then choose one that already exists.")
