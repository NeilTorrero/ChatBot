SBC: D&D ChatBot
To start the Bot run the bot.py file.
The bot will start asking what module do you want to enter (create, companion and gestion) and so,
answer the question following the options offered.
The options that are specific names from a list must be answered with the desired one.
	-Races Available: human, dwarf, elf, dragonborn, halfling, gnome
	-Classes Available: fighter, barbarian, bard, wizard, sorcerer, warlock, 
			    druid, cleric, paladin, ranger

# CatBot
Autors Alex Moñux, Neil Torrero, Marc Aynés
Llenguatge usat: Python
Interpret de python: python 3.7
IDE Usat: PyCharm

Importació del projecte:
PyCharm barra superior d'eines -> File -> Open...
Seleccionar la Carpeta ChatBot

En PyCharm, a dalt a la dreta, hi han els botons per executar i debuggar, a l'esquerra d'aquests hi ha la configuració que s'executarà, si en aquest no surt la paraula "bot" escrita fer:
clic en el desplegable -> Edit configuaration
En la pantalla que apareix, a la esquerra veurem un + (add configuration) sortirà un desplegable, seleccionem de tots ells: Python
Un cop seleccionat a la dreta ens apareixera a la dreta unes opcions a omplir, a dal de tot hi ha un quadre de text anomenta "Name" aquest hem de posar el nom que vulguem, podem posar-hi bot si ens va bé.
el seguent quadre de text que apareix és: "script Path: " aquest hem de seleccionar el fitxer bot.py del nostre projecte, així doncs ens ha de quedar una cosa semblant a <ruta-del-vostre-ordinador>\ChatBot\bot.py
on la <ruta-del-vostre-ordinador> pot ser alguna cosa semblant a C:\Documents\SBC

A l'apartat d'environment ens hem d'assegurar de seleccionar el "Python Interpreter" a Python 3.7
I el "Working directory" a la carpeta d'aquest projecte: ChatBot sent quelcom semblant a:  <ruta-del-vostre-ordinador>\ChatBot
A environment variables, hem d'afegir "ggogle_application_credentials" sense "", per fer-ho a la dreta del quadre de text hi ha un simbol anomenat browse, al seleccionar-lo apareixera una finestra, seleccionem el + i escribim la variable.

Haurem d'instalar algunes llibreries, per fer-ho ens dirigirem a File -> Settings, anirem a l'apartat de Project:<nom del projecte> -> Project Interpreter.
En aquest apartat haurem de seleccionar el simbol + que apareix a la dreta.
A dalt tenim un buscador, hem d'introduir les següents llibreries:
-dialogflow
-google-api-core
-python-telegram-bot
-parse
Per cada una d'elles haurem de seleccionar a la part inferior el boto per instalar.

No ha d'haver cap més problema amb la importació de llibreries, ja que Python les importa automàticament, si hi ha cap problema amb cap llibreria, gràcies a PyCharm aquestes sortiran en vermell en el codi i si intentem executar ens dirà on està el problema
posant el cursor sobre aquest tros de codi i apretant les tecles alt+intro hauriem de poder ser capaços de veure quina llibreria falta per importar i seleccionar import library.

Per executar aquest programa ens hem de dirigir a la fletxa verda d'adalt a la dreta, també anomenada run <nom de la configuració seleccionada> amb aquesta acció executarem la configuració que previament hem configurat.
També és pot usar les tecles Mayus(Shift) + F10.

Si volem tancar el programa ens haurem de dirigir al botó quadrat vermell anomenat Stop <nom de la configuració seleccionada>, també és pot usar les tecles Ctrl + F2

Per qualsevol problema d'execució que no estigui esmentat aquí si us plau envieu un correu a marc.aynesi@students.salle.url.edu, neil.torrero@students.salle.url.edu i alex.monux@students.salle.url.edu

Un cop executat el programa en python, podem conectar-nos al bot usant telegram. Per afegir aquest bot usarem el següent enllaç: https://t.me/Matt_dnd_bot
