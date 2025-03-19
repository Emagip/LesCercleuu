#importations

from Fonctions_creation_var import *
from Graphe_pos_base4 import *
from Trouve_chemin import *

#fonctions de Jeu (solo,pvp ou pve)

def choix_diff():
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

def jouer_solo(Jeu,Jeudep,mesdir,Mmouv):
    """Jeu,jeudep,mesdir,Mmouv"""
    affiche_jeu(Jeu)
    while not fin(Jeu,Jeudep):
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        Jeu = rotation(Jeu,Mmouv[mesdir[cercle][sens]])
        affiche_jeu(Jeu)
    print("vous avez gagné !")

def ordi_joue(MonGraphe,MonJeu,JeuDepart,Matrice_Mouv,n,exen):
    """
    Parcours le chemin le plus court pour finir le jeu grâce au fonctions de Graphe_pos_base4
    et fait l'affichage du jeu simultanément 
    """
    accu = 0
    MonCheminCode = ralonge_chemin(exen,MonGraphe,encoder_jeu(MonJeu),encoder_jeu(JeuDepart))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,Matrice_Mouv)
    LeJeu = MonJeu[:]
    affiche_jeu(LeJeu)
    for mouv in MesMouv:
        accu += 1
        LeJeu = rotation(LeJeu,Matrice_Mouv[mouv])
        affiche_jeu(LeJeu)
        print("Nombre d'itérations: ",accu)
    return fin(LeJeu,JeuDepart)

def joueur_vs_Ordi(jeu, jeuDepart, monGraphe, mesDir, matriceMouv,n,exen):
    #jeu ordi => LeJeu
    #jeu joueur => jeu
    MonCheminCode = ralonge_chemin(exen,monGraphe,encoder_jeu(jeu),encoder_jeu(jeuDepart))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,matriceMouv)
    LeJeu = jeu[:]
    i=0
    arreter = False
    while not fin(LeJeu,jeuDepart):
        print("------------------------------")
        print ('TOUR JOUEUR')
        affiche_jeu(jeu)
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        jeu = rotation(jeu,matriceMouv[mesDir[cercle][sens]])
        if fin(jeu, jeuDepart):
            arreter = True
        if not arreter:
            #ordi
            print("------------------------------")
            print("L'ordi a joué")
            LeJeu = rotation(LeJeu,matriceMouv[MesMouv[i]])
            #affiche_jeu(LeJeu,Lcar)
            
            i+=1
        else:
            print("Joueur gagne")
            affiche_jeu(LeJeu)
            return 0

    print("Ordi gagne")
    return 1
            
    
    

def joueur_vs_joueur(jeu, jeuDepart, Lcar, mesdir, matriceMouv):
    jeu1,jeu2 = jeu[:],jeu[:]
    arreter = False
    while not (fin(jeu1,jeuDepart) or fin(jeu2,jeuDepart)):

        #joueur 1
        print("------------------------------")
        print("TOUR JOUEUR 1")
        affiche_jeu(jeu1,Lcar)
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        jeu1 = rotation(jeu1,matriceMouv[mesdir[cercle][sens]])
        affiche_jeu(jeu1,Lcar)
        if fin(jeu1, jeuDepart):
            arreter = True
        if not arreter:
            #joueur 2
            print("------------------------------")
            print("TOUR JOUEUR 2")
            affiche_jeu(jeu2,Lcar)
            print("choisir le cerlce (0 ou 1)")
            cercle = int(input("---> "))
            print("choisir le sens Trigo = 0, Horraire = 1")
            sens = int(input("---> "))
            jeu2 = rotation(jeu2,matriceMouv[mesdir[cercle][sens]])
            affiche_jeu(jeu2,Lcar)
            if fin(jeu2, jeuDepart):
                arreter = True
        else:
            print("Joueur 2 gagne")
            return 2
    print("Joueur 1 gagne")
    return 1
    
