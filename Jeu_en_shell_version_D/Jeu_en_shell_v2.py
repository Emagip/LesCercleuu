### fichier qui créer toute les variables nécéssaire au différentes fonctions du jeu + execution du mini jeu
#importations

from Graphe_pos_base4 import *
from Fonctions_creation_var import *
from Trouve_chemin import *
from random import randint
from fonctions_jouer_v3 import *

#prog principal

## def dico pour matrices de rotations
D_pos = {
6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]},
10:{"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],"c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]},
12:{"c1T":[1,2,3,4,5,6,0,7,8,9,10,11],"c1H":[6,0,1,2,3,4,5,7,8,9,10,11],"c2T":[7,1,2,3,4,5,6,8,9,10,11,0],"c2H":[11,1,2,3,4,5,6,0,7,8,9,10]}
}

D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4],12:[2,3,3,3,3,3,3,4,4,4,4,4]}

## creations des matrices et des variables du jeu en fonction de nb
J,n_temp,maFonc,n = -1,-1,None,-1
J = choix_jeu()
if J == 3:
    maFonc = joueur_vs_ordi
    n,exen = choix_diff()
    if n == 12:
        print("veuillez patienter, ceci peut prendre quelque secondes")
else :
    exen = 0 
    while n_temp not in ['6','8','10','12']:
        print("veuillez choisir la taille du cercle")
        n_temp = input("---> ")
    n = int(n_temp)
    if n == 12:
        print("veuillez patienter, ceci peut prendre quelque secondes")
    if J == 1:
        maFonc = jouer_solo
    elif J == 2:
        maFonc = ordi_joue
    elif J == 4:
        maFonc = joueur_vs_joueur

Matrice_Mouv = creation_des_matrices(n,D_pos[n])
Ltout = tout_sommets(n)
MonGraphe = creation_graphe(Matrice_Mouv,Ltout)
mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
JeuDepart = D_Jeux[n]
L_exen = exentricite_S(MonGraphe,encoder_jeu(JeuDepart))
i = randint(0,len(L_exen)-1)
print(i)
MonJeu = decoder_jeu(choice((L_exen[i])),n)

if __name__ == "__main__":
    lancement_Jeu(maFonc,MonJeu,JeuDepart,Matrice_Mouv,MonGraphe,n,exen,mes_dir,i,L_exen)