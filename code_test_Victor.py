def calcul_deplacement(old_vecteur, matrice_rotation):
    n = len(old_vecteur)
    new_vecteur = []
    for i in range(n):
        new_vecteur.append(0)
        for j in range(n):
            new_vecteur[i] += old_vecteur[j]*matrice_rotation[i][j]
    return new_vecteur




n = 6   #taille du jeu peut etre 6, 8 ou 10

vec = [2,3,3,3,4,4]

#Matrice de rotation du cercle C1. On va dans le sens horraire
M_c1H = [
[0,0,0,1,0,0],
[1,0,0,0,0,0],
[0,1,0,0,0,0],
[0,0,1,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1]
]

#Matrice de rotation du cercle C1. On va dans le sens trigo
M_c1T = [
[0,1,0,0,0,0],
[0,0,1,0,0,0],
[0,0,0,1,0,0],
[1,0,0,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1]
]

#Matrice de rotation du cercle C2. On va dans le sens horraire
M_c2H = [
[0,0,0,0,0,1],
[0,1,0,0,0,0],
[0,0,1,0,0,0],
[0,0,0,1,0,0],
[1,0,0,0,0,0],
[0,0,0,0,1,0]
]

#Matrice de rotation du cercle C2. On va dans le sens trigo
M_c2T = [
[0,0,0,0,1,0],
[0,1,0,0,0,0],
[0,0,1,0,0,0],
[0,0,0,1,0,0],
[0,0,0,0,0,1],
[1,0,0,0,0,0]
]




    
