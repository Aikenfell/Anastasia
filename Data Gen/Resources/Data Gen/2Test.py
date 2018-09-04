import sys
import uuid
import json
import os



with open('C:\\Users\\Andrew\\Desktop\\BF2 Bot\\Annika Bot\\Data Gen\\Resources\\Data Gen\\Resources\\N_File.json') as f:
    Test = json.load(f, strict=False)
for item in Test["400012400"]["Damage Times"]:

#    print(len(Test["400012400"]["Damage Times"]))

    print(item.split("@")[0].split(":")[1])
