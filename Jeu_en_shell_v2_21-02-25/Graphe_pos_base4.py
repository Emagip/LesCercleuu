# importaions

from codage_jeu import *
from Fonctions_Jeu import *

#fonctions

##def mise_en_place(n,Jeu): #n est le nombre de côté
##    global Ltout,Lkdo,pris,permu
##    Lkdo = [x for x in Jeu if x != 2]
##    Lkdo = Jeu[:]
##    #le jeu de depart mélangé
##    Ltout = [] # conteneur des permutatuons terminé au nb de n!
##    pris = [False]*n # distingue les kdo deja dans permu et ceux qu'il n'y sont pas encore
##    permu = []# la permutation en cours de construction
##
##def Pepenono_rec(i):
##    """ *) ajouter le kdo i à la permu et changer le bool pris[i]
##        **) tester si tout les kdo sont pris -> CdB
##        ***) si hors CdB boucle for j test de pris[j] puis appel rec puis avant de disp
##    """
##    global Lkdo,pris,permu, Ltout
##    pris[i] = True
##    permu.append(Lkdo[i])
##    if len(permu) == len(Lkdo):
##        if permu not in Ltout:
##            Ltout.append(permu[:])
##    else:
##        for j in range(len(Lkdo)):
##            if not pris[j]:
##                Pepenono_rec(j)
##    pris[i] = False
##    permu.pop()
def verif_jeu_valide(jeu):
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
    Ltout = []
    if n == 6:
        for i in range(346, 2644+1): #depart: position [2,3,3,3,4,4] <- codage le plus faible
                                   #arrivée: postion [4,4,3,3,3,2] <- codage le plus élevé
            jeu_actu = decoder_jeu(i)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    elif n == 8:
        for i in range(5482, 43348+1): #depart: position [2,3,3,3,4,4] <- codage le plus faible
                                   #arrivée: postion [4,4,3,3,3,2] <- codage le plus élevé
            jeu_actu = decoder_jeu(i)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    else:
        for i in range(87466, 697684+1): #depart: position [2,3,3,3,4,4] <- codage le plus faible
                                   #arrivée: postion [4,4,3,3,3,2] <- codage le plus élevé
            jeu_actu = decoder_jeu(i)
            if  verif_jeu_valide(jeu_actu):
                Ltout.append(jeu_actu)
    print(Ltout)
    return Ltout
   
            

def creation_graphe(Matrice, Ltout):
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
