import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_LEADER_SKILL_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open (inpath) as f:
    data = json.load(f, strict=False)

newdata = {}
for unit in data:
    newdata[unit["P_LEADER_SKILL_ID"]] = {
            "Skill Name": str(unit["P_LEADER_SKILL_NAME"]),
            "Skill Effects": str(unit["P_PASSIVE_SKILL_GROUP_INFO"])
            #"External Image": str(unit["P_EXT_IMG_PARAM"])
    }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
