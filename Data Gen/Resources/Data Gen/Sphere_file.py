import sys
import uuid
import json
import os


mydir = os.path.dirname(__file__) or '.' 
inpath = os.path.join(mydir, 'Input', 'F_SPHERE_ITEM_MST.json')
filename = os.path.splitext(os.path.basename(__file__))[0]
outpath = os.path.join(mydir, "Resources", filename+".json")


with open(inpath) as f:
    data = json.load(f, strict=False)
inpath = os.path.join(mydir, 'Input', 'F_SPHERE_ITEM_EXPLAIN_MST.json')

with open(inpath) as b:
    lore = json.load(b, strict=False)
    

loredata = {}
for unit in lore:
    loredata[unit["P_SPHERE_ITEM_ID"]] = {
            "Short": str(unit["P_EXPLAIN_SHORT"]),
            "Lore": str(unit["P_EXTRA_TEXT"])
    }

newdata = {}
for unit in data:
    newdata[unit["P_DISPORDER"]] = {
            "Sphere Name": str(unit["P_SPHERE_ITEM_NAME"]),
            "Rarity": str(unit["P_RARE"]),
            "Sphere ID": str(unit["P_SPHERE_ITEM_ID"]),
            "Lore": loredata[str(unit["P_SPHERE_ITEM_ID"])]["Lore"]
    }
with open(outpath, "w") as write_file:
    json.dump(newdata, write_file,indent =4)
print("done")
