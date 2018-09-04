import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_PASSIVE_SKILL_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open (inpath) as f:
    data = json.load(f, strict=False)

newdata = {}
for unit in data:
    newdata[unit["P_PASSIVE_SKILL_ID"]] = {
            "Effect": str(unit["P_PROCESS_TYPE"]),
            "Power": str(unit["P_PROCESS_PARAM"]),
            "Description": str(unit["P_EXT_IMG_PARAM"])
    }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
