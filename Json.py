# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = character_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, Dict, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Equipment:
    name: str
    damage: str

    @staticmethod
    def from_dict(obj: Any) -> "Equipment":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        damage = from_str(obj.get("Damage"))
        return Equipment(name, damage)

    def to_dict(self) -> dict:
        result: dict = {
            "name": from_str(self.name),
            "Damage": from_str(self.damage)
        }
        return result


@dataclass
class SavingThrow:
    strength: Optional[int] = None
    dexterity: Optional[int] = None
    constitution: Optional[int] = None
    intelligence: Optional[int] = None
    wisdom: Optional[int] = None
    charisma: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "SavingThrow":
        assert isinstance(obj, dict)
        strength = from_union([from_int, from_none], obj.get("strength"))
        dexterity = from_union([from_int, from_none], obj.get("dexterity"))
        constitution = from_union([from_int, from_none], obj.get("constitution"))
        intelligence = from_union([from_int, from_none], obj.get("intelligence"))
        wisdom = from_union([from_int, from_none], obj.get("wisdom"))
        charisma = from_union([from_int, from_none], obj.get("charisma"))
        return SavingThrow(strength, dexterity, constitution, intelligence, wisdom, charisma)

    def to_dict(self) -> dict:
        result: dict = {
            "strength": from_union([from_int, from_none], self.strength),
            "dexterity": from_union([from_int, from_none], self.dexterity),
            "constitution": from_union([from_int, from_none], self.constitution),
            "intelligence": from_union([from_int, from_none], self.intelligence),
            "wisdom": from_union([from_int, from_none], self.wisdom),
            "charisma": from_union([from_int, from_none], self.charisma)
        }
        return result


@dataclass
class Spell:
    name: str
    damage: str
    range: int
    casting_time: int
    level: int

    @staticmethod
    def from_dict(obj: Any) -> "Spell":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        damage = from_str(obj.get("damage"))
        range = int(from_str(obj.get("range")))
        casting_time = int(from_str(obj.get("casting-time")))
        level = int(from_str(obj.get("level")))
        return Spell(name, damage, range, casting_time, level)

    def to_dict(self) -> dict:
        result: dict = {
            "name": from_str(self.name), "damage": from_str(self.damage),
            "range": from_str(str(self.range)), "casting-time": from_str(str(self.casting_time)),
            "level": from_str(str(self.level))
        }
        return result


@dataclass
class Character:
    name: str
    level: int
    character_class: str
    race: str
    stats: List[SavingThrow]
    saving_throws: List[SavingThrow]
    skills: List[Dict[str, int]]
    proficiency_bonus: int
    profeciencies: List[str]
    background: str
    inventory: List[str]
    equipment: List[Equipment]
    description: str
    spells: List[Spell]

    @staticmethod
    def from_dict(obj: Any) -> "Character":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        level = from_int(obj.get("level"))
        character_class = from_str(obj.get("class"))
        race = from_str(obj.get("race"))
        stats = from_list(SavingThrow.from_dict, obj.get("stats"))
        saving_throws = from_list(SavingThrow.from_dict, obj.get("saving_throws"))
        skills = from_list(lambda x: from_dict(from_int, x), obj.get("skills"))
        proficiency_bonus = from_int(obj.get("Proficiency Bonus"))
        proficiencies = from_list(from_str, obj.get("Proficiencies"))
        background = from_str(obj.get("Background"))
        inventory = from_list(from_str, obj.get("Inventory"))
        equipment = from_list(Equipment.from_dict, obj.get("Equipment"))
        description = from_str(obj.get("Description"))
        spells = from_list(Spell.from_dict, obj.get("Spells"))
        return Character(name, level, character_class, race, stats, saving_throws, skills, proficiency_bonus,
                         proficiencies, background, inventory, equipment, description, spells)

    def to_dict(self) -> dict:
        result: dict = {
            "name": from_str(self.name), "level": from_int(self.level),
            "class": from_str(self.character_class), "race": from_str(self.race),
            "stats": from_list(lambda x: to_class(SavingThrow, x), self.stats),
            "saving_throws": from_list(lambda x: to_class(SavingThrow, x), self.saving_throws),
            "skills": from_list(lambda x: from_dict(from_int, x), self.skills),
            "Proficiency Bonus": from_int(self.proficiency_bonus),
            "Proficiencies": from_list(from_str, self.profeciencies),
            "Background": from_str(self.background), "Inventory": from_list(from_str, self.inventory),
            "Equipment": from_list(lambda x: to_class(Equipment, x), self.equipment),
            "Description": from_str(self.description),
            "Spells": from_list(lambda x: to_class(Spell, x), self.spells)
        }
        return result


def character_from_dict(s: Any) -> Character:
    return Character.from_dict(s)


def character_to_dict(x: Character) -> Any:
    return to_class(Character, x)
