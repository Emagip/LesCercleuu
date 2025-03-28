#Projet : Circle Puzzle
#Auteurs : Victor Frappaz, Maxime Pigeaud, Fabian Peter

import tkinter as tk
#import time
import Fonctions_creation_var as FJeu
from random import shuffle

WIDTH, HEIGHT = 400, 300
X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
SCALE = 20

D_pos = {6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
         8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]}}

D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}
Matrice_Mouv = FJeu.creation_des_matrices(8, D_pos[8])
mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
JeuDepart = D_Jeux[8]
MonJeu = D_Jeux[8][:]
shuffle(MonJeu)
MonJeu1 = MonJeu.copy()
MonJeu2 = MonJeu.copy()

def transform(x, y):
    return X_OFFSET + x * SCALE, Y_OFFSET - y * SCALE

root = tk.Tk()
root.title("Le Jeu des cercles")

frame1 = tk.Frame(root)
frame1.pack(side = "left")

frame2 = tk.Frame(root)
frame2.pack(side="right")
canvas1 = tk.Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
canvas1.pack()
canvas2 = tk.Canvas(frame2, width=WIDTH, height=HEIGHT, bg="white")
canvas2.pack()
#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)

couleurs = [None, None, "white", "red", "blue"]
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
traced1 = {}
traced2 = {}
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
    traced2[nom] = [
            canvas2.create_arc(info[0][0][0], info[0][0][1],
                              info[0][1][0], info[0][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord',
                              start=info[0][2],extent = info[0][3]),

            canvas2.create_arc(info[1][0][0], info[1][0][1],
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
    canvas2.create_arc(info[0][0][0], info[0][0][1],
                      info[0][1][0], info[0][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[0][2],extent = info[0][3])

    canvas2.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[1][2],extent = info[1][3])



#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)
print(traced2)
def change1(pos):
    i = 0
    for nom, obj in traced1.items():
        canvas1.itemconfig(obj[0], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        canvas1.itemconfig(obj[1], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        i+=1
    root.update()


def change2(pos):
    i = 0
    for nom, obj in traced2.items():
        canvas2.itemconfig(obj[0], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        canvas2.itemconfig(obj[1], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        i+=1
    root.update()

change1(MonJeu)
change2(MonJeu)

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

def Grand_h2(event=None):
    global MonJeu2
    if not FJeu.fin(MonJeu2, JeuDepart):
        MonJeu2 = FJeu.rotation(MonJeu2,Matrice_Mouv[mes_dir[0][1]])
        change2(MonJeu2)
        fini()

def Grand_t2(event=None):
    global MonJeu2
    if not FJeu.fin(MonJeu2, JeuDepart):
        MonJeu2 = FJeu.rotation(MonJeu2,Matrice_Mouv[mes_dir[0][0]])
        change2(MonJeu2)
        fini()
def Petit_h2(event=None):
    global MonJeu2
    if not FJeu.fin(MonJeu2, JeuDepart):
        MonJeu2 = FJeu.rotation(MonJeu2,Matrice_Mouv[mes_dir[1][1]])
        change2(MonJeu2)
        fini()

def Petit_t2(event=None):
    global MonJeu2
    if not FJeu.fin(MonJeu2, JeuDepart):
        MonJeu2 = FJeu.rotation(MonJeu2,Matrice_Mouv[mes_dir[1][0]])
        change2(MonJeu2)
        fini()

def fini():
    if FJeu.fin(MonJeu2,JeuDepart):
        frame1.destroy()
        frame2.destroy()
        imgD = tk.Label(root,text="Le joueur 2 a gagné !")
        imgD.pack()
    elif FJeu.fin(MonJeu1,JeuDepart):
        frame1.destroy()
        frame2.destroy()
        imgV = tk.Label(root,text="Le joueur 1 a gagné !")
        imgV.pack()

root.bind('<Key-e>', Grand_h1)
root.bind('<Key-a>', Grand_t1)
root.bind('<Key-d>', Petit_h1)
root.bind('<Key-q>', Petit_t1)
root.bind('<Up>', Grand_h2)
root.bind('<Down>', Grand_t2)
root.bind('<Left>', Petit_h2)
root.bind('<Right>', Petit_t2)


root.mainloop()
