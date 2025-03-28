### fichier qui créer toute les variables nécéssaire au différentes fonctions du jeu + execution du mini jeu
#importations

from Graphe_pos_base4 import *
from Fonctions_creation_var import *
from Trouve_chemin import *
from random import shuffle
from fonctions_jouer_v3 import *

#prog principal

## def dico pour matrices de rotations
D_pos = {
6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]},
10:{"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],"c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]}
}

D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}

## creations des matrices et des variables du jeu en fonction de nb
    
n,exen = choix_diff()
mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
JeuDepart = D_Jeux[n]
MonJeu = D_Jeux[n][:]
shuffle(MonJeu)

Matrice_Mouv = creation_des_matrices(n,D_pos[n])
Ltout = tout_sommets(n)
MonGraphe = creation_graphe(Matrice_Mouv,Ltout)

#boucle de Jeu solo seulement si exectué directement
if __name__ == "__main__":
    jouer_solo(MonJeu,JeuDepart,mes_dir,Matrice_Mouv)