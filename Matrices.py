#importations



#fonctions
def creation_des_matrices(n):
    if n in [6,8,10]:
        if n == 6:
            D = D6
        elif n == 8:
            D = D8
        elif n == 10:
            D = D10
    else:
        D = D6
        n = 6
    # remplissage matrice
    M_c1T = Crea_matrice(D["c1T"],n)
    M_c1H = Crea_matrice(D["c1H"],n)
    M_c2T = Crea_matrice(D["c2T"],n)
    M_c2H = Crea_matrice(D["c2H"],n)

    D_Mat = {"c1T_M":M_c1T,"c1H_M":M_c1H,"c2T_M":M_c2T,"c2H_M":M_c2T}
    return D_Mat

def Crea_matrice(L,n):
    M = []
    for i in range(len(L)):
        M.append([0]*n)
        M[i][L[i]] = 1
    return M

def Rotation(Jeu,D,direc):
    nvJeu = []
    Mat = D[direc]
    for i in range(len(MonJeu)):
        for j in range(len(MonJeu)):
            if Mat[i][j] != 0:
                Mat[i][j]*MonJeu[j]
                nvJeu.append(Mat[i][j]*MonJeu[j])
    MonJeu = nvJeu

def Fin(Jeu):
    return Jeu == JeuDepart

def Jouer(direc):
    Rotation(MonJeu)
    print(str(MonJeu[0])+"---"+str(MonJeu)+"\n")

D6 = {"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]}
D8 = {"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],
      "c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]}
D10 = {"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],
       "c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]}

JeuDepart = [2,3,3,3,4,4]
MonJeu = [2,3,3,3,4,4]
Matrice_Mouv = creation_des_matrices(6)

while not Fin(MonJeu):
    mes_dir = [["c1T","c1H"],["c2T","c2H"]]
    print("choisir le cerlce (0 ou 1)")
    cercle = input(int("---> "))
    print("choisir le sens Trigo = 0, Horraire = 1")
    sens = input(int("---> "))
    Jouer(mes_dir[cercle][sens])
