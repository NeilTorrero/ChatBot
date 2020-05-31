from tools.API import getInfoAPI


def write_immunities(data, out):
    damage_imm = data["damage_immunities"]
    condition_imm = data["condition_immunities"]
    if len(damage_imm) + len(condition_imm) > 0:
        if len(damage_imm) >= 1:
            out += "Damage immunities are: "
            for a in damage_imm:
                out += a + " "
            out += "And their condition immunities are: "

        if len(condition_imm) >= 1:
            if len(damage_imm) < 1:
                out += "Condition immunities are: "
            for a in damage_imm:
                out += a + " "
    else:
        out = "Looks like this monster doesn't have any of these!"
    return out


def write_monster_properties(data, out, param):
    try:
        index = param["monster-properties"].lower()
        info = data[index]
        for a in param["monster-properties"].split("_"):
            out += "" + a.lower()
    except:
        out = "Looks like this monster doesn't have any of these!"
        return out
    if info:
        if isinstance(info, dict):
            out += " are: "
            for a in list(info.keys()):
                out = + a + ": " + info[a] + ", "
        elif isinstance(info, list):
            out += " are: "
            counter = 0
            for i in info:
                a = list(i.keys())
                if counter == len(info) - 1:
                    out += i[a[0]] + ": " + i[a[1]]
                else:
                    out += i[a[0]] + ": " + i[a[1]] + ", "
                counter += 1
        else:
            out += " is: " + str(data[param["monster-properties"].lower()])
    else:
        out = "Looks like this monster doesn't have any of these!"
    return out


def write_race_properties(data, out, param):
    try:
        index = param["properties"].lower()
        info = data[index]
        for a in param["properties"].split("_"):
            out += "" + a.lower()
    except:
        out = "Looks like this race doesn't have any of these!"
        return out
    if info:
        if isinstance(info, dict):
            out += " are: choose " + info["choose"] + " from:"
            for a in list(info.keys()):
                out = + a + ": " + info[a] + ", "
            counter = 0
            for i in info["from"]:
                if counter == len(info) - 1:
                    out += i["name"]
                else:
                    out += i["name"] + ", "
                counter += 1

        elif isinstance(info, list):
            out += " are: "
            counter = 0
            for i in info:
                if counter == len(info) - 1:
                    out += i["name"]
                else:
                    out += i["name"] + ", "
                counter += 1
        else:
            out += " is: " + str(data[param["Propeties"].lower()])
    else:
        out = "Looks like this race doesn't have any of these!"
    return out


def write_equipment_properties(data, out, param):
    try:
        index = param["properties"].lower()
        info = data[index]
        for a in param["properties"].split("_"):
            out += "" + a.lower()

        if info:
            if isinstance(info, dict):
                if "cost" == param["properties"].lower():
                    out += "is: " + str(info["quantity"]) + info["unit"]
                elif "damage" == param["properties"].lower():
                    damage_type = info["damage_type"]
                    out += "is: " + info["damage_dice"] + " " + damage_type["name"]
                elif "range" == param["properties"].lower():
                    if info["long"]:
                        out += "is: " + str(info["normal"]) + "ft normally and " + str(
                            info["long"]) + "ft with disadvantage"
                    else:
                        out += "is: " + str(info["normal"]) + "ft"
            elif isinstance(info, list):
                out += " are: "
                counter = 0
                for i in info:
                    if counter == len(info) - 1:
                        out += i["name"]
                    else:
                        out += i["name"] + ", "
                    counter += 1
            else:
                out += " is: " + str(info)
        else:
            out = "Looks like this equipment doesn't have any of these!"
        return out
    except:
        out = "\nLooks like this equipment doesn't have any of these!"
        return out


def write_spell_properties(data, out, param):
    try:
        index = param["properties"].lower()
        if index == "description": index = "desc"
        info = data[index]
        for a in param["properties"].split("_"):
            out += "" + a.lower()

        if info:
            if isinstance(info, dict):
                out += "is: " + info["name"]
            elif isinstance(info, list):
                if len(info) > 1:
                    out += " are: "
                else:
                    out += " is: "

                if isinstance(info[0], dict):
                    counter = 0
                    for i in info:
                        if counter == len(info) - 1:
                            out += i["name"]
                        else:
                            out += i["name"] + ", "
                        counter += 1
                else:
                    if index == "desc":
                        counter = 0
                        for i in info:
                            out += i + "\n"
                        try:
                            if data["higher_level"]:
                                out += "\n" + "And... "
                                for i in data["higher_level"]:
                                    out += i + " "
                        except:
                            pass
                    else:
                        counter = 0
                        for i in info:
                            if counter == len(info) - 1:
                                out += i
                            else:
                                out += i + ", "

            else:
                out += " is: " + str(info)
        else:
            out = "Looks like this spell doesn't have any of these!"
        return out
    except:
        out = "Looks like this spell doesn't have any of these!"
        return out

def write_class_properties(data, out, param, level):
    try:
        index = param["properties"].lower()
        print(index)
        info = data[index]
        for a in param["properties"].split("_"):
            out += " " + a.lower()
    except:
        out = "Looks like this class doesn't have any of these!"
        return out
    if info:
        if isinstance(info, dict):
            if index == "starting_equipment":
                dataAux = getInfoAPI("starting-equipment", info["url"].split("/api/starting-equipment/")[1])

                out += "\n You will surely get: "
                counter = 0
                for item in dataAux["starting_equipment"]:
                    if counter == len(dataAux["starting_equipment"]) - 1:
                        out += item["item"]["name"]
                    else:
                        out += item["item"]["name"] + ", "

        elif isinstance(info, list):
            if index == "proficiency" or index == "proficiency_choices" or index == "proficiencies" or index == "saving_throws":
                out += " are these:"
                #proficiency_choices
                #skill
                skill_choices = data["proficiency_choices"][0]
                out += "\n \n" + "Among the skills to choose, you have to choose " \
                       + str(skill_choices["choose"]) + " from: "
                counter = 0
                for skill in skill_choices["from"]:
                    if counter == len(skill_choices["from"])-1:
                        out += skill["name"].split("Skill: ")[1]
                    else:
                        out += skill["name"].split("Skill: ")[1] + ", "
                    counter += 1
                #tool/instruments
                if data["proficiency_choices"][1]:
                    other_choices = data["proficiency_choices"][1]
                    out += "\n \n" + "Among other things to choose, you have to choose" \
                           + str(other_choices["choose"]) + " from: "
                    counter = 0
                    for other in other_choices["from"]:
                        if counter == len(other_choices["from"])-1:
                            out += other["name"]
                        else:
                            out += other["name"] + ", "
                        counter += 1
                #Armor and weapon
                out += "\n \n" + "In regard of item proficiencies, you have... "
                counter = 0
                for i in data["proficiencies"]:
                    if counter == len(data["proficiencies"]) - 1:
                        out += i["name"]
                    else:
                        out += i["name"]+ ", "
                    counter += 1
                #saving throws
                out += "\n \n" + "And you have this saving throws you're proficient in: "
                counter = 0
                for i in data["saving_throws"]:
                    if counter == len(data["saving_throws"]) - 1:
                        out += i["name"]
                    else:
                        out += i["name"]+ ", "
                    counter += 1
                pass
            else:
                #Subclasses
                out += " are: "
                counter = 0
                for sub in info:
                    if counter == len(info) - 1:
                        out += sub["name"]
                    else:
                        out += sub["name"] + ", "
        else:
            out += " is: d" + str(info)
    else:
        out = "Looks like this class doesn't have any of these!"
    return out

def write_trait_properties(data, out, param):
    try:
        index = param["properties"].lower()
        print(index)
        if index == "description": index = "desc"
        info = data[index]
        for a in param["properties"].split("_"):
            out += " " + a.lower()
    except:
        out = "\nLooks like this trait doesn't have any of these!"
        return out
    if info:
        if isinstance(info[0], dict):
            if len(info) > 1:
                out += " are: "
            else:
                out += " is: "
            counter = 0
            for i in info:
                if counter == len(info) - 1:
                    out += i["name"]
                else:
                    out += i["name"] + ", "
                counter += 1
        else:
            out += " is: "
            counter = 0
            for i in info:
                if counter == len(info) - 1:
                    out += i
                else:
                    out += i + "\n "
                counter += 1
    else:
        out = "\nLooks like this trait doesn't have any of these!"
    return out


def write_features_properties(data, out, param):
    try:
        index = param["properties"].lower()
        print(index)
        if index == "description": index = "desc"
        info = data[index]
        for a in param["properties"].split("_"):
            out += " " + a.lower()
    except:
        out = "\n Looks like this feature doesn't have any of these!"
        return out
    if info:
        if isinstance(info, dict):
            out += " is: " + info["name"]
        elif isinstance(info, list):
            if len(info) > 1:
                out += " are: "
            else:
                out += " is: "
            counter = 0
            for i in info:
                if counter == len(info) - 1:
                    out += i
                else:
                    out += i + ", "
                counter += 1
        else:
            out += " is: " + info
    else:
        out = "Looks like this feature doesn't have any of these!"
    return out