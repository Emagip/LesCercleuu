# importaions

from codage_jeu import *
from Jeu_en_shell_MARCHE import MonJeu,Matrice_Mouv,rotation

#fonctions

def mise_en_place(n): #n est le nombre de côté
    global magasin,Ltout
    global Lkdo,pris,permu
    Lkdo = MonJeu[:] #le jeu de depart mélanger
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

def creation_graphe():
    G = {}
    for PermuJeu in Ltout:
        voisin = []
        for cle in  Matrice_Mouv:
            L = rotation(PermuJeu,Matrice_Mouv[cle])
            etiq = encoder_jeu(L)
            voisin.append(etiq)
        S = encoder_jeu(PermuJeu)
        G[S] = voisin[:]
    return G

def parc_LargM(GM,S_E, S_S):
    """ S_E et les sommets i sont des int. \n"""
    Lparcourus = []
    file = [] #init de la file FIFO à vide
    file.append(S_E) # debut algo parcours en largeur
    while not len(file) == 0 and S_S not in Lparcourus: # tant que la file n'est pas vide
        S = file.pop(0)# CREE LE COMPORTEMENT DE FileFIFO
        L_des_voisins = GM[S]
        # S est un int entre 0 et ordre-1 inclus
        # si la file est trop remplie,
        for voisin in L_des_voisins:
            if not(voisin in Lparcourus or voisin in file):
                file.append(voisin)
        Lparcourus.append(S)
    return Lparcourus

mise_en_place(6)
for i in range(6):
    Pepenono_rec(i)

MonGraphe = creation_graphe()
#print(MonGraphe)

lacle = list(MonGraphe.keys())[0]

print(parc_LargM(MonGraphe,lacle, 346))
