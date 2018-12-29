from random import randint
import discord
from discord.ext import commands
import os
import math
import copy

description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)

TOKEN = os.environ['TOKEN']
NOMS=['Accident', 'Achat', 'Acné', 'Action', 'Adolescent', 'Afrique', 'Aiguille', 'Allumer', 'Alpes', 'Alphabet', 'Altitude', 'Amérique', 'Ami', 'Amour', 'Ampoule', 'Anniversaire', 'Appétit', 'Araignée', 'Arbre', 'Arc', 'Arc-en-ciel', 'Argent', 'Arme', 'Armée', 'Ascenseur', 'Asie', 'Assis', 'Astronaute', 'Atchoum', 'Athlète', 'Atlantide', 'Aube', 'Australie', 'Avec', 'Aventure', 'Avion', 'Avocat', 'Bac', 'Baguette', 'Bain', 'Baiser', 'Balai', 'Balle', 'Ballon', 'Bambou', 'Banane', 'Bannir', 'Barbe', 'Barrière', 'Bas', 'Basket', 'Bateau', 'Bâton', 'Batterie', 'Bébé', 'Beethoven', 'Bête', 'Biberon', 'Bière', 'Blanc', 'Blé', 'Bleu', 'Bob', 'Boisson', 'Boîte', 'Bombe', 'Bonbon', 'Bonnet', 'Bord', 'Bordeaux', 'Botte', 'Boue', 'Bougie', 'Boule', 'Bouteille', 'Bouton', 'Branche', 'Bras', 'Bravo', 'Bretagne', 'Brise', 'Brosse', 'Bruit', 'Brume', 'Brun', 'Bûche', 'Bulle', 'Bureau', 'But', 'Cabane', 'Cabine', 'Cacher', 'Cadeau', 'Cafard', 'Café', 'Caisse', 'Calculer', 'Calme', 'Caméra', 'Camion', 'Camping', 'Canada', 'Canard', 'Canette', 'Canine', 'Cap', 'Capitalisme', 'Car', 'Carotte', 'Carré', 'Carte', 'Carton', 'Casque', 'Casser', 'Cassette', 'Cauchemar', 'Cause', 'Ceinture', 'Cellule', 'Cercle', 'Chaîne', 'Chair', 'Chaise', 'Champ', 'Champion', 'Chant', 'Chapeau', 'Charbon', 'Charge', 'Chasse', 'Chat', 'Château', 'Chaud', 'Chaussure', 'Chauve', 'Chef', 'Chemise', 'Chêne', 'Cher', 'Cheval', 'Chevalier', 'Cheveu', 'Chien', 'Chiffre', 'Chine', 'Chocolat', 'Chômage', 'Ciel', 'Cil', 'Cinéma', 'Cire', 'Cirque', 'Citron', 'Clé', 'Clou', 'Clown', 'Coach', 'Coccinelle', 'Code', 'Cœur', 'Col', 'Colle', 'Colline', 'Colonne', 'Cône', 'Confort', 'Continu', 'Contre', 'Conversation', 'Copain', 'Coq', 'Coquillage', 'Corbeau', 'Corde', 'Corps', 'Côte', 'Coude', 'Couloir', 'Coup', 'Cour', 'Courant', 'Courrier', 'Cours', 'Course', 'Court', 'Couteau', 'Couvert', 'Couverture', 'Cowboy', 'Crac', 'Crayon', 'Crème', 'Critique', 'Crochet', 'Croix', 'Croûte', 'Cuillère', 'Cuir', 'Cuisine', 'Culotte', 'Cycle', 'Dard', 'Dé', 'Debout', 'Défaut', 'Dehors', 'Démocratie', 'Dent', 'Dentiste', 'Dessin', 'Devoir', 'Diamant', 'Dictionnaire', 'Dieu', 'Dinosaure', 'Discours', 'Disque', 'Dix', 'Docteur', 'Doigt', 'Domino', 'Dormir', 'Droit', 'Eau', 'Échec', 'Échelle', 'Éclair', 'École', 'Écran', 'Écraser', 'Écrit', 'Église', 'Égout', 'Électricité', 'Éléphant', 'Élève', 'Elfe', 'Empreinte', 'Enceinte', 'Épice', 'Épine', 'Erreur', 'Espace', 'Espion', 'Essence', 'État', 'Été', 'Étoile', 'Étranger', 'Éventail', 'Évolution', 'Explosoin', 'Extension', 'Face', 'Fan', 'Farce', 'Fatigue', 'Fauteuil', 'Femme', 'Fenêtre', 'Fer', 'Fête', 'Feu', 'Feuille', 'Fidèle', 'Fil', 'Fille', 'Flamme', 'Flèche', 'Fleur', 'Fleuve', 'Fond', 'Football', 'Forêt', 'Forger', 'Foudre', 'Fouet', 'Four', 'Fourmi', 'Froid', 'Fromage', 'Front', 'Fruit', 'Fuir', 'Futur', 'Garçon', 'Gâteau', 'Gauche', 'Gaz', 'Gazon', 'Gel', 'Genou', 'Glace', 'Gomme', 'Gorge', 'Goutte', 'Grand', 'Grèce', 'Grenouille', 'Grippe', 'Gris', 'Gros', 'Groupe', 'Guitare', 'Hasard', 'Haut', 'Hélicoptère', 'Herbe', 'Heureux', 'Histoire', 'Hiver', 'Hôtel', 'Huile', 'Humide', 'Humour', 'Indice', 'Internet', 'Inviter', 'Italie', 'Jacques', 'Jambe', 'Jambon', 'Jardin', 'Jaune', 'Jean', 'Jeanne', 'Jet', 'Jeu', 'Jogging', 'Jour', 'Journal', 'Jupiter', 'Kilo', 'Kiwi', 'Laine', 'Lait', 'Langue', 'Lapin', 'Latin', 'Laver', 'Lecteur', 'Léger', 'Lent', 'Lettre', 'Lien', 'Ligne', 'Linge', 'Lion', 'Lit', 'Livre', 'Loi', 'Long', 'Louis', 'Loup', 'Lumière', 'Lundi', 'Lune', 'Lunette', 'Machine', 'Macho', 'main', 'Maison', 'Maîtresse', 'Mal', 'Maladie', 'Maman', 'Mammouth', 'Manger', 'Marais', 'Marc', 'Marche', 'Mariage', 'Marie', 'Mariée', 'Marque', 'Marseille', 'Masse', 'Mer', 'Messe', 'Mètre', 'Métro', 'Miaou', 'Micro', 'Mieux', 'Mille', 'Mine', 'Miroir', 'Moderne', 'Moitié', 'Monde', 'Monstre', 'Montagne', 'Montre', 'Mort', 'Moteur', 'Moto', 'Mou', 'Mouche', 'Moulin', 'Moustache', 'Mouton', 'Mur', 'Muscle', 'Musique', 'Mystère', 'Nage', 'Nature', 'Neige', 'Neutre', 'New\xa0York', 'Nez', 'Nid', 'Ninja', 'Niveau', 'Noël', 'Nœud', 'Noir', 'Nous', 'Nuage', 'Nuit', 'Numéro', 'Œil', 'Œuf', 'Oiseau', 'Olympique', 'Ombre', 'Ongle', 'Or', 'Oral', 'Orange', 'Ordinateur', 'Ordre', 'Ordure', 'Oreille', 'Organe', 'Orgueil', 'Ours', 'Outil', 'Ouvert', 'Ovale', 'Pain', 'Palais', 'Panneau', 'Pantalon', 'Pantin', 'Papa', 'Papier', 'Papillon', 'Paradis', 'Parc', 'Paris', 'Parole', 'Partie', 'Passe', 'Pâte', 'Patin', 'Patte', 'Paul', 'Payer', 'Pêche', 'Peinture', 'Pendule', 'Penser', 'Personne', 'Petit', 'Peur', 'Philosophe', 'Photo', 'Phrase', 'Piano', 'Pièce', 'Pied', 'Pierre', 'Pile', 'Pilote', 'Pince', 'Pioche', 'Pion', 'Pirate', 'Pire', 'Piscine', 'Place', 'Plafond', 'Plage', 'Plaie', 'Plan', 'Planche', 'Planète', 'Plante', 'Plastique', 'Plat', 'Plat', 'Plomb', 'Plonger', 'Pluie', 'Poche', 'Poète', 'Poids', 'Poing', 'Point', 'Poivre', 'Police', 'Politique', 'Pollen', 'Polo', 'Pomme', 'Pompe', 'Pont', 'Population', 'Port', 'Porte', 'Portefeuille', 'Positif', 'Poste', 'Poubelle', 'Poule', 'Poupée', 'Pousser', 'Poussière', 'Pouvoir', 'Préhistoire', 'Premier', 'Présent', 'Presse', 'Prier', 'Princesse', 'Prise', 'Privé', 'Professeur', 'Psychologie', 'Public', 'Pull', 'Punk', 'Puzzle', 'Pyjama', 'Quatre', 'Quinze', 'Race', 'Radio', 'Raisin', 'Rap', 'Rayé', 'Rayon', 'Réfléchir', 'Reine', 'Repas', 'Reptile', 'Requin', 'Rêve', 'Riche', 'Rideau', 'Rien', 'Rire', 'Robinet', 'Roche', 'Roi', 'Rond', 'Rose', 'Roue', 'Rouge', 'Rouille', 'Roux', 'Russie', 'Sable', 'Sabre', 'Sac', 'Sain', 'Saison', 'Sale', 'Salle', 'Salut', 'Samu', 'Sandwich', 'Sang', 'Sapin', 'Satellite', 'Saumon', 'Saut', 'Savoir', 'Schtroumpf', 'Science', 'Scout', 'Sec', 'Seine', 'Sel', 'Sept', 'Serpent', 'Serrer', 'Sexe', 'Shampooing', 'Siècle', 'Siège', 'Sieste', 'Silhouette', 'Sirène', 'Ski', 'Soleil', 'Sommeil', 'Son', 'Sonner', 'Sorcière', 'Sourd', 'Souris', 'Sport', 'Star', 'Station', 'Stylo', 'Sur', 'Surface', 'Sushi', 'Swing', 'Tableau', 'Tache', 'Taille', 'Tante', 'Tapis', 'Tard', 'Taxi', 'Téléphone', 'Télévision', 'Temple', 'Temps', 'Tennis', 'Tête', 'Thé', 'Tigre', 'Tintin', 'Tissu', 'Titre', 'Titre', 'Toast', 'Toilette', 'Tokyo', 'Tombe', 'Ton', 'Top', 'Touche', 'Toujours', 'Tour', 'Tournoi', 'Tout', 'Trace', 'Train', 'Traîner', 'Transport', 'Travail', 'Trésor', 'Triangle', 'Triste', 'Trône', 'Troupeau', 'Tsar', 'Tube', 'Tuer', 'Tuer', 'Tupperware', 'Tuyau', 'Twitter', 'Type', 'Université', 'Vache', 'Vache', 'Vague', 'Vaisselle', 'Valeur', 'Ver', 'Verdict', 'Verre', 'Vers', 'Vert', 'Veste', 'Viande', 'Vide', 'Vie', 'Vieux', 'Ville', 'Vin', 'Vingt', 'Violon', 'Vipère', 'Vision', 'Vite', 'Vive', 'Vœu', 'Voile', 'Voisin', 'Voiture', 'Vol', 'Volume', 'Vote', 'Vouloir', 'Voyage', 'Zen', 'Zéro', 'Zodiaque', 'Zone', 'Zoo']
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def bonjour():
    """Says Hello World"""
    await bot.say("Salut")

#code_names

def code_names_init():
    game=[]
    noms=NOMS
    while len(game)<25:
        k=randint(0,len(noms)-1)
        game.append(noms[k])
        game=list(set(game))
    taille=0
    for x in game:
        taille=max(taille,len(x))
    for i in range(len(game)):
        while len(game[i])<taille:
            game[i]=game[i]+' '
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
async def code_names(espion1 : discord.Member, espion2 : discord.Member, chan : discord.Channel):
    """Allow to play to Code Names"""
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
    await bot.send_message(espion1,'Voici la grille à faire deviner :\n'+affichage_grille)
    await bot.send_message(espion2,'Voici la grille à faire deviner :\n'+affichage_grille)
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
            await bot.say("Tour Bleu")
        await bot.say("combien de cases ?")
        k=(await bot.wait_for_message(channel=chan))
        while k.author == bot.nom:
            k=(await bot.wait_for_message(channel=chan))
        nombre = int(k.content)
        for k in range(nombre):
            await bot.say("Quelle ligne ?")
            t=(await bot.wait_for_message(channel=chan))
            while t.author == bot.nom:
                t=(await bot.wait_for_message(channel=chan))
            i = int(t.content)-1
            await bot.say("Quelle colonne ?")
            t=(await bot.wait_for_message(channel=chan))
            while t.author == bot.nom:
                t=(await bot.wait_for_message(channel=chan))
            j = int(t.content)-1
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
                await bot.say("Les bleus ont gagné !")
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

#productions

mat = []
mat2 = []

for i in range(0,56):
    mat.append([])
    mat2.append([])
    for j in range(0,56):
        mat[i].append(0)
    for k in range(0,24):
        mat2[i].append(False)


nom=["viande","poisson","pain","fruit","legume","fromage","miel","lait","oeuf","epice","tonneau","bouteille_vin","bouteille_cidre","bijoux","poterie","vetement","bougie","livre","parfum","fourrure","teinture","potion","plante","cire","encre","perle","armure","arme","tunique","arc","arme de siege","navire de guerre","bois","bois precieux","peau","cuir","pierre","gemme","argile","fer","corde","fleur","foin","ble","farine","orge","lin","chanvre","chevre","vache","poule","chevaux","bateau","navire de fret","charrette","zeppelin"]

def cherche(char):
    for i in range(0,len(nom)):
        if nom[i] == char:
            return(i)
    return(len(nom)+1)


mat[1][cherche("bateau")] = 0.01
mat[2][cherche("farine")] = 1
mat[cherche("fromage")][cherche("chevre")] = 0.01
mat[cherche("lait")][cherche("vache")] = 0.01
mat[cherche("oeuf")][cherche("poule")] = 0.02
mat[cherche("epice")][cherche("navire de fret")] = 0.005
mat[cherche("tonneau")][cherche("orge")] = 5
mat[cherche("bouteille_vin")][cherche("fruit")] = 10
mat[cherche("bouteille_cidre")][cherche("fruit")] = 10
mat[cherche("bijoux")][cherche("gemme")] = 5
mat[cherche("bijoux")][cherche("bois precieux")] = 5
mat[cherche("poterie")][cherche("argile")] = 10
mat[cherche("vetement")][cherche("lin")] = 5
mat[cherche("vetement")][cherche("teinture")] = 1
mat[cherche("bougie")][cherche("cire")] = 3
mat[cherche("livre")][cherche("cuir")] = 5
mat[cherche("livre")][cherche("encre")] = 1
mat[cherche("parfum")][cherche("fleur")] = 10
mat[cherche("fourrure")][cherche("peau")] = 5
mat[cherche("teinture")][cherche("fleur")] = 5
mat[cherche("potion")][cherche("plante")] = 5
mat[cherche("encre")][cherche("perle")] = 5
mat[cherche("armure")][cherche("fer")] = 30
mat[cherche("arme")][cherche("fer")] = 20
mat[cherche("tunique")][cherche("cuir")] = 10
mat[cherche("arc")][cherche("bois")] = 10
mat[cherche("arme de siege")][cherche("bois")] = 100
mat[cherche("arme de siege")][cherche("corde")] = 100
mat[cherche("arme de siege")][cherche("fer")] = 100
mat[cherche("arme de siege")][cherche("pierre")] = 100
mat[cherche("navire de guerre")][cherche("bois")] = 600
mat[cherche("navire de guerre")][cherche("corde")] = 100
mat[cherche("navire de guerre")][cherche("fer")] = 200
mat[cherche("navire de guerre")][cherche("cuir")] = 200
mat[cherche("corde")][cherche("chanvre")] = 1
mat[cherche("farine")][cherche("ble")] = 1
mat[cherche("chevre")][cherche("foin")] = 200
mat[cherche("vache")][cherche("foin")] = 200
mat[cherche("poule")][cherche("legume")] = 50
mat[cherche("chevaux")][cherche("foin")] = 300
mat[cherche("bateau")][cherche("bois")] = 100
mat[cherche("bateau")][cherche("corde")] = 100
mat[cherche("navire de fret")][cherche("bois")] = 300
mat[cherche("navire de fret")][cherche("corde")] = 100
mat[cherche("navire de fret")][cherche("fer")] = 100
mat[cherche("navire de fret")][cherche("cuir")] = 200
mat[cherche("charrette")][cherche("bois")] = 50
mat[cherche("charrette")][cherche("corde")] = 10
mat[cherche("charrette")][cherche("fer")] = 50
mat[cherche("charrette")][cherche("chevaux")] = 1
mat[cherche("zeppelin")][cherche("bois")] = 100
mat[cherche("zeppelin")][cherche("corde")] = 400
mat[cherche("zeppelin")][cherche("fer")] = 100
mat[cherche("zeppelin")][cherche("cuir")] = 600

def quoi(ressource):
    liste=mat[cherche(ressource)]
    liste_i=[]
    for i in range(0,56):
        if liste[i] != 0:
            liste_i.append((i,liste[i]))
    return(liste_i)

mat2[cherche("viande")][22] = True
mat2[cherche("poisson")][19] = True
mat2[cherche("pain")][3] = True
mat2[cherche("fruit")][22] = True
mat2[cherche("legume")][10] = True
mat2[cherche("fromage")][0] = True
mat2[cherche("miel")][9] = True
def ajoute(char,l):
    for i in range(0,len(l)):
        mat2[cherche(char)][l[i]-1] = True

ajoute("lait",[7])
ajoute("oeuf",[22])
ajoute("epice",[12])
ajoute("tonneau",[3])
ajoute("bouteille_vin",[21])
ajoute("bouteille_cidre",[14])
ajoute("bijoux",[19])
ajoute("poterie",[18])
ajoute("vetement",[8])
ajoute("bougie",[2])
ajoute("livre",[5])
ajoute("parfum",[12])
ajoute("fourrure",[3])
ajoute("teinture",[5])
ajoute("potion",[6])
ajoute("plante",[16])
ajoute("cire",[10])
ajoute("encre",[14])
ajoute("perle",[20])
ajoute("armure",[4,15,17])
ajoute("arme",[3,15,17])
ajoute("tunique",[6,19,21])
ajoute("arc",[6,18,23])
ajoute("arme de siege",[15])
ajoute("navire de guerre",[20])
ajoute("bois",[24])
ajoute("bois precieux",[10])
ajoute("peau",[18])
ajoute("cuir",[24])
ajoute("pierre",[7,13])
ajoute("gemme",[13])
ajoute("argile",[19])
ajoute("fer",[9,13,14])
ajoute("corde",[22])
ajoute("fleur",[24])
ajoute("foin",[9,11])
ajoute("ble",[11])
ajoute("farine",[8])
ajoute("orge",[9])
ajoute("lin",[22])
ajoute("chanvre",[16])
ajoute("chevre",[7])
ajoute("vache",[1])
ajoute("poule",[16])
ajoute("chevaux",[2,17])
ajoute("bateau",[12])
ajoute("navire de fret",[8])
ajoute("charrette",[4])
ajoute("zeppelin",[5])

def ou(char):
    l=[]
    for i in range(0,24):
        if mat2[cherche(char)][i] == True:
            l.append(i)
    return(l)
    
def liste(n):
    l1=[]
    for i in range(0,len(mat2)):
        if mat2[i][n] == True :
            l1.append(i)
    return(l1)

# =============================================================================
# orge,pierre,peau,lin,oeuf,perle : 1/2 partisans
# fer,foin,argile,ble,legume,bois,cuir,fleur,fruit,viande,cordes,bougie,farine,pain,poterie,teinture,lait,fromage,vetement,parfum,epice,bouteille vin, bouteille cidre,poisson,fourrures,tonneaux,bijoux,encre: partisans
# arc,tunique,gemme,arme,armure,poule,livre : 1/5 partisans
# arme de siege,zeppelin,navire de fret,navire de guerre : 1/100
# plante : 1/3
# bateau : 1/20
# orge,pierre,peau,lin,fer,foin,argile,ble,legume,bois,cuir,fleur,fruit,viande,cordes,bougie,farine,pain,poterie,arc,tunique,gemme,arme,armure 

# =============================================================================
def appartient(l,n):
    for x in l:
        if x == n:
            return(True)
    return(False)

def liste_terr(lieu,li):
    l=[lieu]
    l1=liste(lieu)
    for x in l1:
        l2 = quoi(nom[x])
        for y in l2:
            a,b=y
            where=ou(nom[a])
            if appartient(l,where[0]) == False and appartient(li,where[0]) == False:
                l = liste_terr(where[0],li+l) + l
    return(l)

coef=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.2,1,1,1,1,0.33,0.5,1,0.5,0.2,0.2,0.2,0.2,0.01,0.01,1,0.5,0.5,1,0.5,0.2,1,1,1,1,1,1,1,0.5,0.5,1,0.1,0.1,0.2,0.1,0.05,0.1,0.05,0.01]
coef[33]=0.33

def desactive(list_desactive):
    global desactiver
    desactiver = list_desactive.split(' ')

def list_terr2(lieu,i,lieu2,test_3):
    l1=liste(lieu)
    if lieu == lieu2:
        test_3[lieu] = i
    faire=[]
    for x in l1:
        l2 = quoi(nom[x])
        for y in l2:
            a,b=y
            where=ou(nom[a])
            if appartient(desactiver,nom[a]) == False and appartient(desactiver,nom[x]) == False:
                if (where[0] != 0 or test_3[0] == 0) and (where[0] != 6 or test_3[6] == 0)and where[0] != lieu2:
                    if appartient(faire,where[0]) == False:
                        faire.append(where[0])
                        test_3[where[0]] += i*coef[x]*mat[x][a]/coef[a]
                    else:
                        test_3[where[0]] = max(i*coef[x]*mat[x][a]/coef[a],test_3[where[0]],1)    
                    test_3[where[0]] = math.ceil(test_3[where[0]])
            else:
                break
    l=[]
    for x in faire:
        copie=copy.deepcopy(test_3)
        l.append(list_terr2(x,test_3[x],lieu2,copie))
    if faire != []:
        for i in range(0,24):
            m=l[0][i]
            for k in range(0,len(l)):
                m = max(m,l[k][i])
                test_3[i] = m
    return(test_3)

def plus_facile(test_3):
    l=[]
    for i in range(0,24):
        if test_3[i] != 0:
            l.append((i+1,test_3[i]))
    return(l)

@bot.command()
async def productions(i,nb,list_desactive):
    """Allow to know the best number of productions"""
    global test
    test=[0]*24
    desactive(list_desactive)
    h=plus_facile(list_terr2(int(i)-1,int(nb),int(i)-1,test))
    message=""
    for k in h:
        a,b=k
        message=message+str(b)+" productions sur le "+str(a)+"\n"
    await bot.say(message)



bot.run(TOKEN)
        