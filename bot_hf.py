from random import randint
import discord
from discord.ext import commands
import os

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
async def code_names(espion1 : discord.Member, espion2 : discord.Member):
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
        