
class Character():

    def __init__(self, name ="", chara_class="", level=0, race="", background="", stats="", skills={0,0,0,0,0,0},
                 saving_throws={0,0,0,0,0,0}, proficiency=0, inspiration=1, armorClass=10, HP=1, HD="1D10",
                 death_saves={0,0}):
        self.name = name
        self.chara_class = chara_class #Instancia de CharaClass. Tiene los datos generales de la clase
        self.level = level
        self.race = race
        self.background = background
        self.stats = stats #Array en este orden: STR, DEX, CON, INT, WIS, CHA
        self.skills = skills
        self.saving_throws = saving_throws #Array en este orden: STR, DEX, CON, INT, WIS, CHA
        self.proficiency = proficiency
        self.inpiration = inspiration
        self.armorClass = armorClass
        self.initiative = stats[2] - 10/2;
        self.HP = HP #Hit Points
        self.HD = HD #Hit Dice
        self.death_saves = death_saves #array de int de dos posiciones
