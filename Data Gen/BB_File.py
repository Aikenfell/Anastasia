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

foo = {}
for skill in data:
    if skill['P_SKILL_ID'] not in foo:
        foo[skill['P_SKILL_ID']] = {}

    smaller_skill = {}
    smaller_skill = foo[skill['P_SKILL_ID']]
    smaller_skill['Cost'] = str(skill['P_COST_INFO']).split(",")

    if 'P_PROCESS_PARAM' not in smaller_skill:
        smaller_skill['P_PROCESS_PARAM'] = {}

    smaller_skill['P_PROCESS_PARAM'][skill['P_LV']] = skill['P_PROCESS_PARAM']

    if skill['P_EXTRA_TEXT']:
        smaller_skill['P_EXTRA_TEXT'] = skill['P_EXTRA_TEXT']

with open(outpath, "w") as write_file:
    json.dump(foo, write_file,indent =4)
print("done")
