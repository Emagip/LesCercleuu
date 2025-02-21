#importations

from codage_jeu import *
from Fonctions_Jeu import *

#fonctions
def parcoursL_graphe(G,s_E,s_S):
    Lparcourus = []
    trouve = False
    File = []
    File.append([None,s_E])
    Dfp = {}
    while not trouve and len(File)>0:
        Sprecedent,S = File.pop(0)
        Lvoisins = G[S]
        Dfp[S] = Sprecedent
        for voisin in Lvoisins:
            if voisin == s_S:
                trouve = True
                Dfp[voisin] = S
            elif not(voisin in Lparcourus or voisin in File):
                File.append([S,voisin])
        Lparcourus.append(S)

    if trouve:
        chemin = []
        pere = S
        while pere != None:
            chemin.append(pere)
            pere = Dfp[pere]
        chemin.reverse()
        chemin.append(s_S)
        print(chemin)
        resu = chemin
    else:
        resu = False
    return resu

def convLparcourus(Lparc):
    L = []
    for etiq in Lparc:
        L.append(decoder_jeu(etiq))
    return L

def creaLmouv(L_jeu,Matrice):
    L_mouv = []
    for i in range(len(L_jeu)):
        LeJeu = L_jeu[i]
        for cle in Matrice:
            L = rotation(LeJeu,Matrice[cle])
            if i+1 < len(L_jeu) and L == L_jeu[i+1]:
                L_mouv.append(cle)
    return L_mouv

#def retourDep(L_mouv,Jeu):
#    for mouv in L_mouv:
#        Jeu = rotation(Jeu,mouv)
#        affiche_jeu(Jeu)
#    return Jeu