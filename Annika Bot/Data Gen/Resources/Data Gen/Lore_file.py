import sys
import uuid
import json
import os

mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_UNIT_EXPLAIN_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")

with open (inpath) as f:
    data = json.load(f, strict=False)

newdata = {}
for unit in data:
    newdata[unit["P_UNIT_ID"]] = {
            "Unit Lore": str(unit["P_DICTIONARY"]),
            "Evolution Quote": str(unit["P_COMMENT_EVO"]),
            "Fusion Quote": str(unit["P_COMMENT_MIX"]),
            "Summon": str(unit["P_COMMENT_SUMMON"]),
            "Trivia": str(unit["P_DICTIONARY_SHORT"]),
            "Summary": str(unit["P_EXPLAIN_SHORT"]),
            "Download": str(unit["P_COMMENT_DOWNLOAD"])
            #"External Image": str(unit["P_EXT_IMG_PARAM"])
    }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
