from Companion.companionMode import companion_mode
from Creation.creationMode import create_char
from Gestion.gestionMode import gestion_mode


class Switcher(object):
    def switch(self, i):
        method_name = 'mode_' + i
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def mode_create(self):
        create_char()

    def mode_gestion(self):
        gestion_mode()

    def mode_companion(self):
        companion_mode()


s = Switcher()
s.switch("create")
