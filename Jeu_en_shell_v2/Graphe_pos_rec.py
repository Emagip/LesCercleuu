# importaions

from codage_jeu import *
from Fonctions_Jeu import rotation

#fonctions

def mise_en_place(n,Jeu): #n est le nombre de côté
    global Ltout,Lkdo,pris,permu
    Lkdo = Jeu[:] #le jeu de depart mélanger
    Ltout = [] # conteneur des permutatuons terminé au nb de n!
    pris = [False]*n # distingue les kdo deja dans permu et ceux qu'il n'y sont pas encore
    permu = []# la permutation en cours de construction

def Pepenono_rec(i):
    """ *) ajouter le kdo i à la permu et changer le bool pris[i]
        **) tester si tout les kdo sont pris -> CdB
        ***) si hors CdB boucle for j test de pris[j] puis appel rec puis avant de disp
    """
    global Lkdo,pris,permu, Ltout
    pris[i] = True
    permu.append(Lkdo[i])
    if len(permu) == len(Lkdo):
        if permu not in Ltout:
            Ltout.append(permu[:])
    else:
        for j in range(len(Lkdo)):
            if not pris[j]:
                Pepenono_rec(j)
    pris[i] = False
    permu.pop()

def creation_graphe(Matrice):
    G = {}
    for PermuJeu in Ltout:
        voisin = []
        for cle in  Matrice:
            L = rotation(PermuJeu,Matrice[cle])
            #etiq = encoder_jeu(L)
            voisin.append(L)
        S = encoder_jeu(PermuJeu)
        G[S] = voisin[:]
    return G