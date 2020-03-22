import re

from Companion.companionMode import companion_mode
from Creation.creationMode import create_char
from Gestion.gestionMode import gestion_mode

print("Hello, I'm MattBot.")
print("What do you need for today's game?")
while True:
    print(" - Character creation")
    print(" - Character gestion")
    print(" - Companion mode")
    mode = input()
    result = re.match(mode, "create|create", re.IGNORECASE)
    if result:
        create_char()

    result = re.match(mode, "gestion", re.IGNORECASE)
    if result:
        gestion_mode()

    result = re.match(mode, "companion", re.IGNORECASE)
    if result:
        companion_mode()
    print("\nAnything else?")