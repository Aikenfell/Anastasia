import sys
import uuid
import json
import os


mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_ARMS_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open(inpath) as f:
    data = json.load(f)

newdata = {}
for unit in data:
    
    UBN = len(unit["P_SKILL_INFO"].split(","))
    if UBN is 2:    
        newdata[unit["P_DISPORDER"]] = {
                "Name": str(unit["P_ARMS_NAME"]),
                "Rarity": str(unit["P_RARE"]),
                "Summoner ID": str(unit["P_SUMMONER_ID"]),
                "Weapon ID": str(unit["P_ARMS_ID"]),
                "Max Level": str(unit["P_MAX_LV"]),
                "Element": str(unit["P_ELEMENT"]),
                "Max EP": str(unit["gvT2ds0Q"]),
                "Max Enhancements": str(unit["HMt6u09X"]),
                "Max HP": str(unit["P_MAX_HP"]),
                "Max ATK": str(unit["P_MAX_ATK"]),
                "Max DEF": str(unit["P_MAX_DEF"]),
                "Max MDEF": str(unit["P_MAX_MDEF"]),
                "Max BP Specs": str(unit["P_PARAM_MAX"]),
                "Element": str(unit["P_ELEMENT"]),
                "Brave Burst": unit["P_SKILL_INFO"].split(",")[0],
                "Super Brave Burst": unit["P_SKILL_INFO"].split(",")[1],
                "Initial Alt Points": str(unit["P_ALT_SKILL_P"]),
                "Alt Skill": str(unit["P_ALT_SKILL_INFO"]),
                "Leader Skill": str(unit["P_LEADER_SKILL_INFO"]),
                "Es Skill": str(unit["P_PASSIVE_SKILL_GROUP_INFO"]),
                "Damage Type": str(unit["P_ATK_PARTITION"]).split(","),
                "Series": str(unit["P_SERIES"])
        }

    else:
        newdata[unit["P_DISPORDER"]] = {
                "Name": str(unit["P_ARMS_NAME"]),
                "Rarity": str(unit["P_RARE"]),
                "Summoner ID": str(unit["P_SUMMONER_ID"]),
                "Weapon ID": str(unit["P_ARMS_ID"]),
                "Max Level": str(unit["P_MAX_LV"]),
                "Element": str(unit["P_ELEMENT"]),
                "Max EP": str(unit["gvT2ds0Q"]),
                "Max Enhancements": str(unit["HMt6u09X"]),
                "Max HP": str(unit["P_MAX_HP"]),
                "Max ATK": str(unit["P_MAX_ATK"]),
                "Max DEF": str(unit["P_MAX_DEF"]),
                "Max MDEF": str(unit["P_MAX_MDEF"]),
                "Max BP Specs": str(unit["P_PARAM_MAX"]),
                "Element": str(unit["P_ELEMENT"]),
                "Brave Burst": unit["P_SKILL_INFO"],
                "Super Brave Burst": "",
                "Initial Alt Points": str(unit["P_ALT_SKILL_P"]),
                "Alt Skill": str(unit["P_ALT_SKILL_INFO"]),
                "Leader Skill": str(unit["P_LEADER_SKILL_INFO"]),
                "Es Skill": str(unit["P_PASSIVE_SKILL_GROUP_INFO"]),
                "Damage Type": str(unit["P_ATK_PARTITION"]).split(","),
                "Series": str(unit["P_SERIES"])
        }


with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
