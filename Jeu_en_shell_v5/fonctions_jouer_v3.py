#importations

from Fonctions_creation_var import *
from Graphe_pos_base4 import *
from Trouve_chemin import *

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
    #nv n =10
    print("7 : dur")
    print("8 : extrème")
    print("9 : expert")
    diff = -1
    while diff not in [1,2,3,4,5,6,7,8,9]:
        diff = int(input("---> "))
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
            exen = 4
        elif diff == 5:
            exen = 2
        elif diff == 6:
            exen = 0
    elif diff in [7,8,9]:
        n = 10
        if diff == 7:
            exen = 6
        elif diff == 8:
            exen = 4
        elif diff == 9:
            exen = 0
    return [n,exen]

def choix_jeu():
    """demande au joueur de choisir le mode de jeu auquel il veut jouer"""
    jeux = -1
    while jeux not in [1,2,3,4]:
        print("veuillez choisir un mode de Jeu")
        print("1 : jouer_solo")
        print("2 : lancer l'ordi")
        print("3 : ordi vs joueur")
        print("4 : joueur vc joueur")
        jeux = int(input("---> "))
    return jeux

def jouer_solo(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """fait une partie de jeu en solo"""
    affiche_jeu(jeu)
    while not fin(jeu,jeuDep):
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        jeu = rotation(jeu,matriceMouv[mesDir[cercle][sens]])
        affiche_jeu(jeu)
    print("vous avez gagné !")
    return jeu 

def ordi_joue(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """
    Parcours le chemin le plus court pour finir le jeu grâce au fonctions de Graphe_pos_base4
    et fait l'affichage du jeu simultanément 
    """
    accu = 0
    MonCheminCode = ralonge_chemin(0,monGraphe,encoder_jeu(jeu),encoder_jeu(jeuDep))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,matriceMouv)
    LeJeu = jeu[:]
    affiche_jeu(LeJeu)
    for mouv in MesMouv:
        accu += 1
        LeJeu = rotation(LeJeu,matriceMouv[mouv])
        affiche_jeu(LeJeu)
        print("Nombre d'itérations: ",accu)
    return fin(LeJeu,jeuDep)

def joueur_vs_ordi(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """Le joueur joue contre un ordi plus ou moins simple en fonction de l'excentricité"""
    #jeu ordi => LeJeu
    #jeu joueur => jeu
    MonCheminCode = ralonge_chemin(exen,monGraphe,encoder_jeu(jeu),encoder_jeu(jeuDep))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,matriceMouv)
    LeJeu = jeu[:]
    i=0
    arreter = False
    print("veuillez donner le pseudo du premier joueur")
    j1 = input("---> ")
    while not fin(LeJeu,jeuDep):
        print("------------ooo000ooo------------")
        print ('TOUR DE',j1)
        affiche_jeu(jeu)
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        jeu = rotation(jeu,matriceMouv[mesDir[cercle][sens]])
        if fin(jeu, jeuDep):
            arreter = True
        if not arreter:
            #ordi
            print("------------ooo000ooo------------")
            print("L'ORDI À JOUÉ")
            LeJeu = rotation(LeJeu,matriceMouv[MesMouv[i]])
            #affiche_jeu(LeJeu,Lcar)
            
            i+=1
        else:
            print(j1," à gagné !")
            affiche_jeu(LeJeu)
            return jeu

    print("Ordi gagne")
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
        print("------------ooo000ooo------------")
        print("TOUR DE",j1)
        affiche_jeu(jeu1)
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        jeu1 = rotation(jeu1,matriceMouv[mesDir[cercle][sens]])
        if fin(jeu1, jeuDep):
            arreter = True
        if not arreter:
            #joueur 2
            print("------------ooo000ooo------------")
            print("TOUR DE",j2)
            affiche_jeu(jeu2)
            print("choisir le cerlce (0 ou 1)")
            cercle = int(input("---> "))
            print("choisir le sens Trigo = 0, Horraire = 1")
            sens = int(input("---> "))
            jeu2 = rotation(jeu2,matriceMouv[mesDir[cercle][sens]])
            if fin(jeu2,jeuDep):
                arreter = True
        else:
            print(j2," à gagné !")
            return jeu2
    print(j1," à gagné !")
    return jeu1
    
def lancement_Jeu(maFonc,jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir):
    """execute le jeu choisi"""
    maFonc(jeu,jeuDep,matriceMouv,monGraphe,n,exen,mesDir)