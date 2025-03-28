# importations
import numpy as np
#import matplotlib.pyplot as plt
from copy import  copy, deepcopy
from math import sqrt, exp
from random import random, randint
from Graphe_pos_base4 import *
from Jeu_en_shell_Victoooor import *

# fn def sur les tableaux  
def sigmo(x,a):
    return 1/(1+np.exp(-a*x))


class Poids():
    def __init__(self, R):
        """R: Réseau de neurones"""
        self.nb_entree = R.nb_entree
        self.nb_cc = R.nb_cc #sous la forme d'un tuple (L, N), L = nb cc et N = nb neurone par cc
        self.nb_sortie = R.nb_sortie
        (L, N) = self.nb_cc
        r4 = Poids.mise_en_poids1(self.nb_entree, N)
        r5 = Poids.mise_en_poids2(L, N)
        r6 = Poids.mise_en_poids3(N,self.nb_sortie)
        self.We = r4
        self.Wcc = r5
        self.Ws = r6
    def lestailles(self):
        Lresu = [np.shape(self.We),len(self.LWcc)]
        for elem in [self.Wcc[0], self.Ws] :
            t = np.shape(elem)
            Lresu.append(t)
        return Lresu
    
    def mise_en_poids1(nb_entree, N):
        L = []
        for i in range(N):
            L.append([])
            for j in range(nb_entree+1):#+1 à cause du biais
                #a = 4*random()-2.0
                #print(a)
                L[-1].append(4*random()-2.0)
        T = np.array(L, dtype='f4')
        #print(T, "\n")
        return T

    def mise_en_poids2(L, N):
        LWc = []
        for i in range(L-1):
            LWr = []
            for j in range(N):
                LWr.append([])
                for k in range(N+1):
                    LWr[-1].append(4*random()-2.0)
            T = np.array(LWr, dtype='f4')
            LWc.append(T)

        #for ele in LWc: print(ele,"\n")
        return LWc
    
    def mise_en_poids3(N, nb_sortie):
        L = []
        for i in range(nb_sortie):
            L.append([])
            for j in range(N+1):
                L[-1].append(4*random()-2.0)
        T = np.array(L, dtype='f4')
        #print(T)
        return T

        

class Neurone():
    def __init__(self, J, E, L, N, S, L_a, s_a_trouv):
        J = decoder_jeu(J, 6)
        self.nb_entree = E
        self.nb_cc = (L, N)
        self.nb_sortie = S
        r1 = Neurone.mise_en_neu1(E, J)
        r2 = Neurone.mise_en_neu2(L, N)
        r3 = Neurone.mise_en_neu3(S)
        self.e = r1
        self.cc = r2
        self.s = r3
        #self.ccT = np.transpose(self.cc) # transposée pour aider la remontée du grad ?
        self.cc_pre_sigmo = deepcopy(self.cc) # les Z c'est avant la sigmo
        self.s_pre_sigmo = deepcopy(self.s) # idem avant la sigmo
        self.s_a_trouver = s_a_trouv
        self.offset = 1
        self.W = Poids(self)
        
    def lestailles(self):
        Lresu = []
        for elem in [self.e, self.cc, self.s]:
            t = np.shape(elem)
            Lresu.append(t)
        return Lresu

    def mise_en_neu_jeu(J):
        L = []
        for cote in J:
            if cote == 2: L.append(0); L.append(0)
            elif cote == 3: L.append(0); L.append(1)
            else: L.append(1); L.append(0)
        return L

    def mise_en_neu1(E, J):
        #L = [0.123]*(E//2) + [0.89]*(E-E//2) + [1.0]
        L = Neurone.mise_en_neu_jeu(J)+[1.0] #jeu: [4,3,3,3,2,4]
        T = np.array(L[:], dtype='f4')
        T = np.reshape(T, (E+1,1)) #(T, (E,1))
        #print(T)
        return T

    def mise_en_neu2(L, N):
        Liste = [i/10.0+0.01234 for i in range(N)] + [1.0]
        LL = []
        for i in range(L):
            LL.append(copy(Liste))
        T = np.array(LL, dtype='f4')
        T = np.transpose(T)
        #print(T)
        return T

    def mise_en_neu3(S):
        T = np.array([0.123456]*S, dtype='f4')
        T = np.reshape(T, (S,1))
        #print(T)
        return T

    def propa(self, W):
        global L_a
        z1 = np.matmul(W.We,self.e)
        N = self.nb_cc[1]
        self.cc_pre_sigmo[0:N, 0:1] = z1
        self.cc[0:N, 0:1] = sigmo(z1, L_a[0])

        for couche in range(np.shape(self.cc)[1]-1):
            z1 = np.matmul(W.Wcc[couche+0], self.cc[0:np.shape(self.cc)[0], couche+0:couche+1])
            self.cc_pre_sigmo[0:N, couche+1:couche+2] = z1
            self.cc[0:N, couche+1:couche+2] = sigmo(z1, L_a[0])
        z1 = np.matmul(W.Ws, self.cc[0:len(self.cc), len(self.cc[0])-1:len(self.cc[0])])
        self.s_pre_sigmo[:, 0:1] = z1
        self.s[:,0:1] = sigmo(z1, L_a[0])
        #print(self.e,'\n', self.cc,'\n', self.s)
        

    def poids_offset(self, offset=0.1):
        
        self.propa(self.W)
        #print('Neurone à trouver: ', self.s_a_trouver, '\n Sorties après propa: \n', self.s, "\n-----------------\n-----------------")
        poids = self.W.Wcc[0][0]
        cout_avant_offset.append(self.cout())
        poidsPlus = poids+offset
        poidsMoins = poids-offset
        self.W.Wcc[0][0] = poidsPlus
        self.propa(self.W)
        #print("Offset positif: \n", self.s)
        #print('cout: ', self.cout())
        coutPlus = self.cout()
        self.W.Wcc[0][0] = poidsMoins
        self.propa(self.W)
        #print("-----------------\n Offset negatif: \n",self.s)
        #print('cout: ', self.cout())
        coutMoins = self.cout()
        delta_cout.append(coutPlus - coutMoins)

    def cout(self):
        #print(self.s_a_trouver)
        accu = 0
        for i in range(4):
            if i != self.s_a_trouver :
                accu += (self.s[i])**2
            else:
                accu += (self.s[self.s_a_trouver]-1)**2
        return accu

    def somme_cout(cout):
        somme = 0
        for elem in cout:
            somme += elem
        return somme

    def ajouter_offset(self):
        self.W.Wcc[0][0] += self.offset
    def soustraire_offset(self):
        self.W.Wcc[0][0] -= self.offset

somme_cout_avant_offset = 0
cout_debut = 0
cout_final = 0
for i in range(10):
    delta_cout = []
    cout_avant_offset = []
    Ltout_pos_6 = tout_sommets(6)        
    L_a = [1.5]
    i=0
    for pos in Ltout_pos_6[1:]:
        pos = encoder_jeu(pos)
        mouv_a_faire = return_first_val(pos)
        A = Neurone(pos, 12, 6, 10, 4, 1.5, mouv_a_faire)
        A.poids_offset()
        i+=1
    somme_cout_avant_offset = Neurone.somme_cout(cout_avant_offset)
    somme_cout_apres_offset = Neurone.somme_cout(delta_cout)
    #print("Somme des couts avant offsets: ", somme_cout_avant_offset)
    #print("Somme des couts après offsets: ", somme_cout_apres_offset)
    cout_debut += somme_cout_avant_offset
    if somme_cout_apres_offset >= 0:
        A.soustraire_offset()
    else:
        A.ajouter_offset()
    cout_apres_offset = []
    for pos in Ltout_pos_6[1:]:
        cout_apres_offset.append(A.cout())
    cout_final += Neurone.somme_cout(cout_apres_offset)
    
print(cout_debut/10)
print(cout_final/10)
#ça ne marche pas

