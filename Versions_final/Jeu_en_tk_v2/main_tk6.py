#Projet : Circle Puzzle
#Auteurs : Victor Frappaz, Maxime Pigeaud, Fabian Peter

import tkinter as tk
#import time
import Fonctions_creation_var as FJeu
from random import shuffle

WIDTH, HEIGHT = 800, 600
X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
SCALE = 40

D_pos = {6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]}}
D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}
Matrice_Mouv = FJeu.creation_des_matrices(6, D_pos[6])
mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
JeuDepart = D_Jeux[6]
MonJeu = D_Jeux[6][:]
shuffle(MonJeu)

MonJeu1 = MonJeu.copy()
MonJeu2 = MonJeu.copy()

def transform(x, y):
    return X_OFFSET + x * SCALE, Y_OFFSET - y * SCALE

root = tk.Tk()
root.title("Le Jeu des cercles")

frame1 = tk.Frame(root)
frame1.pack(side = "left")

canvas1 = tk.Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
canvas1.pack()
#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)

couleurs = [None, None, "white", "red", "blue"]
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
traced1 = {}
for nom, info in coords_set.items():
    traced1[nom] = [
            canvas1.create_arc(info[0][0][0], info[0][0][1],
                              info[0][1][0], info[0][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord',
                              start=info[0][2],extent = info[0][3]),

            canvas1.create_arc(info[1][0][0], info[1][0][1],
                              info[1][1][0], info[1][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord', 
                              start=info[1][2],extent = info[1][3])
            ]
    canvas1.create_arc(info[0][0][0], info[0][0][1],
                      info[0][1][0], info[0][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[0][2],extent = info[0][3])

    canvas1.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[1][2],extent = info[1][3])



#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)
def change1(pos):
    i = 0
    for nom, obj in traced1.items():
        canvas1.itemconfig(obj[0], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        canvas1.itemconfig(obj[1], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        i+=1
    root.update()

change1(MonJeu)

def Grand_h1(event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[0][1]])
        change1(MonJeu1)
        fini()

def Grand_t1(event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[0][0]])
        change1(MonJeu1)
        fini()
def Petit_h1(event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[1][1]])
        change1(MonJeu1)
        fini()

def Petit_t1(event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[1][0]])
        change1(MonJeu1)
        fini()

def fini():
    if FJeu.fin(MonJeu2,JeuDepart):
        frame1.destroy()
        imgD = tk.Label(root,text="vous avez perdu !")
        imgD.pack()
    elif FJeu.fin(MonJeu1,JeuDepart):
        frame1.destroy()
        imgV = tk.Label(root,text="Vous avez gagné !")
        imgV.pack()

root.bind('<Key-e>', Grand_h1)
root.bind('<Key-a>', Grand_t1)
root.bind('<Key-d>', Petit_h1)
root.bind('<Key-q>', Petit_t1)

root.mainloop()
