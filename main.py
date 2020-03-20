from Companion.companionMode import companionMode
from Creation.creationMode import createChar
from Gestion.gestionMode import gestionMode


class Switcher(object):
    def switch(self, i):
        method_name = 'mode_' + i
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def mode_create(self):
        createChar()

    def mode_gestion(self):
        gestionMode()

    def mode_companion(self):
        companionMode()


s = Switcher()
s.switch("create")
