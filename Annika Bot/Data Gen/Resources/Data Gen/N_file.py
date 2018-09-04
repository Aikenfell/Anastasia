import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_EFFECT_PROCESS_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open (inpath) as f:
    data = json.load(f, strict=False)

newdata = {}
for unit in data:
    newdata[unit["P_EFFECT_PROCESS_ID"]] = {
            "Description": str(unit["P_EFFECT_PROCESS_NAME"]),
            "Effect Frame": str(unit["P_EFFECT_FRAME"]),
            "Damage Frame": str(unit["P_DAMAGE_FRAME"])
    }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
