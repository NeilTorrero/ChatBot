# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = characters_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Dict, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class SavingThrows:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @staticmethod
    def from_dict(obj: Any) -> "SavingThrows":
        assert isinstance(obj, dict)
        strength = from_int(obj.get("strength"))
        dexterity = from_int(obj.get("dexterity"))
        constitution = from_int(obj.get("constitution"))
        intelligence = from_int(obj.get("intelligence"))
        wisdom = from_int(obj.get("wisdom"))
        charisma = from_int(obj.get("charisma"))
        return SavingThrows(strength, dexterity, constitution, intelligence, wisdom, charisma)

    def to_dict(self) -> dict:
        result: dict = {
            "strength": from_int(self.strength),
            "dexterity": from_int(self.dexterity),
            "constitution": from_int(self.constitution),
            "intelligence": from_int(self.intelligence),
            "wisdom": from_int(self.wisdom),
            "charisma": from_int(self.charisma)
        }
        return result


@dataclass
class Spell:
    name: str
    damage: str
    spell_range: int
    casting_time: int
    level: int
    components: str
    duration: str

    @staticmethod
    def from_dict(obj: Any) -> "Spell":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        damage = from_str(obj.get("damage"))
        spell_range = from_int(obj.get("spell-range"))
        casting_time = from_int(obj.get("casting-time"))
        level = from_int(obj.get("level"))
        components = from_str(obj.get("components"))
        duration = from_str(obj.get("Duration"))
        return Spell(name, damage, spell_range, casting_time, level, components, duration)

    def to_dict(self) -> dict:
        result: dict = {
            "name": from_str(self.name),
            "damage": from_str(self.damage),
            "spell-range": from_int(self.spell_range),
            "casting-time": from_int(self.casting_time),
            "level": from_int(self.level),
            "components": from_str(self.components),
            "Duration": from_str(self.duration)
        }
        return result


@dataclass
class Character:
    name: str
    level: int
    character_class: str
    race: str
    stats: SavingThrows
    saving_throws: SavingThrows
    skills: Dict[str, int]
    proficiency_bonus: int
    proficiencies: List[str]
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
        stats = SavingThrows.from_dict(obj.get("stats"))
        saving_throws = SavingThrows.from_dict(obj.get("saving_throws"))
        skills = from_dict(from_int, obj.get("skills"))
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
            "name": from_str(self.name),
            "level": from_int(self.level),
            "class": from_str(self.character_class),
            "race": from_str(self.race),
            "stats": to_class(SavingThrows, self.stats),
            "saving_throws": to_class(SavingThrows, self.saving_throws),
            "skills": from_dict(from_int, self.skills),
            "Proficiency Bonus": from_int(self.proficiency_bonus),
            "Proficiencies": from_list(from_str, self.proficiencies),
            "Background": from_str(self.background),
            "Inventory": from_list(from_str, self.inventory),
            "Equipment": from_list(lambda x: to_class(Equipment, x), self.equipment),
            "Description": from_str(self.description),
            "Spells": from_list(lambda x: to_class(Spell, x), self.spells)
        }
        return result


def characters_from_dict(s: Any) -> List[Character]:
    return from_list(Character.from_dict, s)


def characters_to_dict(x: List[Character]) -> Any:
    return from_list(lambda x: to_class(Character, x), x)
