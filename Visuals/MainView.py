from tkinter import *
from tkinter.ttk import *

from Visuals.components.scrollableFrame import scrollableFrame

path = "C:\\Users\\User\\Documents\\GitHub\\web\\ChatBot"
def initVis():

    window = Tk()

    window.title("Mattbott - WoTC")
    window.geometry("1400x900+200-100")
    filename = PhotoImage(file=path+"\\resources\\bg_IMG.png")
    background_label = Label(window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #https://blog.tecladocode.com/tkinter-scrollable-frames/
    #Conversation Log
    conversation = scrollableFrame(window, W=1048, H=776, X=10, Y=10)

    #for i in range(50):
    #    Label(conversation.scrollable_frame, text="Sample scrolling label").pack()


    #List of characters Frame
    charasList = scrollableFrame(window, W=282, H=776, X =1086, Y=10)
    Label(charasList.scrollable_frame, text="Current Characters:").pack()
    #Text input
    input = Text(window, height=5, width=133)
    input.place(x=10, y=796)

    ##Send and reset buttons
    send = Button(window, text="Send", width=49)
    #send.config(height = 20)
    restart = Button(window, text="Restart", width=49)
    send.place(x=1086,y=796)
    restart.place(x=1086,y=839)

    window.resizable(False, False)
    window.mainloop()