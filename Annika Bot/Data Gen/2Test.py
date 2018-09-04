import sys
import uuid
import json
import os



with open('F_UNIT_EXPLAIN_MST.json') as f:
    sphere = json.load(f, strict=False)

with open('F_SPHERE_ITEM_EXPLAIN_MST.json') as f:
    lore = json.load(f, strict=False)
    
#    print(len(data["3"]["P_SKILL_INFO"].split(","))
    print(lore['P_SPHERE_ITEM_ID']["100101"])
