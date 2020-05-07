

class equipment():

    def __init__(self, _id=None, index=None, name=None, equipmentCategory=None, weaponCategory=None, weaponRange=None
                 , cost=None, damage=None, _range=None, weight=None, twoHandDamage=None, url=None):

        self.id = _id
        self.index = index
        self.name = name
        self.equipmentCategory = equipmentCategory
        self.weaponCategory = weaponCategory
        self.weaponRange = weaponRange
        self.cost = cost
        self.damage = damage #Ex: 1d8
        self._range = _range
        self.weight = weight
        self.twoHandDamage = twoHandDamage #Ex: 1d8
        self.url = url
