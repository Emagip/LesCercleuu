#importations

from codage_jeu import *
from Fonctions_creation_var import *
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
    if s_E == s_S:
        resu = False
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
    dejavu = [S]
    ordre = len(G)
    Lexen = [[S]]
    i = 0
    while len(dejavu)<ordre:
        Lexen.append([])
        for s in Lexen[i]:
            Lvoisins = G[s]
            for voisin in Lvoisins:
                if voisin not in dejavu:
                    Lexen[i+1].append(voisin)
                    dejavu.append(voisin)
        i += 1
    return Lexen

def ralonge_chemin(exen,G,S_e,S_s):
    Lexen = exentricite_S(G,S_s)
    if exen != 0:
        nv_S = choice(Lexen[exen])
        monchemin = trouveChemin(G,S_e,nv_S)
        print("chemin1 :",monchemin)
        print(nv_S,S_s)
        ch2 = trouveChemin(G,nv_S,S_s)
        print("chemin2 :",ch2)
        monchemin.pop()
        print(nv_S)
        for sommet in ch2:
            monchemin.append(sommet)
    print(S_e,S_s)
    monchemin = trouveChemin(G,S_e,S_s)
    return monchemin

def simulations(exen,G,S_s,nb):
    L_chlong = []
    L_chopti = []
    for i in range(nb):
        S_e = choice(list(G.keys()))
        a,b = ralonge_chemin(exen,G,S_e,S_s)
        L_chlong.append(len(a))
        L_chopti.append(len(b))
    moyLong = sum(L_chlong)/len(L_chlong)
    moyOpti = sum(L_chopti)/len(L_chopti)
    print("moyLong : ",moyLong,"\nmoyOpti : ",moyOpti)

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