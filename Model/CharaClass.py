
class chara_class():
    def __init__(self, _id=None, index=None, name=None, hit_die=None, proficiency_choices=None
                 , proficiencies=None, saving_throws=None, starting_equipment=None, class_levels=None,
                 subclasses=None, url=None):
        self._id =_id
        self.index = index
        self.name = name
        self.hit_die = hit_die
        self.proficiency_choices = proficiency_choices #List of ProficiencyChoice
        self.proficiencies = proficiencies #List of Proficiency (URL&Name)
        self.saving_throws = saving_throws #List of SavingThrows (URL&Name)
        self.starting_equipment = starting_equipment #List of StartingEquipment
        self.class_levels = class_levels #List of ClassLevels (URL&Name)
        self.subclasses = subclasses #List of SubClass (URL&Name)
        self.url = url