# importaions

from codage_jeu import *
from Fonctions_Jeu import *

#fonctions

def verif_jeu_valide(jeu):
    """
    vérifie si le jeu donné est bien une position possible du jeu de base
    renvoie un booléen True ou False
    """
    n = len(jeu)
    nbde2 = 0
    nbde3 = 0
    nbde4 = 0
    nbde5 = 0
    for i in range(len(jeu)):
        if jeu[i] == 3:
            nbde3 += 1    
        elif jeu[i] == 4:
            nbde4 += 1
        elif jeu[i] == 5:
            return False
        else:
            nbde2 += 1
    if not(nbde2 == 1 and nbde3 == n//2 and nbde4 == (n//2)-1):
        return False
    return True

def tout_sommets(n):
    """
    renvoie une liste contenants toutes les positons possible du jeu en fonction de n
    soit tous les sommets pour le graphe
    """
    Ltout = []
    if n == 6:
        for i in range(346, 2644+1):
            jeu_actu = decoder_jeu(i,n)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    elif n == 8:
        for i in range(5482, 43348+1):
            jeu_actu = decoder_jeu(i,n)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    else:
        for i in range(87466, 697684+1):
            jeu_actu = decoder_jeu(i,n)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    return Ltout
   
            

def creation_graphe(Matrice, Ltout):
    """
    renvoie un graphe G qui possède les sommets contenu dans Ltout et leurs donnent comme voisins 
    leurs rotations par le dictionnaire des matrices de rotations
    """
    G = {}
    for PermuJeu in Ltout:
        voisin = []
        for cle in  Matrice:
            L = rotation(PermuJeu,Matrice[cle])
            etiq = encoder_jeu(L)
            voisin.append(etiq)
        S = encoder_jeu(PermuJeu)
        G[S] = voisin[:]
    return G
