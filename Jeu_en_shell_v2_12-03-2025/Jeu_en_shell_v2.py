### fichier qui créer toute les variables nécéssaire au différentes fonctions du jeu + execution du mini jeu
#importations

from Graphe_pos_base4 import *
from Fonctions_Jeu import *
from Trouve_chemin import *
from random import shuffle

#prog principal

## def variables
D_pos = {
6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]},
10:{"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],"c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]}
}

Lcarac2 = [[0,None],[1,None],[2,"o"],[3,"A"],[4,"B"],[5,"C"],[6,"D"],[7,"E"],[8,"F"]]
D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}

## boucle Jeu
nb = -1
while nb not in [6,8,10,12]:
    print("veuillez donner le nombre de côtés")
    nb = int(input('---> '))
    Matrice_Mouv = creation_des_matrices(nb,D_pos[nb])

JeuDepart = D_Jeux[nb]
MonJeu = D_Jeux[nb][:]
shuffle(MonJeu)

Ltout = tout_sommets(nb)
MonGraphe = creation_graphe(Matrice_Mouv,Ltout)
print(MonJeu)

def Ordi_joue():
    """
    Parcours le chemin le plus court pour finir le jeu grâce au fonctions de Graphe_pos_base4
    et fait l'affichage du jeu simultanément 
    """
    MonCheminCode = parcoursL_graphe(MonGraphe,encoder_jeu(MonJeu),encoder_jeu(JeuDepart))
    MonChemin = convLparcourus(MonCheminCode)
    print(MonChemin)
    MesMouv = creaLmouv(MonChemin,Matrice_Mouv)
    print(MesMouv)
    LeJeu = MonJeu[:]
    affiche_jeu(LeJeu,Lcarac2)
    for mouv in MesMouv:
        LeJeu = rotation(LeJeu,Matrice_Mouv[mouv])
        affiche_jeu(LeJeu,Lcarac2)
    return fin(LeJeu,JeuDepart)

    #for jeu in MonChemin:
    #    affiche_jeu(jeu,Lcarac2)
    #return fin(LeJeu,JeuDepart)

#seulement si exectué directement
if __name__ == "__main__":
    affiche_jeu(MonJeu,Lcarac2)
    while not fin(MonJeu,JeuDepart):
        mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
        print("choisir le cerlce (0 ou 1)")
        cercle = int(input("---> "))
        print("choisir le sens Trigo = 0, Horraire = 1")
        sens = int(input("---> "))
        MonJeu = rotation(MonJeu,Matrice_Mouv[mes_dir[cercle][sens]])
        affiche_jeu(MonJeu,Lcarac2)

    print("vous avez gagné !")