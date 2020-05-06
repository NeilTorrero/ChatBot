from tkinter import *
from tkinter.ttk import *


# https://blog.tecladocode.com/tkinter-scrollable-frames/
# Start of scrollable frame
class characterElement(Frame):
    def __init__(self, window, name, race, chara_class, chara_lvl, img):
        # general frame
        container = Frame(window, width=200, height=300)
        # sub frame
        nameAndPic = Frame(container)

        # name Label
        labelName = Label(container, text=name, font=("Times New Roman", 14, "bold"))
        # Race Label
        labelRace = Label(container, text="Race:" + race)
        # Class Label
        labelClass = Label(container, text="Class:"+chara_class + "(Lvl." + chara_lvl + ")")
        # character Picture Label
        filename = PhotoImage(file=img)
        labelPicture = Label(container, image=filename)
        labelPicture.image=filename

        # nameAndPic placing
        labelName.grid(column=0, row=0)
        #labelPicture.place(x=50,y=0)
        # general frame placing
        #nameAndPic.grid(column=0, row=0)
        labelRace.grid(column=0, row=1, padx=0, pady=0)
        labelClass.grid(column=0, row=2, padx=0, pady=0)

        container.pack()

