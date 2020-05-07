class Spell:
    def __init__(self, index=None, name=None, desc=None, higher_level=None, _range=None, components=None
                 , material=None, ritual=None, duration=None, concentration=None, casting_time=None
                 , level=None, school=None, classes=None, subclasses=None):
        self.index = index
        self.name = name
        self.desc = desc
        self.higher_level = higher_level
        self._range = _range
        self.components = components
        self.material = material
        self.ritual = ritual
        self.duration = duration
        self.concentration = concentration
        self.casting_time = casting_time
        self.level = level
        self.school = school #Url&Name
        self.classes = classes #Array de Url&Name
        self.subclasses = subclasses #Array de Url&Name