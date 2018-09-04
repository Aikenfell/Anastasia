import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_SKILL_LEVEL_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open (inpath) as f:
    data = json.load(f, strict=False)

newdata = {}
subdata = []
subsub = {}
for unit in data:
    if ["P_EXTRA_TEXT"] != "":
        newdata[unit["P_SKILL_ID"]] = {
                unit["P_LV"]: unit["P_PROCESS_PARAM"],
                "Description": unit["P_EXTRA_TEXT"],
                "Cost": unit["P_COST_INFO"].split(",")[1]
        }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
