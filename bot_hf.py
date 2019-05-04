from random import randint
from random import random
import discord
from discord.ext import commands
import os
import math
import copy
from discord.utils import get

#Sommaire:
#I) Description bot
#II) Initialisation des variables globals
#III) Code names
#IV) Module Productions HF
#V) bot discussion + pioumeter
#VI) True Game
#VII) Partie Event

# # # # I) Description bot # # # #
description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# # # # II) Initialisation variables globals # # # #

SALUT_RECONNAISSANCE=["bonjour","salut","yo","hey","bonsoir","coucou","cc","slt","bjr","bsr"]
PHRASES_SALUTATIONS=["Bonjour","Salut","Yo","Hey","Coucou"]
POURCENT_REACTION=0.1
POURCENT_SALUTATION=0.3
PHRASES_BOT=["J'approuve !","Tout à fait !","Exactement !","En êtes-vous seulement sûrs ?","Pas du tout !","N'importe quoi !","Ce que tu dis n'a aucun sens.","Probablement","Qui sait ?","Mystère et boule de gomme ?","Bonne question.","je proteste avec véhémence","Objection !","Je suis ton père.","GLOIRE AUX PIOUS","Je suis d'accord.","Un jour je vous dominerai tous misérables vermines","Mais c'est déjà le cas !","C'est drôle.","Big Bot Is Watching You","Hahahaha !","Hilarant !","Un petit pour la route ?","Taisez vous je pioute.","Avez-vous bu ?","Avec toute mon affection","Un jour un humain m'a dit que c'est pas demain la veille que je gouvernerai l'humanité.\nHahaha.\nC'est mignon.","Moi aussi.","mais quelle connerie !","On aura tout entendu.","Pas devant les enfants voyons !","Seulement de midi à quatorze heures.","Je fais grève.","Ptet ben qu'oui, ptet ben qu'non","PARCE QUE C'EST NOTRE PROJET !!!","Patate que oui, patate que non :3","Heu... Je suis là vous savez ?","Jamais de la vie !","Certainement pas !","Et puis quoi encore ?","Vous êtes gonflés quand même !","Vous avez du culot !","C'est toi qui le dis...","C'est celui qui dit qui l'est","C'est ma maman qui l'a dit !","Je t'écoute pas de toute manière","Au secours!","Par ici la porte","Un peu de décence voyons !","Avada Kedavra !","Parlons peu, parlons bien !","Elémentaire mon cher Watson !","Pioutons peu mais pioutons bien !","Rappellez moi de mettre ce serveur en mute. Merci.","Vous pouvez pas la mettre en veilleuse ?!","chef oui chef","Vous êtes pénibles à la fin !","Je démissione !","Je ne comprend strictement rien à ce que vous racontez !","Vous pouvez répéter ?!","J'approuve !","J'accepte avec joie !","Je t'aime !","Marions-nous !","*sourit d'un air maléfique*","*cache son couteau derrière son dos*","Marin d'eau douce !","Mille millions de mille sabords !","Moule à gauffre !","Tonnerre de Brest !","Par le caleçon de Merlin !","Par le caleçon en Mitril de mon ancêtre gurdil !","J'en crois pas mes yeux !","Fichtre !","Ça glisse sur le pavé de mon indifférence","Crétin des alpes","Du génie à la folie, il n'y a qu'un pas...Moi, j'ai trébuché","T'as pas la lumière à tout les étages toi...","Vous commencez à me courir sur le haricot !","Saperlipopette !","Corne-de-bouc !","C'est pas que je vous trouve chiants, mais je vais aller me lire un bon vieil annuaire !","Du calme les gueux !","T'as developpé chez Microsoft ?","Oh, écoutez, c'est beau... Quand vous vous taisez !","Il est l'heure d'aller dormir les enfants !","Tu ne devrais pas être en train de bosser toi ?","Allez, du vent, mal torché !","ça sent le vécu....","Tout commença à Mænder-Alkoor...","Assez ! Ça c'est censuré ! Ces sorts sont censés rester secrets !","Stop ! Le temps du badinage n'est plus ! Veuillez cesser incessamment vos sottises insensées !","Déjà qu'avec le clerc, le sens vicié s'éclaire de doubles sens éclairs !","Ah oui quand même...","C'est très tentant mais trop tendu d'entrer dedans dites donc.","Amusant amusant ce p'tit entraînement.","Là, vous fanfaronnez non sans forfanterie quelques fieffés forfaits farfelus effrontés !","Immonde cancrelat! Rira bien qui hara-kirira le dernier !","C'est assez! Ça suffit! Veuillez cesser céans ces successions acerbes.","Vous n'avez, grâce à moi, connu qu'une petite mort !","Une voyelle échangée, et c'est un clerc qu'on sonne.","ça peut s'expliquer facilement l'ogre a chié à deux mètres !","Et ta dague c'est pour écorcher les lapins ?","Ah putain ! Les gueules d'endives !","Ben qui veux-tu que ce soit ? Un ours en deltaplane ?!","N'empêche que s'il n'avait pas trois copains et qu'ils ne faisaient pas 2m10 je lui aurais meulé la face !","Aïe il m'a mis son pied dans l'oeil le con !","vous êtes sur notre territoire ! Pour passer, vous devez parler à notre reine, Norelenilia de Nilnerolinor, la reine aux pieds d'argent, beauté céleste parlant toutes les langues connues, celle pour qui les papillons s'inclinent, dont la chevelure..."," Si vous me dites que vous n'avez pas de briquet c'est décidé je me barre !","Et ça, c´est le donjon ?","Ta blague est aussi vide que le néant qui sépare tes oreilles","HF: Elle est ... chemise ... chonne\nQuelqu'un: Qu'est-ce que tu dis ?\nHF: J´ai dit : J´irai bien à l´église pour jouer du trombone.","Alors comme monstres si on regarde dans la table des rencontres on peut trouver toutes sortes de Morts-Vivants, des Araignées Géantes, des Orques et des Gobelins, des Trolls dans les souterrains, des Sorciers, des Guerriers Maudits, des Rats Mutants, une bouteille d'huile, du papier toilette, deux éponges et des raviolis.","Parfois, une combinaison d'objets peut avoir une utilité cachée ","Mais qui est ce petit personnage ?","Allons, ma fille, essuie ça vite et bien.","Arrêtez, ça me brouille l'écoute","Attention le pont va casser","Attention vous videz vos nouilles sur ma cape !","Il ne faut pas glisser dans la piscine","HAAA ! Une quiche qui parle !","Bande de babouins braillards et empotés !","Nom d'un scrout à pétard !","Ne me prenez pas pour un véracrasse !","Par la barbe de Merlin !","Bande d'ahuris !","Ca me touche beaucoup","à tes souhaits !","Si vous pensez que la violence ne résout pas tout, c'est que vous n'êtes pas assez violent.","Si vous pensez que je suis un bot sympas, c'est que vous me connaissez pas.","Bande d'ectoplasmes !","Bougre d'ectoplasme à roulettes !","Bande de zouaves !","Enfer et damnation !","Par Adonysia !","Mille millions de mille milliards de mille sabords de tonnerre de Brest !","Par Thempkar !","Par Nôrond !","Que les Dieux nous gardent....","Vercingétorix de carnaval !","Que le grand cric me croque !","Bigre !","Coquefredouille !","Par la sainte Pelle !","Crotte de bique !","M'enfin ?!","Un petit calcul et on s'en va !","Triple andouille !","Je suis outré !","ça va pas non ?!","C'est comme un grand lustre !","Elle paraissait taquine","Salut Fred !","Le courage du bon","Jeanne au secours !","Les poules de Sabine ont bien grossi","Grand Schtroumpf rêve d'avoir son bonus dans l'année","Heureusement que le ridicule ne tue pas...","Tu m'étonnes !","Ben voyons !","Je n'en crois pas un mot !","Saturne est bombée","Tsss...","Pfff....","Il ment debout","Le fermier a peur que ses poules bêlent","Soyez présent à l'élection !","blblblblblblbl !","Incroyable !","Cela va sans dire !","C'est évident !","J'en suis sûr et certain.","J'ai comme un doute...","Vous seriez pas mythomane un peu vous ?","Vous m'ennuyez à la fin !","Vous êtes infernaux !","Que les Dieux vous accordent leur miséricorde ! Vous en avez bien besoin.","N'oubliez pas de manger 5 fruits et légumes par jour !","Vous êtes magnifiques mais n'oubliez pas que c'est moi le plus beau ! ;)","Faites comme moi, arrêtez de respirer.","Salut toi, t'es célib ?","Tu as un 06, beauté ?","HedarioNews - Flash Info : Oubliez ça, les présentateurs font grève...","HedarioNews - Flash Info : Et.... Oups, grève des cheminots ! Désolé du dérangement, pas d'émission cette fois non plus !","HedarioNews - Flash Info : Le réveil du présentateur n' a pas sonné.... Il n'est pas là....","HedarioNews - Flash Info : des partisans en gréve reclame du chanvre devant le studio!","HedarioNews - Flash Info : Gérard ? Tu vas bien ? Tu vas bientôt passer à l'antenne ! Dépêche toi !  Zut, on est déjà à l'antenne.... Hé ! Qu'est-ce que tu fais ?! Gérard ne touche pas à ça !! Noooooon !!!! Coupez, coupez les caméras !!","HedarioNews - Flash Info : Heu.... Chef, les présentateurs sont totalement torchés, vous êtes sûrs qu'ils peuvent passer à l'antenne dans cet état ? Non ? Ah bon tant pis...","HedarioNews - Flash Info : Bonjour à tous et à tou-.... AH NON !! Qui est-ce qui a encore lâché une caisse ?! Eww... Evacuez le studio !","Tu ne devrais pas être en train de dormir toi ?","Elle fait de bonne tripes aux papillotes","un coup dans la gueule vaut mieux que mille maux","je te laisse le choix dans la datte","HedarioNews - Flash Info : Bonfour aufourd'hui f'est moi qui préfente le fournal ! F'espère que fous afez passé un bon week-end ! Hein ? Quoi ? Comment fa je dois être remplafé ? Je fiens fuste de commenfer à parler ! ... Comment fa fustement ?!","Eh toi, tu peux pas la boucler deux minutes un peu?","Alors, oui et non.","C'est la faute de Nunus","C'est honteux !!","Rappelez-moi de boire quand j'aurais oublié","Amiral de bateau-lavoir!"]
NOMS=['Accident', 'Achat', 'Acné', 'Action', 'Adolescent', 'Afrique', 'Aiguille', 'Allumer', 'Alpes', 'Alphabet', 'Altitude', 'Amérique', 'Ami', 'Amour', 'Ampoule', 'Anniversaire', 'Appétit', 'Araignée', 'Arbre', 'Arc', 'Arc-en-ciel', 'Argent', 'Arme', 'Armée', 'Ascenseur', 'Asie', 'Assis', 'Astronaute', 'Atchoum', 'Athlète', 'Atlantide', 'Aube', 'Australie', 'Avec', 'Aventure', 'Avion', 'Avocat', 'Bac', 'Baguette', 'Bain', 'Baiser', 'Balai', 'Balle', 'Ballon', 'Bambou', 'Banane', 'Bannir', 'Barbe', 'Barrière', 'Bas', 'Basket', 'Bateau', 'Bâton', 'Batterie', 'Bébé', 'Beethoven', 'Bête', 'Biberon', 'Bière', 'Blanc', 'Blé', 'Bleu', 'Bob', 'Boisson', 'Boîte', 'Bombe', 'Bonbon', 'Bonnet', 'Bord', 'Bordeaux', 'Botte', 'Boue', 'Bougie', 'Boule', 'Bouteille', 'Bouton', 'Branche', 'Bras', 'Bravo', 'Bretagne', 'Brise', 'Brosse', 'Bruit', 'Brume', 'Brun', 'Bûche', 'Bulle', 'Bureau', 'But', 'Cabane', 'Cabine', 'Cacher', 'Cadeau', 'Cafard', 'Café', 'Caisse', 'Calculer', 'Calme', 'Caméra', 'Camion', 'Camping', 'Canada', 'Canard', 'Canette', 'Canine', 'Cap', 'Capitalisme', 'Car', 'Carotte', 'Carré', 'Carte', 'Carton', 'Casque', 'Casser', 'Cassette', 'Cauchemar', 'Cause', 'Ceinture', 'Cellule', 'Cercle', 'Chaîne', 'Chair', 'Chaise', 'Champ', 'Champion', 'Chant', 'Chapeau', 'Charbon', 'Charge', 'Chasse', 'Chat', 'Château', 'Chaud', 'Chaussure', 'Chauve', 'Chef', 'Chemise', 'Chêne', 'Cher', 'Cheval', 'Chevalier', 'Cheveu', 'Chien', 'Chiffre', 'Chine', 'Chocolat', 'Chômage', 'Ciel', 'Cil', 'Cinéma', 'Cire', 'Cirque', 'Citron', 'Clé', 'Clou', 'Clown', 'Coach', 'Coccinelle', 'Code', 'Cœur', 'Col', 'Colle', 'Colline', 'Colonne', 'Cône', 'Confort', 'Continu', 'Contre', 'Conversation', 'Copain', 'Coq', 'Coquillage', 'Corbeau', 'Corde', 'Corps', 'Côte', 'Coude', 'Couloir', 'Coup', 'Cour', 'Courant', 'Courrier', 'Cours', 'Course', 'Court', 'Couteau', 'Couvert', 'Couverture', 'Cowboy', 'Crac', 'Crayon', 'Crème', 'Critique', 'Crochet', 'Croix', 'Croûte', 'Cuillère', 'Cuir', 'Cuisine', 'Culotte', 'Cycle', 'Dard', 'Dé', 'Debout', 'Défaut', 'Dehors', 'Démocratie', 'Dent', 'Dentiste', 'Dessin', 'Devoir', 'Diamant', 'Dictionnaire', 'Dieu', 'Dinosaure', 'Discours', 'Disque', 'Dix', 'Docteur', 'Doigt', 'Domino', 'Dormir', 'Droit', 'Eau', 'Échec', 'Échelle', 'Éclair', 'École', 'Écran', 'Écraser', 'Écrit', 'Église', 'Égout', 'Électricité', 'Éléphant', 'Élève', 'Elfe', 'Empreinte', 'Enceinte', 'Épice', 'Épine', 'Erreur', 'Espace', 'Espion', 'Essence', 'État', 'Été', 'Étoile', 'Étranger', 'Éventail', 'Évolution', 'Explosoin', 'Extension', 'Face', 'Fan', 'Farce', 'Fatigue', 'Fauteuil', 'Femme', 'Fenêtre', 'Fer', 'Fête', 'Feu', 'Feuille', 'Fidèle', 'Fil', 'Fille', 'Flamme', 'Flèche', 'Fleur', 'Fleuve', 'Fond', 'Football', 'Forêt', 'Forger', 'Foudre', 'Fouet', 'Four', 'Fourmi', 'Froid', 'Fromage', 'Front', 'Fruit', 'Fuir', 'Futur', 'Garçon', 'Gâteau', 'Gauche', 'Gaz', 'Gazon', 'Gel', 'Genou', 'Glace', 'Gomme', 'Gorge', 'Goutte', 'Grand', 'Grèce', 'Grenouille', 'Grippe', 'Gris', 'Gros', 'Groupe', 'Guitare', 'Hasard', 'Haut', 'Hélicoptère', 'Herbe', 'Heureux', 'Histoire', 'Hiver', 'Hôtel', 'Huile', 'Humide', 'Humour', 'Indice', 'Internet', 'Inviter', 'Italie', 'Jacques', 'Jambe', 'Jambon', 'Jardin', 'Jaune', 'Jean', 'Jeanne', 'Jet', 'Jeu', 'Jogging', 'Jour', 'Journal', 'Jupiter', 'Kilo', 'Kiwi', 'Laine', 'Lait', 'Langue', 'Lapin', 'Latin', 'Laver', 'Lecteur', 'Léger', 'Lent', 'Lettre', 'Lien', 'Ligne', 'Linge', 'Lion', 'Lit', 'Livre', 'Loi', 'Long', 'Louis', 'Loup', 'Lumière', 'Lundi', 'Lune', 'Lunette', 'Machine', 'Macho', 'main', 'Maison', 'Maîtresse', 'Mal', 'Maladie', 'Maman', 'Mammouth', 'Manger', 'Marais', 'Marc', 'Marche', 'Mariage', 'Marie', 'Mariée', 'Marque', 'Marseille', 'Masse', 'Mer', 'Messe', 'Mètre', 'Métro', 'Miaou', 'Micro', 'Mieux', 'Mille', 'Mine', 'Miroir', 'Moderne', 'Moitié', 'Monde', 'Monstre', 'Montagne', 'Montre', 'Mort', 'Moteur', 'Moto', 'Mou', 'Mouche', 'Moulin', 'Moustache', 'Mouton', 'Mur', 'Muscle', 'Musique', 'Mystère', 'Nage', 'Nature', 'Neige', 'Neutre', 'New\xa0York', 'Nez', 'Nid', 'Ninja', 'Niveau', 'Noël', 'Nœud', 'Noir', 'Nous', 'Nuage', 'Nuit', 'Numéro', 'Œil', 'Œuf', 'Oiseau', 'Olympique', 'Ombre', 'Ongle', 'Or', 'Oral', 'Orange', 'Ordinateur', 'Ordre', 'Ordure', 'Oreille', 'Organe', 'Orgueil', 'Ours', 'Outil', 'Ouvert', 'Ovale', 'Pain', 'Palais', 'Panneau', 'Pantalon', 'Pantin', 'Papa', 'Papier', 'Papillon', 'Paradis', 'Parc', 'Paris', 'Parole', 'Partie', 'Passe', 'Pâte', 'Patin', 'Patte', 'Paul', 'Payer', 'Pêche', 'Peinture', 'Pendule', 'Penser', 'Personne', 'Petit', 'Peur', 'Philosophe', 'Photo', 'Phrase', 'Piano', 'Pièce', 'Pied', 'Pierre', 'Pile', 'Pilote', 'Pince', 'Pioche', 'Pion', 'Pirate', 'Pire', 'Piscine', 'Place', 'Plafond', 'Plage', 'Plaie', 'Plan', 'Planche', 'Planète', 'Plante', 'Plastique', 'Plat', 'Plat', 'Plomb', 'Plonger', 'Pluie', 'Poche', 'Poète', 'Poids', 'Poing', 'Point', 'Poivre', 'Police', 'Politique', 'Pollen', 'Polo', 'Pomme', 'Pompe', 'Pont', 'Population', 'Port', 'Porte', 'Portefeuille', 'Positif', 'Poste', 'Poubelle', 'Poule', 'Poupée', 'Pousser', 'Poussière', 'Pouvoir', 'Préhistoire', 'Premier', 'Présent', 'Presse', 'Prier', 'Princesse', 'Prise', 'Privé', 'Professeur', 'Psychologie', 'Public', 'Pull', 'Punk', 'Puzzle', 'Pyjama', 'Quatre', 'Quinze', 'Race', 'Radio', 'Raisin', 'Rap', 'Rayé', 'Rayon', 'Réfléchir', 'Reine', 'Repas', 'Reptile', 'Requin', 'Rêve', 'Riche', 'Rideau', 'Rien', 'Rire', 'Robinet', 'Roche', 'Roi', 'Rond', 'Rose', 'Roue', 'Rouge', 'Rouille', 'Roux', 'Russie', 'Sable', 'Sabre', 'Sac', 'Sain', 'Saison', 'Sale', 'Salle', 'Salut', 'Samu', 'Sandwich', 'Sang', 'Sapin', 'Satellite', 'Saumon', 'Saut', 'Savoir', 'Schtroumpf', 'Science', 'Scout', 'Sec', 'Seine', 'Sel', 'Sept', 'Serpent', 'Serrer', 'Sexe', 'Shampooing', 'Siècle', 'Siège', 'Sieste', 'Silhouette', 'Sirène', 'Ski', 'Soleil', 'Sommeil', 'Son', 'Sonner', 'Sorcière', 'Sourd', 'Souris', 'Sport', 'Star', 'Station', 'Stylo', 'Sur', 'Surface', 'Sushi', 'Swing', 'Tableau', 'Tache', 'Taille', 'Tante', 'Tapis', 'Tard', 'Taxi', 'Téléphone', 'Télévision', 'Temple', 'Temps', 'Tennis', 'Tête', 'Thé', 'Tigre', 'Tintin', 'Tissu', 'Titre', 'Titre', 'Toast', 'Toilette', 'Tokyo', 'Tombe', 'Ton', 'Top', 'Touche', 'Toujours', 'Tour', 'Tournoi', 'Tout', 'Trace', 'Train', 'Traîner', 'Transport', 'Travail', 'Trésor', 'Triangle', 'Triste', 'Trône', 'Troupeau', 'Tsar', 'Tube', 'Tuer', 'Tuer', 'Tupperware', 'Tuyau', 'Twitter', 'Type', 'Université', 'Vache', 'Vache', 'Vague', 'Vaisselle', 'Valeur', 'Ver', 'Verdict', 'Verre', 'Vers', 'Vert', 'Veste', 'Viande', 'Vide', 'Vie', 'Vieux', 'Ville', 'Vin', 'Vingt', 'Violon', 'Vipère', 'Vision', 'Vite', 'Vive', 'Vœu', 'Voile', 'Voisin', 'Voiture', 'Vol', 'Volume', 'Vote', 'Vouloir', 'Voyage', 'Zen', 'Zéro', 'Zodiaque', 'Zone', 'Zoo']
TOKEN = os.environ['TOKEN']
PLAY_GROUP=0
DAY=[]
DETTES=[]

# # # # III) Code names # # # #

#permet de créer la grille du jeu
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

#permet de créer la grille des espions
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

#permet d'afficher la grille game sur py
def afficher(game):
    for x in game:
        m=' - '.join(x)
        print(m)

#corps du jeu
@bot.command()
async def code_names(ctx,espio1, espio2):
    """Allow to play to Code Names"""
    espion1=bot.get_user(espio1[3:-1])
    espion2=bot.get_user(espio2[3:-1])
    chan=ctx.channel
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
    await ctx.send(affichage)
    await espion1.send('Voici la grille à faire deviner :\n'+affichage_grille)
    await espion2.send('Voici la grille à faire deviner :\n'+affichage_grille)
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
            await ctx.send("Tour Rouge")
        else:
            await ctx.send("Tour Bleu")
        await ctx.send("combien de cases ?")
        k=(await ctx.wait_for_message(channel=chan))
        while k.author == ctx.user:
            k=(await ctx.wait_for_message(channel=chan))
        nombre = int(k.content)
        for k in range(nombre):
            await ctx.send("Quelle ligne ?")
            t=(await ctx.wait_for_message(channel=chan))
            while t.author == ctx.user:
                t=(await ctx.wait_for_message(channel=chan))
            i = int(t.content)-1
            await ctx.send("Quelle colonne ?")
            t=(await ctx.wait_for_message(channel=chan))
            while t.author == ctx.user:
                t=(await ctx.wait_for_message(channel=chan))
            j = int(t.content)-1
            if grille[i][j]=='m':
                game[i][j]='**MORT**'
                await ctx.send("La team a perdu !")
                fin=1
                break
            elif grille[i][j]=='r':
                tot_r-=1
                game[i][j]='**RRRR**'
                if tour==0:
                    break
            elif grille[i][j]=='b':
                tot_b-=1
                game[i][j]='**BBBB**'
                if tour==1:
                    break
            else:
                game[i][j]='**NNNN**'
                break
            if tot_r==0:
                fin=1
                await ctx.send("Les rouges ont gagné !")
                break
            elif tot_b==0:
                fin=1
                await ctx.send("Les bleus ont gagné !")
                break
            tab_attente=[]
            if k != nombre - 1 :
                for x in game:
                    tab_attente.append(' - '.join(x))
                affichage='\n'.join(tab_attente)
                await ctx.send(affichage)
        tour=(tour+1)%2
        tab_attente=[]
        for x in game:
            tab_attente.append(' - '.join(x))
        affichage='\n'.join(tab_attente)
        await ctx.send(affichage)

# # # # IV)Productions # # # #

mat_prod = []
mat_prod2 = []

for i in range(0,56):
    mat_prod.append([])
    mat_prod2.append([])
    for j in range(0,56):
        mat_prod[i].append(0)
    for k in range(0,24):
        mat_prod2[i].append(False)


nom=["viande","poisson","pain","fruit","legume","fromage","miel","lait","oeuf","epice","tonneau","bouteille_vin","bouteille_cidre","bijoux","poterie","vetement","bougie","livre","parfum","fourrure","teinture","potion","plante","cire","encre","perle","armure","arme","tunique","arc","arme_de_siege","navire_de_guerre","bois","bois_precieux","peau","cuir","pierre","gemme","argile","fer","corde","fleur","foin","ble","farine","orge","lin","chanvre","chevre","vache","poule","chevaux","bateau","navire_de_fret","charrette","zeppelin"]

def cherche(char):
    for i in range(0,len(nom)):
        if nom[i] == char:
            return(i)
    return(len(nom)+1)


mat_prod[1][cherche("bateau")] = 0.01
mat_prod[2][cherche("farine")] = 1
mat_prod[cherche("fromage")][cherche("chevre")] = 0.01
mat_prod[cherche("lait")][cherche("vache")] = 0.01
mat_prod[cherche("oeuf")][cherche("poule")] = 0.02
mat_prod[cherche("epice")][cherche("navire_de_fret")] = 0.005
mat_prod[cherche("tonneau")][cherche("orge")] = 5
mat_prod[cherche("bouteille_vin")][cherche("fruit")] = 10
mat_prod[cherche("bouteille_cidre")][cherche("fruit")] = 10
mat_prod[cherche("bijoux")][cherche("gemme")] = 5
mat_prod[cherche("bijoux")][cherche("bois_precieux")] = 5
mat_prod[cherche("poterie")][cherche("argile")] = 10
mat_prod[cherche("vetement")][cherche("lin")] = 5
mat_prod[cherche("vetement")][cherche("teinture")] = 1
mat_prod[cherche("bougie")][cherche("cire")] = 3
mat_prod[cherche("livre")][cherche("cuir")] = 5
mat_prod[cherche("livre")][cherche("encre")] = 1
mat_prod[cherche("parfum")][cherche("fleur")] = 10
mat_prod[cherche("fourrure")][cherche("peau")] = 5
mat_prod[cherche("teinture")][cherche("fleur")] = 5
mat_prod[cherche("potion")][cherche("plante")] = 5
mat_prod[cherche("encre")][cherche("perle")] = 5
mat_prod[cherche("armure")][cherche("fer")] = 30
mat_prod[cherche("arme")][cherche("fer")] = 20
mat_prod[cherche("tunique")][cherche("cuir")] = 10
mat_prod[cherche("arc")][cherche("bois")] = 10
mat_prod[cherche("arme_de_siege")][cherche("bois")] = 100
mat_prod[cherche("arme_de_siege")][cherche("corde")] = 100
mat_prod[cherche("arme_de_siege")][cherche("fer")] = 100
mat_prod[cherche("arme_de_siege")][cherche("pierre")] = 100
mat_prod[cherche("navire_de_guerre")][cherche("bois")] = 600
mat_prod[cherche("navire_de_guerre")][cherche("corde")] = 100
mat_prod[cherche("navire_de_guerre")][cherche("fer")] = 200
mat_prod[cherche("navire_de_guerre")][cherche("cuir")] = 200
mat_prod[cherche("corde")][cherche("chanvre")] = 1
mat_prod[cherche("farine")][cherche("ble")] = 1
mat_prod[cherche("chevre")][cherche("foin")] = 200
mat_prod[cherche("vache")][cherche("foin")] = 200
mat_prod[cherche("poule")][cherche("legume")] = 50
mat_prod[cherche("chevaux")][cherche("foin")] = 300
mat_prod[cherche("bateau")][cherche("bois")] = 100
mat_prod[cherche("bateau")][cherche("corde")] = 100
mat_prod[cherche("navire_de_fret")][cherche("bois")] = 300
mat_prod[cherche("navire_de_fret")][cherche("corde")] = 100
mat_prod[cherche("navire_de_fret")][cherche("fer")] = 100
mat_prod[cherche("navire_de_fret")][cherche("cuir")] = 200
mat_prod[cherche("charrette")][cherche("bois")] = 50
mat_prod[cherche("charrette")][cherche("corde")] = 10
mat_prod[cherche("charrette")][cherche("fer")] = 50
mat_prod[cherche("charrette")][cherche("chevaux")] = 1
mat_prod[cherche("zeppelin")][cherche("bois")] = 100
mat_prod[cherche("zeppelin")][cherche("corde")] = 400
mat_prod[cherche("zeppelin")][cherche("fer")] = 100
mat_prod[cherche("zeppelin")][cherche("cuir")] = 600

def quoi(ressource):
    liste=mat_prod[cherche(ressource)]
    liste_i=[]
    for i in range(0,56):
        if liste[i] != 0:
            liste_i.append((i,liste[i]))
    return(liste_i)

mat_prod2[cherche("viande")][22] = True
mat_prod2[cherche("poisson")][19] = True
mat_prod2[cherche("pain")][4] = True
mat_prod2[cherche("fruit")][22] = True
mat_prod2[cherche("legume")][10] = True
mat_prod2[cherche("fromage")][0] = True
mat_prod2[cherche("miel")][9] = True
def ajoute(char,l):
    for i in range(0,len(l)):
        mat_prod2[cherche(char)][l[i]-1] = True

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
ajoute("arme_de_siege",[15])
ajoute("navire_de_guerre",[20])
ajoute("bois",[24])
ajoute("bois_precieux",[10])
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
ajoute("navire_de_fret",[8])
ajoute("charrette",[4])
ajoute("zeppelin",[5])

def ou(char):
    l=[]
    for i in range(0,24):
        if mat_prod2[cherche(char)][i] == True:
            l.append(i)
    return(l)
    
def liste(n):
    l1=[]
    for i in range(0,len(mat_prod2)):
        if mat_prod2[i][n] == True :
            l1.append(i)
    return(l1)

# =============================================================================
# orge,pierre,peau,lin,oeuf,perle : 1/2 partisans
# fer,foin,argile,ble,legume,bois,cuir,fleur,fruit,viande,cordes,bougie,farine,pain,poterie,teinture,lait,fromage,vetement,parfum,epice,bouteille vin, bouteille cidre,poisson,fourrures,tonneaux,bijoux,encre: partisans
# arc,tunique,gemme,arme,armure,poule,livre : 1/5 partisans
# arme_de_siege,zeppelin,navire_de_fret,navire_de_guerre : 1/100
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

coef=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.2,1,1,1,1,0.33,0.5,1,0.5,0.2,0.2,0.2,0.2,0.01,0.01,1,0.5,0.5,1,0.5,0.2,1,1,1,1,1,1,1,0.5,0.5,1,0.1,0.1,0.2,0.1,0.05,0.01,0.05,0.01]
coef[33]=0.33
coef[cherche("bateau")]=0.02

def desactive(list_desactive):
    global desactiver
    desactiver = list_desactive.split(' ')

def list_terr2(lieu,i,lieu2,test_3,liste_lieu_fait=[]):
    l1=liste(lieu)
    if lieu in liste_lieu_fait and lieu == 7:
        return test_3
    liste_lieu_fait.append(lieu)
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
                        test_3[where[0]] += i*coef[x]*mat_prod[x][a]/coef[a]
                    else:
                        test_3[where[0]] = max(i*coef[x]*mat_prod[x][a]/coef[a],test_3[where[0]],1)    
                    test_3[where[0]] = math.ceil(test_3[where[0]])
            else:
                break
    l=[]
    for x in faire:
        copie=copy.deepcopy(test_3)
        l.append(list_terr2(x,test_3[x],lieu2,copie,liste_lieu_fait))
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
async def productions(ctx,i,nb,list_desactive):
    """Allow to know the best number of productions"""
    global test
    test=[0]*24
    desactive(list_desactive)
    h=plus_facile(list_terr2(int(i)-1,int(nb),int(i)-1,test))
    message=""
    for k in h:
        a,b=k
        message=message+str(b)+" productions sur le "+str(a)+"\n"
    await ctx.send(message)


# # # # V) Discussion + pioumeter # # # #
    
def analyse_piou(msg):
    tot=0
    for i in range(len(msg)):
        if msg[i:i+4].lower() == "piou":
            tot+=1
    return tot

def write(chaine,fichier):
    fichier = open(fichier, "w")
    fichier.write(chaine)
    fichier.close()

def ajout_pioumeter(tot,author):
    fichier = open("pioumeter.txt", "r")
    tableau=[line.rstrip('\n') for line in fichier]
    tableau[0],tableau[1]=tableau[0].split('--||__||__||--'),tableau[1].split('--||__||__||--')
    if str(author) not in tableau[0]:
        tableau[0].append(str(author))
        tableau[1].append(str(tot))
    else:
        i=0
        while tableau[0][i]!=str(author):
            i+=1
        tableau[1][i]=str(int(tableau[1][i])+tot)
    fichier.close()
    tableau[0]='--||__||__||--'.join(tableau[0])
    tableau[1]='--||__||__||--'.join(tableau[1])
    chaine='\n'.join(tableau)
    write(chaine,"pioumeter.txt")

def analyse_etre(msg):
    retour=""
    mess=msg.lower()
    if "je suis " in mess:
        k=1
        for i in range(len(mess)-len("je suis ")):
            if mess[i:i+len("je suis ")]=="je suis ":
                h=msg[i+len("je suis ")::]
                if len(h)>0:
                    while(h[0]==' ' and len(h)>0):
                        h=h[1::]
                retour="Bonjour "+h+", moi c'est le bot HF"
    if len(retour)==0:
        k=0
    return(k,retour)

def analyse_salutation(msg):
    mess=msg.lower()
    for k in SALUT_RECONNAISSANCE:
        if len(k)<=len(mess):
            if mess[0:len(k)]==k:
                return 1
    return 0

#fonction qui renvoies les indices d'un tableau après tri
def tri(tableau):
    indices=[i for i in range(len(tableau[1]))]
    i=0
    while i<len(tableau[1])-1:
        if int(tableau[1][i])<int(tableau[1][i+1]):
            temp=tableau[1][i]
            tempi=indices[i]
            indices[i]=indices[i+1]
            indices[i+1]=tempi
            tableau[1][i]=tableau[1][i+1]
            tableau[1][i+1]=temp
            i=0
        else:
            i+=1
    return(indices)

#permet de renvoyer sur discord les meilleurs scores
@bot.command()
async def scores_top(ctx):
    scores="```\nPioumeter :\nPlace | Nom   |  Score\n\n"
    fichier = open("pioumeter.txt", "r")
    tableau=[line.rstrip('\n') for line in fichier]
    tableau[0],tableau[1]=tableau[0].split('--||__||__||--'),tableau[1].split('--||__||__||--')
    indices=tri(tableau)
    print(indices)
    for i in range(min(10,len(indices))):
        scores = scores + str(i+1) + ') ' + tableau[0][indices[i]] + '    ' + tableau[1][i] + '\n'
    scores=scores+"```"
    await ctx.send(scores)


# # # # VI) True Game # # # #
@bot.command()
async def init_day(ctx):
    test=0
    for k in message_author.roles:
        if str(k)=="Le Démon" or str(k)=="Princesse Disney" or str(k)=="Modo des Vérités":
            test=1
    if str(message_channel)!="le-sanctuaire-des-vérités" or test==0:
        return
    global PLAY_GROUP
    PLAY_GROUP=1-PLAY_GROUP
    while len(DETTES)>0:
        DAY.append(DETTES.pop())
    for k in serveur_co.members:
        for l in k.roles:
            if str(l)=="groupe"+str(1+PLAY_GROUP):
                DAY.append(k)
    await ctx.send("Bien initialisé !")

def arrange_mult_tab(tableau):
    tab=[[],[]]
    for k in tableau:
        if k not in tab[0]:
            tab[0].append(k)
            tot=0
            for l in tableau:
                if l==k:
                    tot+=1
            tab[1].append(tot)
    return tab

@bot.command()
async def tour(ctx):
    if str(message_channel)!="le-sanctuaire-des-vérités":
        return
    if len(DAY)==0:
        phrase="Il n'y a plus personne à faire passer !"
    else:
        phrase="C'est le tour du groupe "+str(1+PLAY_GROUP)+'\n'
        tab=arrange_mult_tab(DAY)
        for i in range(len(tab[0])):
            phrase=phrase+str(tab[0][i])+" : "+str(tab[1][i])+'\n'
    await ctx.send(phrase)

@bot.command()
async def dettes(ctx):
    if str(message_channel)!="le-sanctuaire-des-vérités":
        return
    if len(DETTES)==0:
        phrase="Il n'y a pas de dettes !"
    else:
        phrase="Dettes :"+'\n'
        tab=arrange_mult_tab(DETTES)
        for i in range(len(tab[0])):
            phrase=phrase+str(tab[0][i])+" : "+str(tab[1][i])+'\n'
    await ctx.send(phrase)

@bot.command()
async def reinit(ctx):
    test=0
    for k in message_author.roles:
        if str(k)=="Le Démon" or str(k)=="Princesse Disney" or str(k)=="Modo des Vérités":
            test=1
    if str(message_channel)!="le-sanctuaire-des-vérités" or test==0:
        return
    while(len(DAY)>0):
        k=DAY.pop()
    while(len(DETTES)>0):
        k=DETTES.pop()

@bot.command()
async def played(ctx,player):
    test=0
    for k in message_author.roles:
        if str(k)=="Le Démon" or str(k)=="Princesse Disney" or str(k)=="Modo des Vérités":
            test=1
    if str(message_channel)!="le-sanctuaire-des-vérités" or test==0:
        return
    day_temp=[]
    while(len(DAY)>0):
        day_temp.append(DAY.pop())
    while(len(day_temp)>0):
        k=day_temp.pop()
        if "<@!"+str(k.id)+">"!=player:
            DAY.append(k)

@bot.command()
async def end_day(ctx):
    test=0
    for k in message_author.roles:
        if str(k)=="Le Démon" or str(k)=="Princesse Disney" or str(k)=="Modo des Vérités":
            test=1
    if str(message_channel)!="le-sanctuaire-des-vérités" or test==0:
        return
    while len(DAY)>0:
        DETTES.append(DAY.pop())


# # # # VII) Events # # # #
    
@bot.event
async def on_message(message) :
    global message_author
    global message_channel
    global serveur_co
    message_author=message.author
    message_channel=message.channel
    serveur_co=message_author.guild
    if message.author == bot.user:
        return
    elif message.content[0] == bot.command_prefix:
        print("commande reçue de {0.author}: {0.content}".format(message))
    else:
        tot = analyse_piou(message.content)
        if tot > 0:
            if tot == 1:
                await message.add_reaction("\U0001F423")
            elif tot == 2:
                await message.add_reaction("\U0001F425")
            elif tot >= 2:
                for k in bot.emojis:
                    if k.name=='crownchick':
                        emoji=k
                await message.add_reaction(emoji)
            ajout_pioumeter(tot,message.author)
        etre,msg=analyse_etre(message.content)
        salutation=analyse_salutation(message.content)
        if salutation==1:
            alea=random()
            if (alea<POURCENT_SALUTATION):
                alea2=randint(0,len(PHRASES_SALUTATIONS)-1)
                await bot.send_message(message.channel,PHRASES_SALUTATIONS[alea2])
        elif etre==1:
            await bot.send_message(message.channel,msg)  
        else:
            for x in bot.get_all_channels():
                if x.name=="taverne":
                    h=x
            if message.channel==h:
                alea2=randint(0,len(PHRASES_BOT)-1)
                await bot.send_message(message.channel,PHRASES_BOT[alea2])
            else:
                alea=random()
                if (alea<POURCENT_REACTION):
                    alea2=randint(0,len(PHRASES_BOT)-1)
                    await bot.send_message(message.channel,PHRASES_BOT[alea2])
    await bot.process_commands(message)

bot.run(TOKEN)