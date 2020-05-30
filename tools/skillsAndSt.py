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
        skills[skill] = (stats[skill2Stat[skill]] - 10) / 2

    data = getInfoAPI("classes", className)
    dataLevel = getInfoAPI("classes/"+className+"/levels", level)
    proficiencyBonus = dataLevel["prof_bonus"]

    for st in list(saving_throws.keys()):
        if data["saving_throws"][0]["name"][:3].lower() == st[:3].lower() \
                or data["saving_throws"][1]["name"][:3].lower() == st[:3]:
            saving_throws[st] = ((stats[st] - 10) / 2) + proficiencyBonus
        saving_throws[st] = (stats[st] - 10) / 2
