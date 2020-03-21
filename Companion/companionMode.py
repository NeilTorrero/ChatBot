def character_selection():
    # Selection of characters from saved if none go to creationMode
    print("Characters:")
    # return character


class Need(object):
    def switch(self, option):
        method_name = 'mode_' + option
        method = getattr(self, method_name, lambda: 'Invalid')
        return method(exit)

    def mode_feat(self):
        use_spell_feat()
        return False

    def mode_dice(self):
        dice_roll()
        return False

    def mode_back(self):
        return True


def use_spell_feat():
    print("Spell")


def dice_roll():
    print("Dice")


def companion_mode():
    print("Please select your character:")

    # JSON get characters
    character = character_selection()

    back = False
    while back:
        n = Need()
        back = n.switch("create")
