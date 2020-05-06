from tkinter import *
path = "C:\\Users\\User\\Documents\\GitHub\\web\\ChatBot\\resources\\"

MAX_CHARS = 91;

class chatMessage(Frame):
    def __init__(self, window, messageText, isBot):
        # general frame
        container = Frame(window)
        # sub frame
        textFrame = Frame(container, bg="brown")

        #TODO: comprovar que mensaje sea menor que 91 charas y si no lo es separarlo y new line
        if(len(messageText) >= 91):
            parts = messageText.split(" ")
            messageText = ""
            parts[len(parts)-1] = "\n" + parts[len(parts)-1]
            for part in parts:
                messageText = messageText + " "+ part
        else:
            while len(messageText) <= 180:
                messageText = messageText + "   "

        # text Label
        if isBot:
            personText = Label(textFrame, bg="brown", text="Mattbot", fg="white",   font=("Times New Roman", 12, "underline"))
            labelText = Label(textFrame,bg="brown", text=messageText, font=("Times New Roman", 12, "bold"), justify="left")
        else:
            textFrame.config(bg="green")
            personText = Label(textFrame, bg="green", text="You", fg="white", font=("Times New Roman", 12, "underline"))
            labelText = Label(textFrame, bg="green", text=messageText, font=("Times New Roman", 12, "bold"),justify="left")
        #Text Placing
        personText.pack(padx=1, pady=1)
        labelText.pack(padx=10,pady=10)

        #Pic Label
        filename = PhotoImage(file=path + "placeholder.png")
        labelPicture = Label(container, image=filename)
        labelPicture.image = filename

        # general frame placing
        textFrame.grid(column=1, row=0)
        labelPicture.grid(column=0, row=0)

        container.pack()
