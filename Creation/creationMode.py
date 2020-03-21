import json

from random import random

from Json import *


def create_char():
    isRight = 0
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
    while isRight==0:
        print("So, what about your stats?\n"
              "a)Roll them now!\n"
              "b)Let me set those\n")
        choice = input()
        if choice == "a":
            isRight = 1
            chara.stats = Stats( random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18),
                                       random.randrange(3,18))
            
            chara.saving_throws = Stats(int((chara.stats.strength-10)/2),
                                        int((chara.stats.dexterity - 10) / 2),
                                        int((chara.stats.constitution - 10) / 2),
                                        int((chara.stats.intelligence - 10) / 2),
                                        int((chara.stats.wisdom - 10) / 2),
                                        int((chara.stats.charisma - 10) / 2))

            pass
        elif choice == "b":
            isRight = 1
            print("Strength:")
            chara.stats.strength = int(input())
            print("Dexterity:")
            chara.stats.dexterity = int(input())
            print("Constitution:")
            chara.stats.constitution = int(input())
            print("Intelligence:")
            chara.stats.intelligence = int(input())
            print("Wisdom:")
            chara.stats.wisdom = int(input())
            print("Charisma")
            chara.stats.charisma = int(input())
            chara.saving_throws = Stats(int((chara.stats.strength-10)/2),
                                        int((chara.stats.dexterity - 10) / 2),
                                        int((chara.stats.constitution - 10) / 2),
                                        int((chara.stats.intelligence - 10) / 2),
                                        int((chara.stats.wisdom - 10) / 2),
                                        int((chara.stats.charisma - 10) / 2))

            isright = 1
            pass
        else:
            isright = 0
            print("That's not a valid choice, my friend!\n")

    isRight = 0
    #Comprobar que level sigui vàlid
    while  isRight==0:
        print("At what level should we start?\n")
        level = int(input())
        isRight = 1
        chara.level = level
        if  (level >= 20) or (level <= 1):
            print("That's not a valid level, my friend!\n")
            isRight = 0

    isRight = 0
    while isRight == 0:
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

    isRight = 0
    while isRight == 0:
        print("Do you want to input a description? Y/N\n")
        answer = input()
        if answer == "Y":
            isRight = 1
            print("Let's see it!\n")
            description = input()
            chara.description = description
            pass
        elif answer == "N":
            isRight = 1
            print("That's fine, too!")
            pass
        else:
            isRight=0
            print("Not a valid answer, friend!\n")

    #TODO: Escribir el nuevo PJ en el JSON
    with open('chara.json', 'r') as myfile:
        data = myfile.read()
    characters = characters_from_dict(json.loads(data))
    characters.append(chara)
    #characters_to_dict(characters)
    json.dump(characters)