
def write_immunities(data, out):
    damage_imm = data["damage_immunities"]
    condition_imm = data["condition_immunities"]
    if len(damage_imm) > 1:
        out += "Damage immunities are: "
        for a in damage_imm:
            out += a +" "



