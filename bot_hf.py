from random import randint
import discord
from discord.ext import commands

description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello():
    """Says Hello World"""
    await bot.say("Hellod")

def code_names_init():
    game=[]
    noms=[]
    fich1=open("mots_code_names.txt.txt","r")
    h=fich1.read()
    for x in h.split('\n'):
        noms.append(x)
    while len(game)<25:
        k=randint(0,len(noms)-1)
        game.append(noms[k])
        game=list(set(game))
    l=[]
    for i in range(5):
        l.append(game[i*5:5*(i+1)])
    return(l)
    
def grille_jeu_init():
    tab_jeu=[['n' for i in range(5)]for j in range(5)]
    c=randint(0,1)
    if (c == 1):
        i1,j1=randint(0,4),randint(0,4)
        tab_jeu[i1][j1]='m'
        k=0
        while k<9:
            i1,j1=randint(0,4),randint(0,4)
            if tab_jeu[i1][j1]=='n':
                tab_jeu[i1][j1]='r'
                k+=1
        k=0
        while k<8:
            i1,j1=randint(0,4),randint(0,4)
            if tab_jeu[i1][j1]=='n':
                tab_jeu[i1][j1]='b'
                k+=1
        return('r',tab_jeu)
    else:
        i1,j1=randint(0,4),randint(0,4)
        tab_jeu[i1][j1]='m'
        k=0
        while k<9:
            i1,j1=randint(0,4),randint(0,4)
            if tab_jeu[i1][j1]=='n':
                tab_jeu[i1][j1]='b'
                k+=1
        k=0
        while k<8:
            i1,j1=randint(0,4),randint(0,4)
            if tab_jeu[i1][j1]=='n':
                tab_jeu[i1][j1]='r'
                k+=1
        return('b',tab_jeu)

def afficher(game):
    for x in game:
        m=' - '.join(x)
        print(m)

@bot.command()
async def code_names(espion1 : discord.Member, espion2 : discord.Member):
    game=code_names_init()
    a,grille=grille_jeu_init()
    fin=0
    tab_attente=[]
    for x in game:
        tab_attente.append(' - '.join(x))
    affichage='\n'.join(tab_attente)
    tab_attente=[]
    for x in grille:
        tab_attente.append(' - '.join(x))
    affichage_grille='\n'.join(tab_attente)
    await bot.say(affichage)
    await bot.send_message(espion1,affichage_grille)
    await bot.send_message(espion2,affichage_grille)
    if a=='r':
        tot_r=9
        tot_b=8
        tour=1
    else:
        tot_r=8
        tot_b=9
        tour=0
    while(fin!=1):
        if tour ==1:
            await bot.say("Tour Rouge")
        else:
            await bot.say("Tour Bleue")
        await bot.say("combien de cases ?")
        nombre = int((await bot.wait_for_message(author=espion1)).content)
        for k in range(nombre):
            await bot.say("Quel ligne ?")
            i = int((await bot.wait_for_message(author=espion1)).content)-1
            await bot.say("Quel colonne ?")
            j = int((await bot.wait_for_message(author=espion1)).content)-1
            if grille[i][j]=='m':
                game[i][j]='MORT'
                await bot.say("La team a perdu !")
                fin=1
                break
            elif grille[i][j]=='r':
                tot_r-=1
                game[i][j]='RRRR'
                if tour==0:
                    break
            elif grille[i][j]=='b':
                tot_b-=1
                game[i][j]='BBBB'
                if tour==1:
                    break
            else:
                game[i][j]='NNNN'
                break
            if tot_r==0:
                fin=1
                await bot.say("Les rouges ont gagné !")
                break
            elif tot_b==0:
                fin=1
                await bot.say("Les bleues ont gagné !")
                break
            tab_attente=[]
            if k != nombre - 1 :
                for x in game:
                    tab_attente.append(' - '.join(x))
                affichage='\n'.join(tab_attente)
                await bot.say(affichage)
        tour=(tour+1)%2
        tab_attente=[]
        for x in game:
            tab_attente.append(' - '.join(x))
        affichage='\n'.join(tab_attente)
        await bot.say(affichage)
        

bot.run(TOKEN)
        