from tools.API import getInfoAPI


def skillsAndSTCreation(stats, saving_throws, skills, className, proficiencyBonus):
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

    ST2stat = {
        "STR" : "strength",
        "DEX" : "dexterity"
    }

    for skill in list(skill2Stat.keys()):
        skills[skill] = (stats[skill2Stat[skill]] - 10) / 2


    data = getInfoAPI("classes", className)

    for st in list(saving_throws.keys()):
        if data["saving_throws"][0]["name"][:3].lower() == st[:3].lower() \
            or data["saving_throws"][1]["name"][:3].lower() == st[:3]:
            saving_throws[st] = ((stats[st] - 10)/2) + proficiencyBonus
        saving_throws[st] = (stats[st] - 10) / 2