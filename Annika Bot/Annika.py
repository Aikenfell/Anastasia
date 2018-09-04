import sys
import uuid
import http.client
import json
import os
import jellyfish
import re
import discord
import asyncio
##from datetime import datetime
##from datetime import timedelta
from discord.ext import commands

def loadFiles(files):
    dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Data Gen\\Resources\\')
    ret = []
    for file in files:
        path = os.path.join(dir, file)
        if not os.path.exists(path):
            print(path, " was not found.")
            continue
        print(file+" Loading")
        with open(path) as f:
                ret.append(json.load(f, strict=False))

    return ret        
    print("All Files Loaded")

    return ret        
    print("All Files Loaded")
[BF2LS,BF2Units,BF2Lore,BF2BB,BF2MC,BF2S,BF2A,BF2P]=loadFiles(['LS_file.json','Unit_file.json','Lore_file.json','Burst_file.json','Weapon_file.json','Sphere_file.json','Art_file.json','BB_file.json'])


with open('PP_file.json') as a:
    BF2PP = json.load(a, strict=False)
##
##with open('unit_file.json') as b:
##    BF2Units = json.load(b)
##
##with open('Lore_file.json') as c:
##    BF2Lore = json.load(c)
##
##with open('Burst_file.json') as d:
##    BF2BB = json.load(d)
##
##with open('weapon_file.json') as e:
##    BF2MC = json.load(e)
##    
##with open('Sphere_file.json') as f:
##    BF2S = json.load(f)
##    
def fix_fields(fields):
    remove=[]
    uses=['name','value']
    for f in range(0,len(fields)):
        field = fields[f]
        for i in uses:
            if len(field[i])==0:
                remove.append(f)
    fin = [i for j, i in enumerate(fields) if j not in remove]
    return(fin)


#global vars
prefix='a.'
bot = commands.Bot(command_prefix=prefix)

    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.guilds)
    print('------')



# unit commands
@bot.command() # info
async def unit(ctx, code: str):
    global units
    global prefix
#    command=prefix+'unit'
#    unit=(command,units,ctx)

    #start embed - title
    print("Data For Unit "+code)

    embed = discord.Embed(
        title=BF2Units[code]["Name"],
        description="",
        #url=unit['link'],
        #color=ELEMENT_COLOR.get(unit['element'], DEFAULT_ELEMENT_COLOR),
    )
    
    if int(code) < 300 :
        Icon = "http://diffs.bravefrontier.gg/asset_files/ja/unit_unit"+str(BF2Units[code]['Element'])+"_01/1/unit_ills_thum_"+BF2Units[code]["Unit ID"]+".png"
    else:
        Icon = "https://games.gaym.jp/images/upload/3653/icon/"+BF2Units[code]["Unit ID"]+".png"    
    print(Icon)
    embed.set_thumbnail(url=Icon)
    #unit data
    stats=['Max HP', 'Max ATK', 'Max DEF', 'Max MDEF']
    table='\n'.join(['**{Stat}** :  {value}'.format(Stat=stat, value=BF2Units[code][stat])for stat in stats])
        
    embed.add_field(name="**Stats At Max Level**",      value=table,     inline=False)
    
    embed.add_field(name="Total Alt Points",      value=BF2Units[code]["Initial Alt Points"],     inline=False)

    embed.add_field(name="Normal Attack Damage Distribution",      value="**Physical : **"+BF2Units[code]["Damage Type"][0]+"%\n"+"**Magical : **"+BF2Units[code]["Damage Type"][1]+"%",     inline=False)

    if BF2Units[code]['Alt Skill'] != "":
        embed.add_field(name="Alt Skill",      value=BF2Units[code]['Alt Skill'],     inline=False)
    
    embed.add_field(name="Max BP Enhancements",      value=BF2Units[code]['Max BP Specs'],     inline=False)
    if BF2Units[code]['Brave Burst'] != "":
        embed.add_field(name="**Brave Burst : **"+"__"+str(BF2BB[str(BF2Units[code]['Brave Burst'])]["Skill Name"])+"__",      value=BF2P[BF2Units[code]['Brave Burst']]["P_EXTRA_TEXT"]+"\nCost : "+BF2P[BF2Units[code]['Brave Burst']]["Cost"][1]+" Burst Crystals",     inline=False)
    if BF2Units[code]['Super Brave Burst'] != "":
        embed.add_field(name="**Super Brave Burst : **"+"__"+str(BF2BB[str(BF2Units[code]['Super Brave Burst'])]["Skill Name"])+"__",      value=BF2P[BF2Units[code]['Super Brave Burst']]["P_EXTRA_TEXT"]+"\nCost : "+BF2P[BF2Units[code]['Super Brave Burst']]["Cost"][1]+" Burst Crystals",     inline=False)
    if BF2Units[code]['Leader Skill'] != "":
        embed.add_field(name="**Leader Skill : **"+"__"+str(BF2LS[str(BF2Units[code]['Leader Skill'])]["Skill Name"])+"__",      value="Placeholder"#BF2PP[BF2Units[code]['Leader Skill']]["Description"]
                        ,     inline=False)
    if BF2Units[code]['Es Skill'] != "":
        embed.add_field(name="Es Skill",      value=BF2Units[code]['Es Skill'],     inline=False)
    Art = BF2A[code]['Image']+".png"

    embed.set_image(url=Art)
    await ctx.send(embed=embed)

    # unit commands
@bot.command() # info
async def victory(ctx, code: str):
    global units
    global prefix
    command=prefix+'victory'

    #start embed - title
    embed = discord.Embed(
        title=BF2A[code]['Name'],
        description="",
    )
    Art = BF2A[code]['Victory']+".gif"
    embed.set_image(url= Art)
    await ctx.send(embed=embed) 

@bot.command() # info
async def move(ctx, code: str):
    global units
    global prefix
    command=prefix+'move'

    #start embed - title
    embed = discord.Embed(
        title=BF2A[code]['Name'],
        description="",
    )
    Art = BF2A[code]['Move']+".gif"
    embed.set_image(url= Art)
    await ctx.send(embed=embed) 

@bot.command() # info
async def image(ctx, code: str):
    global units
    global prefix
    command=prefix+'attack'

    #start embed - title
    embed = discord.Embed(
        title=BF2A[code]['Name'],
        description="",
    )
    Art = BF2A[code]['Image']+".png"
    embed.set_image(url= Art)
    await ctx.send(embed=embed) 

@bot.command() # info
async def thumbnail(ctx, code: str):
    global units
    global prefix
    command=prefix+'attack'

    #start embed - title
    embed = discord.Embed(
        title=BF2A[code]['Name'],
        description="",
    )
    Art = BF2A[code]['Thumbnail']+".png"
    embed.set_image(url= Art)
    await ctx.send(embed=embed) 

@bot.command() # info
async def weapon(ctx, code: str):
    global units
    global prefix
#    command=prefix+'unit'
#    unit=(command,units,ctx)

    #start embed - title
    print("Data For Unit "+code)

    embed = discord.Embed(
        title=BF2Units[code]["Name"],
        description="",
        #url=unit['link'],
        #color=ELEMENT_COLOR.get(unit['element'], DEFAULT_ELEMENT_COLOR),
    )
    Icon = "http://diffs.bravefrontier.gg/asset_files/ja/weapon_weapon/1/weapon_thum_"+BF2MC[code]["Weapon ID"]+".png"
    print(Icon)
    embed.set_thumbnail(url=Icon)
    #unit data
    embed.add_field(name="Max HP",      value=BF2MC[code]['Max HP'],     inline=False)
    
    embed.add_field(name="Max Atk",      value=BF2MC[code]['Max ATK'],     inline=False)

    embed.add_field(name="Max Def",      value=BF2MC[code]['Max DEF'],     inline=False)

    embed.add_field(name="Max MDef",      value=BF2MC[code]['Max MDEF'],     inline=False)

    embed.add_field(name="Total Alt Points",      value=BF2MC[code]["Initial Alt Points"],     inline=False)

    if BF2MC[code]['Alt Skill'] != "":
        embed.add_field(name="Alt Skill",      value=BF2MC[code]['Alt Skill'],     inline=False)
    
    if BF2MC[code]['Brave Burst'] != "":
        embed.add_field(name="Brave Burst",      value=BF2BB[str(BF2MC[code]['Brave Burst'])]["Skill Name"],     inline=False)
    if BF2MC[code]['Super Brave Burst'] != "":
        embed.add_field(name="Super Brave Burst",      value=BF2BB[str(BF2MC[code]['Super Brave Burst'])]["Skill Name"],     inline=False)
    if BF2MC[code]['Leader Skill'] != "":
        embed.add_field(name="Leader Skill",      value=BF2LS[str(BF2MC[code]['Leader Skill'])]["Skill Name"],     inline=False)
    if BF2MC[code]['Es Skill'] != "":
        embed.add_field(name="Es Skill",      value=BF2MC[code]['Es Skill'],     inline=False)
        
    Art = "http://diffs.bravefrontier.gg/asset_files/ja/unit_unit_arms_rin_01/1/unit_ills_full_221"+BF2MC[code]["Weapon ID"]+".png"
    embed.set_image(url=Art)
    await ctx.send(embed=embed) 



# unit commands
@bot.command() # info
async def lore(ctx, code: str):
    global units
    global prefix
#    command=prefix+'unit'
#    unit=(command,units,ctx)

    #start embed - title
    print(code)

    embed = discord.Embed(
        title=BF2Units[code]["Name"],
        description="",
        #url=unit['link'],
        #color=ELEMENT_COLOR.get(unit['element'], DEFAULT_ELEMENT_COLOR),
    )
    Icon = "http://diffs.bravefrontier.gg/asset_files/ja/unit_unit"+str(BF2Units[code]['Element'])+"_01/1/unit_ills_thum_"+BF2Units[code]["Unit ID"]+".png"
    print(Icon)
    embed.set_thumbnail(url=Icon)
    #unit data
    print("Lore For Unit "+code)
    embed.add_field(name="Lore",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Unit Lore"],     inline=False)
    if BF2Lore[str(BF2Units[code]["Unit ID"])]["Evolution Quote"] != "":
        embed.add_field(name="Evolution",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Evolution Quote"],     inline=False)
    if BF2Lore[str(BF2Units[code]["Unit ID"])]["Fusion Quote"] != "":
        embed.add_field(name="Fusion",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Fusion Quote"],     inline=False)
    if BF2Lore[str(BF2Units[code]["Unit ID"])]["Summon"] != "":
        embed.add_field(name="Summon",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Summon"],     inline=False)
    if BF2Lore[str(BF2Units[code]["Unit ID"])]["Download"] != "":
        embed.add_field(name="Download",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Download"],     inline=False)
    if BF2Lore[str(BF2Units[code]["Unit ID"])]["Trivia"] != "":
        embed.add_field(name="Trivia",      value=BF2Lore[str(BF2Units[code]["Unit ID"])]["Trivia"],     inline=False)
    

    Art = BF2A[code]['Image']+".png"
    embed.set_image(url=Art)
    await ctx.send(embed=embed)


@bot.command() # info
async def sphere(ctx, code: str):
    global units
    global prefix
#    command=prefix+'unit'
#    unit=(command,units,ctx)

    #start embed - title
    print(code)

    embed = discord.Embed(
        title=BF2S[code]["Sphere Name"],
        description="",
        #url=unit['link'],
        #color=ELEMENT_COLOR.get(unit['element'], DEFAULT_ELEMENT_COLOR),
    )
    Icon = "http://diffs.bravefrontier.gg/asset_files/ja/item_item/1/sphere_thum_"+BF2S[code]["Sphere ID"]+".png"
    print(Icon)
    embed.set_thumbnail(url=Icon)
    #unit data
    print("Sphere Code - "+code)
    embed.add_field(name="Rarity",      value=BF2S[code]["Rarity"],     inline=False)
    embed.add_field(name="Sphere ID",      value=BF2S[code]["Sphere ID"],     inline=False)
    embed.add_field(name="Lore",      value=BF2S[code]["Lore"],     inline=False)

    await ctx.send(embed=embed)
    



@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Anastasia", description="Still A Wip But Getting There", color=0xeee657)

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/oauth2/authorize?client_id=474238952979824640&permissions=387136&scope=bot>)")
    # credits 
    embed.add_field(name="Credits", value=
        "Art Files And Game Data: <@164162210652880899> & <@176793098721034240>\n"+
        "Code: <@281201917802315776> & <@213962205895458818>\n"+
        "Unit And Summoner Guides : <@228313269042020353> & <@294121487743582209>\n"+
        "Hosting: <@213962205895458818>")
    #embed.add_field(name="Thanks", value="")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Anastasia Bot", description="**Commands:**", color=0xeee657)

    embed.add_field(name="a.unit *Unit ID*", value="Brings Up Unit Info", inline=False)
    embed.add_field(name="a.lore *Unit ID*", value="Brings Up Unit Lore And Trivia", inline=False)
    embed.add_field(name="a.weapon *Weapon ID*", value="Brings Up Weapon Info", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def guide(ctx, code: int):
    embed = discord.Embed(title="Page "+str(code), description="**Unit Guide**", color=0xeee657)

    if code == 1:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479452973865500673/Page_1.png")
    elif code == 2:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479452981612380170/Page_2.png")
    elif code == 3:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479452986343424010/Page_3.png")
    elif code == 4:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479457633229733924/Page_4.png")
    elif code == 5:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479460420780949514/Page_5.png")
    elif code == 6:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479464920807636992/Page_6.png")
    elif code == 7:
        embed.set_image(url="https://cdn.discordapp.com/attachments/475017946830340099/479464949509390336/Page_7.png")
    await ctx.send(embed=embed)


@bot.command()
async def arthelp(ctx):
    embed = discord.Embed(title="Anastasia Bot", description="**Art Commands:**", color=0xeee657)

    embed.add_field(name="a.move *Unit ID*", value="Brings Up Unit Movement Animation", inline=False)
    embed.add_field(name="a.attack *Unit ID*", value="Brings Up Unit Attack Animation", inline=False)
    embed.add_field(name="a.move *Unit ID*", value="Brings Up Unit Victory Animation", inline=False)
    embed.add_field(name="a.idle *Unit ID*", value="Brings Up Unit Idle Animation", inline=False)
    embed.add_field(name="a.image *Unit ID*", value="Brings Up Unit Full Image", inline=False)
    embed.add_field(name="a.thumbnail *Unit ID*", value="Brings Up Unit Thumnail", inline=False)
    await ctx.send(embed=embed)

@bot.command() # info
async def debug(ctx):
    global units
    global prefix
    command=prefix+'unit'
    unit=find_best(command,units,ctx)

    #start embed - title
    embed = discord.Embed(
        title=unit['name'],
        description="",
        url=unit['link'],
        color=ELEMENT_COLOR.get(unit['element'], DEFAULT_ELEMENT_COLOR),
    )
    #icon
    embed.set_thumbnail(url=unit['icon'])
    #unit data
    embed.add_field(name="gender",      value=unit['gender'],     inline=True)
    embed.add_field(name="rarity",      value=unit['rarity'],     inline=True)
    embed.add_field(name="country",     value=unit['country'],    inline=True)
    if unit['collab'] != "":
        embed.add_field(name="collab",      value=unit['collab'],     inline=True)
    if unit['master ability'] != "":
        embed.add_field(name="master ability",value=unit['master ability'],inline=False)
    embed.add_field(name="leader skill",value=unit['leader skill'],inline=False)
    embed.add_field(name="Job 1",       value=unit['job 1'],      inline=True)
    embed.add_field(name="Job 2",       value=unit['job 2'],      inline=True)
    if unit['job 3'] != "":
        embed.add_field(name="Job 3",       value=unit['job 3'],      inline=False)
    if unit['jc 1'] != "":
        embed.add_field(name="Job Change 1",value=unit['jc 1'],       inline=True)
    if unit['jc 2'] != "":
        embed.add_field(name="Job Change 2",value=unit['jc 2'],       inline=True)
    if unit['jc 3'] != "":
        embed.add_field(name="Job Change 3",value=unit['jc 3'],       inline=True)

    embed.set_image(url=unit['artworks'][0]['full'])
    await ctx.send(embed=embed) 




BOT_TOKEN=""
bot.run(BOT_TOKEN)
