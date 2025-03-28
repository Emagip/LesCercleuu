import tkinter as tk
#import time
import Fonctions_creation_var as FJeu
from random import shuffle

WIDTH, HEIGHT = 800, 600
X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
SCALE = 30

D_pos = {6:{"c1T":[1,2,3,0,4,5],"c1H":[3,0,1,2,4,5],"c2T":[4,1,2,3,5,0],"c2H":[5,1,2,3,0,4]},
         8:{"c1T":[1,2,3,4,0,5,6,7],"c1H":[4,0,1,2,3,5,6,7],"c2T":[5,1,2,3,4,6,7,0],"c2H":[7,1,2,3,4,0,5,6]},
         10:{"c1T":[1,2,3,4,5,0,6,7,8,9],"c1H":[5,0,1,2,3,4,6,7,8,9],"c2T":[6,1,2,3,4,5,7,8,9,0],"c2H":[9,1,2,3,4,5,0,6,7,8]}
         }

D_Jeux = {6:[2,3,3,3,4,4],8:[2,3,3,3,3,4,4,4],10:[2,3,3,3,3,3,4,4,4,4]}
Matrice_Mouv = FJeu.creation_des_matrices(10, D_pos[10])
mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]
JeuDepart = D_Jeux[10]
MonJeu = D_Jeux[10][:]
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
                      width=4,
                      start=info[0][2],extent = info[0][3])

    canvas1.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=4,
                      start=info[1][2],extent = info[1][3])
    canvas2.create_arc(info[0][0][0], info[0][0][1],
                      info[0][1][0], info[0][1][1],
                      outline='black', style='arc',
                      width=4,
                      start=info[0][2],extent = info[0][3])

    canvas2.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=4,
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
