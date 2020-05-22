from tkinter import *
from tkinter.ttk import *

from Visuals.components.characterElement import characterElement
from Visuals.components.chatMessage import chatMessage
from Visuals.components.scrollableFrame import scrollableFrame

class MainView():
    path = "C:\\Users\\User\\Documents\\GitHub\\web\\ChatBot\\resources\\"
    window = ""
    charasList = ""
    conversation = ""
    send = ""
    def __init__(self):
        self.window = Tk()

        self.window.title("Mattbott - WoTC")
        self.window.geometry("1400x900+200-100")
        filename = PhotoImage(file=self.path + "bg_IMG.png")
        background_label = Label(self.window, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # https://blog.tecladocode.com/tkinter-scrollable-frames/
        # Conversation Log
        self.conversation = scrollableFrame(self.window, W=1048, H=776, X=10, Y=10)

        # for i in range(50):
        #    Label(conversation.scrollable_frame, text="Sample scrolling label").pack()

        # List of characters Frame
        self.charasList = scrollableFrame(self.window, W=282, H=776, X=1086, Y=10)
        Label(self.charasList.scrollable_frame, text="Current Characters:").pack()
        # Text input
        input = Text(self.window, height=5, width=133)
        input.place(x=10, y=796)

        ##Send and reset buttons
        self.send = Button(self.window, text="Send", width=49)
        # send.config(height = 20)
        restart = Button(self.window, text="Restart", width=49)
        self.send.place(x=1086, y=796)
        restart.place(x=1086, y=839)

        characterElement(self.charasList.scrollable_frame, "place", "Humano", "Paladin", "6", self.path + "placeholder.png")
        chatMessage(self.conversation.scrollable_frame, "Jaja si soy yommmmmmmmmmmmmmmmmmmmmmm mmmmmmmmmmmmmmmmmmmmm mmmmmmmmmmmmmm mmmmmmmmmmmmmmmmmmm", 1)

        self.window.resizable(False, False)

    def startGUI(self):
        self.window.mainloop()

    def addMessage(self, isBot, message):
        chatMessage(self.conversation.scrollable_frame,
                              message,
                              isBot)

    def addChara(self, chara_name, race, chara_class, level):
        characterElement(self.charasList.scrollable_frame,
                         chara_name, race, chara_class, level,
                         self.path + "placeholder.png")

    def getMessage(self):
        return self.send.get("1.0",'end-1c')
