#Projet : Circle Puzzle
#Auteurs : Victor Frappaz, Maxime Pigeaud, Fabian Peter

import Graphe_pos_base4 as GPB
import Trouve_chemin as balade
import Fonctions_creation_var as FJeu
from random import randint, choice

D_pos = {6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
         8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]},
         10:{"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],"c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]}
         }
D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}

def transform(x, y):
    return X_OFFSET + x * SCALE, Y_OFFSET - y * SCALE

def mise_en_place(n,exen):
    global Matrice_Mouv,Ltout,MonGraphe,JeuDepart,L_exen,MonJeu1,MonJeu2,MesMouv
    Matrice_Mouv = FJeu.creation_des_matrices(n, D_pos[n])
    Ltout = GPB.tout_sommets(n)
    MonGraphe = GPB.creation_graphe(Matrice_Mouv,Ltout)
    JeuDepart = D_Jeux[n]
    L_exen = balade.exentricite_S(MonGraphe, GPB.encoder_jeu(JeuDepart))

    i = randint(0,len(L_exen)-1)

    MonJeu1 = GPB.decoder_jeu(choice(L_exen[i]),n)
    MonJeu2 = GPB.decoder_jeu(choice(L_exen[i]),n)
    print(MonJeu1)
    print(MonJeu2)

    MonCheminCode = balade.ralonge_chemin(exen,MonGraphe,GPB.encoder_jeu(MonJeu2), GPB.encoder_jeu(JeuDepart))
    MonChemin = balade.convLparcourus(MonCheminCode,n)
    MesMouv = balade.creaLmouv(MonChemin, Matrice_Mouv)

def give_coords(n):
    global WIDTH,HEIGHT,X_OFFSET,Y_OFFSET,SCALE,coords_set,x0,y0,x1,y1
    if n == 6:
        WIDTH, HEIGHT = 800, 600
        X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
        SCALE = 30
        x0, y0 = transform(-2.4 - 5.6, 0 + 5.6)
        x1, y1 = transform(-2.4 + 5.6, 0 - 5.6)
        coords_set = {
            "c0": [[transform(-5.95 - 8.67, 0 + 8.67), transform(-5.95 + 8.67, 0 - 8.67), 23.51, -47.02], [transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 120.03, 119.94],2],
            "c1": [[transform(-2.4 - 8.4, -10.62 + 8.4), transform(-2.4 + 8.4, -10.62 - 8.4), 58.41, 63.18],[(x0, y0), (x1, y1),-38.17,-103.66],3],
            "c2": [[transform(-10.22 - 4.87, 0 + 4.87), transform(-10.22 + 4.87, 0 - 4.87), 45.33, -90.65],[(x0,y0), (x1, y1), 141.83, 76.34], 3],
            "c3": [[transform(-2.4 - 8.4, 10.62 + 8.4), transform(-2.4 + 8.4, 10.62 - 8.4), -58.41, -63.18],[(x0,y0), (x1,y1),38.17, 103.66], 3],
            "c4": [[transform(9.01 - 8.71, 8.66 + 8.71), transform(9.01 + 8.71, 8.66 - 8.71), -96.65, -46.78],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, 120.03],4],
            "c5": [[transform(9.01 - 8.71, -8.66 + 8.71), transform(9.01 + 8.71, -8.66 - 8.71), 96.65, 46.78],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, -120.03],4]
            }
    if n == 8:
        WIDTH, HEIGHT = 800, 600
        X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
        SCALE = 30
        x0, y0 = transform(-3 - 5, 0 + 5)
        x1, y1 = transform(-3 + 5, 0 - 5)
        coords_set = {
            "c0": [[transform(-3.24 - 5.24, 0 + 5.24), transform(-3.24 + 5.24, 0 - 5.24), 32.69, -65.38], [transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 135, 90],2],
            "c1": [[transform(-0.36 - 4.84, -7.42 + 4.88), transform(-0.36 + 4.88, -7.42 - 4.88), 71.5, 75.87],[(x0, y0), (x1, y1),-34.16,-72.58],3],
            "c2": [[transform(-9.32 - 4.88, -4.71 + 4.88), transform(-9.32 + 4.88, -4.71 - 4.88), -1.11, 75.43],[(x0,y0), (x1, y1), -106.74, -73.15], 3],
            "c3": [[transform(-9.34 - 4.88, 4.68 + 4.88), transform(-9.34 + 4.88, 4.68 - 4.88), 1.32, -75.37],[(x0,y0), (x1,y1),180, -73.12], 3],
            "c4": [[transform(-0.37 - 4.89, 7.47 + 4.88), transform(-0.37 + 4.88, 7.47 - 4.88), -71.65, -75.18],[(x0, y0), (x1, y1), 34.16, 72.83],3],
            "c5": [[transform(4 - 5.24, 7.24 + 5.24), transform(4 + 5.24, 7.24 - 5.24), -57.31, -65.38],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 45, 90],4],
            "c6": [[transform(11.24 - 5.24, 0 + 5.24), transform(11.24 + 5.24, 0 - 5.24), 147.31, 65.38],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), -45, 90],4],
            "c7": [[transform(4 - 5.24, -7.24 + 5.24), transform(4 + 5.24, -7.24 - 5.24), 57.31, 65.38],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), -45, -90],4],
            }
    if n == 10:
        WIDTH, HEIGHT = 800, 600
        X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
        SCALE = 30
        x0, y0 = transform(-5.4 - 6.6, 0 + 6.6)
        x1, y1 = transform(-5.4 + 6.6, 0 - 6.6)
        coords_set = {
                "c0": [[transform(-2.62 - 4.12, 0 + 4.12), transform(-2.62 + 4.12, 0 - 4.12), 34.77, -69.53], [transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 144, 72],2],
                "c1": [[transform(5.11 - 12.25, -13.8 + 12.25), transform(5.11 + 12.25, -13.8 - 12.25), 110.78, 33.01],[(x0, y0), (x1, y1),-20.88, -63.61],3],
                "c2": [[transform(-13.07 - 12.18, -15.49 + 12.18), transform(-13.07 + 12.18, -15.49 - 12.18), 47.06, 33.18],[(x0,y0), (x1, y1), -84.56, -63.61], 3],
                "c3": [[transform(-22.58 - 12.08, 0 + 12.08), transform(-22.58 + 12.08, 0 - 12.08), 16.69, -33.43],[(x0,y0), (x1,y1),148.28, 63.55], 3],
                "c4": [[transform(-13.09 - 12.17, 15.46 + 12.17), transform(-13.09 + 12.17, 15.46 - 12.17), -46.94, -33.24],[(x0, y0), (x1, y1), 84.62, 63.66],3],
                "c5": [[transform(5.08 - 12.22, 13.79 + 12.22), transform(5.08 + 12.22, 13.79 - 12.22), -110.7, -33.12],[(x0, y0), (x1, y1), 20.88, 63.74],3],
                "c6": [[transform(1.95 - 4.14, 6.32 + 4.14), transform(1.95 + 4.14, 6.32 - 4.14), -37.43, -69.21],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 71.96, 72.04],4],
                "c7": [[transform(9.35 - 4.12, 3.89 + 4.12), transform(9.35 + 4.12, 3.89 - 4.12), -109.17, -69.6],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, 71.96],4],
                "c8": [[transform(9.36 - 4.12, -3.89 + 4.12), transform(9.36 + 4.12, -3.89 - 4.12), 109.22, 69.6],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, -71.99], 4],
                "c9": [[transform(1.95 - 4.14, -6.32 + 4.14), transform(1.95 + 4.14, -6.32 - 4.14), 37.43, 69.21],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), -71.99, -72.01],4]
                }
#mise_en_place(8,0)
#give_coords(8)