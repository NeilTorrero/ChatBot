from tkinter import *
from tkinter.ttk import *


# https://blog.tecladocode.com/tkinter-scrollable-frames/
# Start of scrollable frame
class characterElement(Frame):
    def __init__(self, window, name, race, chara_class, chara_lvl, img):
        # general frame
        container = Frame(window)
        # sub frame
        nameAndPic = Frame(container)

        # name Label
        labelName = Label(nameAndPic, text=name)
        # Race Label
        labelRace = Label(container, text="Race:" + race)
        # Class Label
        labelClass = Label(container, text=chara_class + "(Lvl." + chara_lvl + ")")
        # character Picture Label
        filename = PhotoImage(file=img)
        labelPicture = Label(nameAndPic, image=filename)

        # nameAndPic placing
        labelName.grid(column=0, row=0)
        labelPicture.grid(column=3, row=0)
        # general frame placing
        nameAndPic.grid(column=0, row=0)
        labelRace.grid(column=0, row=1)
        labelClass.grid(column=0, row=2)

        container.pack()
