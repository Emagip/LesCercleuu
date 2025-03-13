#importations

from codage_jeu import *
from Fonctions_Jeu import *
from random import choice

#fonctions
def trouveChemin(G,s_E,s_S):
    """
    Fait un parcours en largeur d'un graphe donné 'G' depuis le sommet sommet d'entrée s_E
    jusqu'au sommet de sortie soit la position de départ du jeu. Puis Grâce à un dictionnaire {fils:père}
    renvoie le chemin de s_S pour aller à s_E
    """
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
        resu = chemin
    else:
        resu = False
    return resu

def exentricite_S(G,S):
    LSom = parcour_Lgraphe(G,S)
    while len(LSom)>0:
        pass

def parcour_Profgraphe(G,S):
    Lparcourus = []
    File = []
    File.append(S)
    while len(File)>0:
        S = File.pop(0)
        Lvoisins = G[S]
        for voisin in Lvoisins:
            if not(voisin in Lparcourus or voisin in File):
                File.append(voisin)
        Lparcourus.append(S)
    return Lparcourus

def convLparcourus(Lche,n):
    """
    convertie la liste des positons de jeu encoder et renvoie une autre liste avec toutes les postions 
    du jeu sous la forme d'une liste des couleurs (ex : [2,4,3,3,4,3])
    """
    L = []
    for etiq in Lche:
        L.append(decoder_jeu(etiq,n))
    return L

def creaLmouv(L_jeu,Matrice):
    """
    prend en argument la liste de tout les jeu (L_jeu) et une un dictionnaire avec les 
    matrices de rotations et renvoie les mouv à éffectuer pour revenir au point de départ
    """
    L_mouv = []
    for i in range(len(L_jeu)):
        LeJeu = L_jeu[i]
        for cle in Matrice:
            L = rotation(LeJeu,Matrice[cle])
            if i+1 < len(L_jeu) and L == L_jeu[i+1]:
                L_mouv.append(cle)
    return L_mouv