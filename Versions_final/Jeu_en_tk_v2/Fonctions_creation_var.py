#Projet : Circle Puzzle
#Auteurs : Victor Frappaz, Maxime Pigeaud, Fabian Peter

#fonctions
def creation_des_matrices(n,D):
    """
    créer toute les matrices de mouvement à partir du dictionnaire des positions
    du jeu pour les indices en appelant crea_matrice() et renvoie un dictionnaire contenant les 4 matrices 
    de rotations
    """
    # remplissage matrice
    M_c1T = crea_matrice(D["c1T"],n)
    M_c1H = crea_matrice(D["c1H"],n)
    M_c2T = crea_matrice(D["c2T"],n)
    M_c2H = crea_matrice(D["c2H"],n)

    D_Mat = {"c1T_M":M_c1T,"c1H_M":M_c1H,"c2T_M":M_c2T,"c2H_M":M_c2H}
    return D_Mat

def crea_matrice(L,n):
    """
    renvoie une matrice de rotations en fonctions des indices dans L et en fonctions 
    de la taille du jeu n
    """
    M = []
    for i in range(len(L)):
        M.append([0]*n)
        M[i][L[i]] = 1
    return M

def rotation(old_vecteur, matrice_rotation):
    """
    renvoie la rotation du jeu par la matrice de rotations pris en paramètre
    """
    n = len(old_vecteur)
    new_vecteur = []
    for i in range(n):
        new_vecteur.append(0)
        for j in range(n):
            new_vecteur[i] += old_vecteur[j]*matrice_rotation[i][j]
    return new_vecteur

def fin(Jeu,Jeuverif):
    return Jeu == Jeuverif

def affiche_jeu(J):
    """ affiche un jeu à 2 cycles 2 couleurs 1 case vide \
        Lsymb permet de remplacer les int 0,1,2 par \
        des lettres approopriées (p.ex.  'o', 'A', 'B' ) \
        inapproprié pour les len(J) != 6 ou 8"""
    Lsymb = [[0,None],[1,None],[2,"o"],[3,"A"],[4,"B"],[5,"C"],[6,"D"],[7,"E"],[8,"F"]]
    if len(J) in [6,8,10,12]:
        Lcar=[]
        taille = len(Lsymb)
        for n in J:
            davai = True
            i = 0; car = " "
            while davai and i<taille :
                if n==Lsymb[i][0] :
                    car = Lsymb[i][1]
                    davai = False
                i+=1
            Lcar.append(car)
        print()
        if len(J)==6 :
            print("  .-"+Lcar[3]+"-.")
            print("  |   | "+Lcar[4])
            print("  "+Lcar[2]+"   "+Lcar[0]+"   "+">")
            print("  |   | "+Lcar[5])
            print("  '-"+Lcar[1]+"-'")
        if len(J) == 8 :
            print("  .--"+Lcar[4]+"-.-"+Lcar[5]+".")
            print("  "+Lcar[3]+"    |   \\ ")
            print("  |    "+Lcar[0]+"    "+Lcar[6])
            print("  "+Lcar[2]+"    |   / ")
            print("  '--"+Lcar[1]+"-'-"+Lcar[7]+"'")
        if len(J) == 10 :
            print("  "+Lcar[4]+"--"+Lcar[5]+"-.-"+Lcar[6]+"-.")
            print("  |    |    "+Lcar[7])
            print("  "+Lcar[3]+"    "+Lcar[0]+"    |")
            print("  |    |    "+Lcar[8])
            print("  "+Lcar[2]+"--"+Lcar[1]+"-'-"+Lcar[9]+"-'")
        if len(J) == 12 :
            print("  .-"+Lcar[5]+"-"+Lcar[6]+"-.-"+Lcar[7]+"-"+Lcar[8]+".")
            print("  "+Lcar[4]+"     |     \\ ")
            print("  |     "+Lcar[0]+"      "+Lcar[9])
            print("  "+Lcar[3]+"     |     / ")
            print("  '-"+Lcar[2]+"-"+Lcar[1]+"-'-"+Lcar[11]+"-"+Lcar[10]+"'")
    else :
        print("je ne sais pas faire")