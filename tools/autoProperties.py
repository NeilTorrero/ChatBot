import random

from tools.API import getInfoAPI


def skillsAndSTCreation(chara):
    skill2Stat = {
        "acrobatics": "dexterity",
        "animal-handling": "wisdom",
        "arcana": "intelligence",
        "athletics": "strength",
        "deception": "charisma",
        "history": "intelligence",
        "insight": "wisdom",
        "intimidation": "charisma",
        "medicine": "wisdom",
        "nature": "intelligence",
        "perception": "wisdom",
        "performance": "charisma",
        "religion": "intelligence",
        "sleight-of-hand": "dexterity",
        "stealth": "dexterity",
        "survival": "wisdom"
    }

    stats = chara['stats']
    saving_throws = chara['saving_throws']
    skills = chara['skills']
    className = chara['classes']
    level = chara['level']
    for skill in list(skill2Stat.keys()):
        skills[skill] = int((stats[skill2Stat[skill]] - 10) / 2)

    data = getInfoAPI("classes", className)
    dataLevel = getInfoAPI("classes/"+className+"/levels", int(level))
    proficiencyBonus = dataLevel["prof_bonus"]

    for st in list(saving_throws.keys()):
        if data["saving_throws"][0]["name"][:3].lower() == st[:3].lower() \
                or data["saving_throws"][1]["name"][:3].lower() == st[:3]:
            saving_throws[st] = int(((stats[st] - 10) / 2)) + proficiencyBonus
        saving_throws[st] = int((stats[st] - 10) / 2)


def lifeCalculator(chara):
    con = int((chara['stats']['constitution'] - 10) / 2)
    className = chara['classes']
    data = getInfoAPI("classes", className)
    hit_dice = data['hit_die']
    life = hit_dice + con
    for i in range(1, int(chara['level'])):
        life += random.randrange(1, int(hit_dice)) + con
    chara['life'] = int(life)
