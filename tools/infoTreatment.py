
def write_immunities(data, out):
    damage_imm = data["damage_immunities"]
    condition_imm = data["condition_immunities"]
    if (len(damage_imm) + len(condition_imm) > 0):
        if len(damage_imm) >= 1:
            out += "Damage immunities are: "
            for a in damage_imm:
                out += a + " "
            out + "And their condition immunities are: "

        if len(condition_imm) >= 1:
            if len(damage_imm) < 1:
                out += "Condition immunities are: "
            for a in damage_imm:
                out += a + " "
    else:
        out ="Looks like this monster doesn't have any of these!"
    return out

def write_monster_properties(data, out , param):
    index = param["Monster-Properties"].lower()
    info = data[index]
    for a in param["Monster-Properties"].split("_"):
        out += " " + a.lower()
    if((info)):
        if isinstance(info, dict):
            out += " are: "
            for a in list(info.keys()):
                out = + a + ": " + info[a] + ", "
        elif isinstance(info, list):
            out += " are: "
            i = 0
            for i in info:
                a = list(i.keys())
                if i == len(info) - 1:
                    out = + info[a[0]] + ": " + info[a[0]]
                else:
                    out = + info[a[0]] + ": " + info[a[0]] + ", "
                i += 1
        else:
            out += " is: " + str(data[param["Monster-Properties"].lower()])
    else:
        out = "Looks like this monster doesn't have any of these!"
    return out