def skillsAndSTCreation(stats, saving_throws, skills):
    skill2Stat = {
        "Acrobatics": "dexterity",
        "Animal Handling": "wisdom",
        "Arcana": "intelligence",
        "Athletics": "strength",
        "Deception": "charisma",
        "History": "intelligence",
        "Insight": "wisdom",
        "Intimidation": "charisma",
        "Medicine": "wisdom",
        "Nature": "intelligence",
        "Perception": "wisdom",
        "Performance": "charisma",
        "Religion": "intelligence",
        "Sleight of Hand": "dexterity",
        "Stealth": "dexterity",
        "Survival": "wisdom"
    }

    for skill in list(skill2Stat.keys()):
        skills[skill] = (stats[skill2Stat[skill]] - 10) / 2

    for st in list(saving_throws.keys()):
        saving_throws[st] = (stats[st] - 10) / 2
