import re

from Logic.Companion.companionMode import companion_mode
from Logic.Creation.creationMode import create_char
from Logic.Gestion.gestionMode import gestion_mode
from Visuals.MainView import  *
from Companion.companionMode import companion_mode
from Creation.creationMode import create_char
from Gestion.gestionMode import gestion_mode
from API import getInfoAPI

print("Hello, I'm MattBot.")

#getInfoAPI("spells", "acid-arrow")

active = True

while active:
    m = MainView()
    print("What do you need for today's game?")
    print(" - Character creation")
    print(" - Character gestion")
    print(" - Companion mode")
    m.addMessage(0, "me gustan los bichos rosas")
    m.startGUI()
    mode = input()

    string = re.compile("(create|creation|gestion|edit|companion|goodbye|bye|exit|quit)", re.IGNORECASE)
    result = string.match(mode)
    if result:
        string = re.compile("(create|creation)", re.IGNORECASE)
        result = string.match(mode)
        if result:
            create_char()

        string = re.compile("(gestion|edit)", re.IGNORECASE)
        result = string.match(mode)
        if result:
            gestion_mode()

        string = re.compile("(companion)", re.IGNORECASE)
        result = string.match(mode)
        if result:
            companion_mode()
        string = re.compile("(goodbye|bye|exit|quit)", re.IGNORECASE)
        result = string.match(mode)
        if result:
            active = False
    else:
        print("Sorry but I can't do that")
