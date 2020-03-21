import json

from random import random

from Json import *


def create_char():
    isRight = 1
    #TODO Crear nuevo pesonaje (new Character) e ir llenando
    with open('characterTemplate.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    chara = characters[0]

    print("Welcome, please choose your Race!\n")
    Race = input()
    chara.race = Race
    #Comprobar que Race sigui vàlida
    print("Interesting! What about your class?\n")
    Class = input()
    chara.character_class = Class
    while isRight==1:
        print("So, what about your stats?\n"
              "a)Roll them now!\n"
              "b)Let me set those\n")
        choice = input()
        if choice == "a":
            isright = 1
            chara.stats = SavingThrow( random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18))
            chara.saving_throws = SavingThrow((chara.stats.strength-10)/2,
                                              (chara.stats.dexterity - 10) / 2,
                                              (chara.stats.constitution - 10) / 2,
                                              (chara.stats.intelligence - 10) / 2,
                                              (chara.stats.wisdom - 10) / 2,
                                              (chara.stats.charisma - 10) / 2)

            pass
        elif choice == "b":
            print("Strength:")
            chara.stats[0] = input()
            print("Dexterity:")
            chara.stats[1] = input()
            print("Constitution:")
            chara.stats[2] = input()
            print("Intelligence:")
            chara.stats[3] = input()
            print("Wisdom:")
            chara.stats[4] = input()
            print("Charisma")
            chara.stats[5] = input()
            chara.saving_throws = SavingThrow((chara.stats[0]-10)/2,
                                              (chara.stats[1] - 10) / 2,
                                              (chara.stats[2] - 10) / 2,
                                              (chara.stats[3] - 10) / 2,
                                              (chara.stats[4] - 10) / 2,
                                              (chara.stats[5] - 10) / 2)



            isright = 1
            pass
        else:
            isright = 0
            print("That's not a valid choice, my friend!\n")

    isRight = 1
    #Comprobar que level sigui vàlid
    while  isRight==1:
        print("At what level should we start?\n")
        level = input()
        chara.level = level
        if  (level <= 20) or (level >= 1):
            print("That's not a valid level, my friend!\n")
            isRight = 0

    isRight = 1
    while isRight == 1:
        print("Well then, it's time to choose your background now!\n"
              "a)Scholar!\n"
              "b)Slave\n"
              "C)Soldier")
        background = input()
        chara.background = background
        if background >= "a" or background <= "b":
            isRight = 1
        else:
            isRight = 0
            print("That's not a valid choice, my friend!\n")
    isRight = 1;
    while isRight == 1:
        print("Do you want to input a description? Y/N\n")
        answer = input();
        if answer == "Y":
            print("Let's see it!\n")
            description = input()
            chara.description = description
            pass
        elif answer == "N":
            print("That's fine, too!")
            pass
        else:
            isRight=0
            print("Not a valid answer, friend!\n")

    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    characters.append(chara)