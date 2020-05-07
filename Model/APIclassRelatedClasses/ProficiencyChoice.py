
#Esta clase se utiliza para: From, Proficiency, SavingThrow, subClass
class ProficiencyChoice():
    def __init__(self, choose=None, _type=None, _from=None):
        self.choose = choose
        self.type = _type
        self._from = _from #List of "From"