#Projet : Circle Puzzle
#Auteurs : Victor Frappaz, Maxime Pigeaud, Fabian Peter

#importations

from Fonctions_creation_var import *
from Graphe_pos_base4 import *
from Trouve_chemin import *
from random import choice

#fonctions de Jeu (solo,pvp ou pve)

def choix_diff():
    """demande au jour par une boucle while de choisir la difficulté du jeu pour choisir l'exentricité du graphe"""
    print("veuillez choisir une difficulté : \n")
    #nv n = 6
    print("1 : extrèmement facile") #excentricite 2
    print("2 : très facile")#excentricite 1
    print("3 : facile")#excentricite 0
    # nv n = 8
    print("4 : moyen facile")#excentricite 6
    print("5 : moyen")
    print("6 : moyen dur")
    #nv n = 10
    print("7 : dur")
    print("8 : extrème")
    print("9 : expert")
    # n = 12
    print("10 : hardcore")
    print("11 : démon")
    print("12 : fou")
    diff_temp,diff = -1,-1
    while diff_temp not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
        diff_temp = input("---> ")
    diff = int(diff_temp)
    if diff in [1,2,3]:
        n = 6
        if diff == 1:
            exen = 2
        elif diff == 2:
            exen = 1
        elif diff == 3:
            exen = 0
    elif diff in [4,5,6]:
        n = 8
        if diff == 4:
            exen = 3
        elif diff == 5:
            exen = 2
        elif diff == 6:
            exen = 0
    elif diff in [7,8,9]:
        n = 10
        if diff == 7:
            exen = 4
        elif diff == 8:
            exen = 3
        elif diff == 9:
            exen = 0
    elif diff in [10,11,12]:
        n = 12
        if diff == 10:
            exen = 4
        elif diff == 11:
            exen = 3
        elif diff == 12:
            exen = 0
    return [n,exen]

def choix_jeu():
    """demande au joueur de choisir le mode de jeu auquel il veut jouer"""
    jeux = -1
    while jeux not in ['1','2','3','4']:
        print("veuillez choisir un mode de Jeu")
        print("1 : jouer_solo")
        print("2 : lancer l'ordi")
        print("3 : ordi vs joueur")
        print("4 : joueur vs joueur")
        jeux = input("---> ")
    jeux = int(jeux)
    return jeux

def verif():
    """fonction qui vérifie si la valeur donné est valable pour jouer dans le jeu"""
    val = -1
    while val not in ['1','0']:
        val = input("---> ")
    return int(val)

def unTour(jeu,matriceMouv,mesDir):
    """exute un tour de jeu pour compacter le programme"""
    print("choisir le cerlce (0 ou 1)")
    cercle = verif()
    print("choisir le sens Trigo = 0, Horraire = 1")
    sens = verif()
    jeu = rotation(jeu,matriceMouv[mesDir[cercle][sens]])
    return jeu 

def jouer_solo(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """fait une partie de jeu en solo"""
    affiche_jeu(jeu)
    while not fin(jeu,jeuDep):
        jeu = unTour(jeu,matriceMouv,mesDir)
        affiche_jeu(jeu)
    print("vous avez gagné !")
    return jeu

def creaVarOrdi(jeu,jeuDep,matriceMouv,monGraphe,n):
    """creer le chemin en mouvement, soit les clé du dictionnaires des matrices de rotations"""
    MonCheminCode = ralonge_chemin(0,monGraphe,encoder_jeu(jeu),encoder_jeu(jeuDep))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,matriceMouv)
    return MesMouv

def ordi_joue(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """
    Parcours le chemin le plus court pour finir le jeu grâce au fonctions de Graphe_pos_base4
    et fait l'affichage du jeu simultanément 
    """
    accu = 0
    MesMouv = creaVarOrdi(jeu,jeuDep,matriceMouv,monGraphe,n)
    LeJeu = jeu[:]
    affiche_jeu(LeJeu)
    for mouv in MesMouv:
        accu += 1
        LeJeu = rotation(LeJeu,matriceMouv[mouv])
        affiche_jeu(LeJeu)
        print("Nombre d'itérations: ",accu)
    return fin(LeJeu,jeuDep)

def joueur_vs_ordi(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir,j,L_exen):
    """Le joueur joue contre un ordi plus ou moins simple en fonction de l'excentricité"""
    #jeu ordi => LeJeu
    #jeu joueur => jeu
    MesMouv = creaVarOrdi(jeu,jeuDep,matriceMouv,monGraphe,n)
    LeJeu = decoder_jeu(choice((L_exen[j])),n)
    i=0
    arreter = False
    print("veuillez donner le pseudo du joueur")
    j1 = input("---> ")
    while not fin(LeJeu,jeuDep):
        print("---------------------------------")
        print ('TOUR DE',j1)
        affiche_jeu(jeu)
        jeu = unTour(jeu,matriceMouv,mesDir)
        if fin(jeu, jeuDep):
            arreter = True
        if not arreter:
            #ordi
            print("---------------------------------")
            print("L'ORDI A JOUÉ")
            LeJeu = rotation(LeJeu,matriceMouv[MesMouv[i]])
            #affiche_jeu(LeJeu,Lcar)
            
            i+=1
        else:
            print(j1," a gagné !")
            affiche_jeu(LeJeu)
            return jeu

    print("Ordi gagne")
    affiche_jeu(LeJeu)
    return LeJeu
            
    
    

def joueur_vs_joueur(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """deux joueur s'affronte en 1v1"""
    jeu1,jeu2 = jeu[:],jeu[:]
    arreter = False
    print("veuillez donner le pseudo du premier joueur")
    j1 = input("---> ")
    print("veuillez donner le pseudo du deuxième joueur")
    j2 = input("---> ")
    while not (fin(jeu1,jeuDep) or fin(jeu2,jeuDep)):

        #joueur 1
        print("---------------------------------")
        print("TOUR DE",j1)
        affiche_jeu(jeu1)
        jeu1 = unTour(jeu1,matriceMouv,mesDir)
        if fin(jeu1, jeuDep):
            arreter = True
        if not arreter:
            #joueur 2
            print("---------------------------------")
            print("TOUR DE",j2)
            affiche_jeu(jeu2)
            jeu2 = unTour(jeu2,matriceMouv,mesDir)
            if fin(jeu2,jeuDep):
                arreter = True
        else:
            print(j2," a gagné !")
            return jeu2
    print(j1," a gagné !")
    return jeu1
    
def lancement_Jeu(maFonc,jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir,i,L_exen):
    """execute le jeu choisi"""
    if maFonc == joueur_vs_ordi:
        maFonc(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir,i,L_exen)
    else:
        maFonc(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir)