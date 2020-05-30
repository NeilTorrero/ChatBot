def skillsAndSTCreation(stats, saving_throws, skills):
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

    for skill in list(skill2Stat.keys()):
        skills[skill] = (stats[skill2Stat[skill]] - 10) / 2

    for st in list(saving_throws.keys()):
        saving_throws[st] = (stats[st] - 10) / 2
