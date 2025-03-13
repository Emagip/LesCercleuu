#importations

from Fonctions_Jeu import *
from Graphe_pos_base4 import *
from Trouve_chemin import *

#fonctions de Jeu (solo,pvp ou pve)

def jouer_solo(Jeu,Jeudep,Lcar,mesdir,Mmouv):
    """Jeu,jeudep,Lcar,mesdir,Mmouv"""
    affiche_jeu(Jeu,Lcar)
    while not fin(Jeu,Jeudep):
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        Jeu = rotation(Jeu,Mmouv[mesdir[cercle][sens]])
        print(Jeu)
        affiche_jeu(Jeu,Lcar)
    print("vous avez gagné !")

def ordi_joue(MonGraphe,MonJeu,JeuDepart,Matrice_Mouv,Lcarac2,n):
    """
    Parcours le chemin le plus court pour finir le jeu grâce au fonctions de Graphe_pos_base4
    et fait l'affichage du jeu simultanément 
    """
    MonCheminCode = trouveChemin(MonGraphe,encoder_jeu(MonJeu),encoder_jeu(JeuDepart))
    MonChemin = convLparcourus(MonCheminCode,n)
    MesMouv = creaLmouv(MonChemin,Matrice_Mouv)
    LeJeu = MonJeu[:]
    affiche_jeu(LeJeu,Lcarac2)
    for mouv in MesMouv:
        LeJeu = rotation(LeJeu,Matrice_Mouv[mouv])
        affiche_jeu(LeJeu,Lcarac2)
    return fin(LeJeu,JeuDepart)

def joueur_vs_Ordi():
    pass

def joueur_vs_joueur():
    pass
