class MainController:

    def __init__(self, mainView):
        self.mainView = mainView

    def userMessage(self):
        message = self.mainView.getMessage()
        self.mainView.addMessage(0, message)
        #TODO: Restart textArea

        #TODO: AI Action

    def botMessage(self, message):
        self.mainView.addMessage(1, message)

    def addChara(self, chara_name, race, chara_class, level):
        self.mainView.addMessage(chara_name, race, chara_class, level)