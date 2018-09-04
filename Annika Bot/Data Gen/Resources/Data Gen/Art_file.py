import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_UNIT_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")


with open(inpath) as f:
    data = json.load(f)

newdata = {}
for unit in data:
    
    UBN = len(unit["P_SKILL_INFO"].split(","))
    newdata[unit["P_DISPORDER"]] = {
        "Name": str(unit["P_UNIT_NAME"]),
        "ID": str(unit["P_UNIT_ID"]),
        "Element": str(unit["P_ELEMENT"]),
        "Image": "",
        "Thumbnail": "",
        "Attack": "",
        "Idle": "",
        "Victory": "",
        "Move": ""
}

with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
