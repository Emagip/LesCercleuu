import tkinter as tk
from miseEnPlace import *

root = tk.Tk()

mes_dir = [["c1T_M","c1H_M"],["c2T_M","c2H_M"]]

frame1 = tk.Frame(root)
frame1.pack(side = "left")

frame2 = tk.Frame(root)
frame2.pack(side="right")
canvas1 = tk.Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
canvas1.pack()
canvas2 = tk.Canvas(frame2, width=WIDTH, height=HEIGHT, bg="white")
canvas2.pack()

couleurs = [None, None, "white", "red", "blue"]
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

def Petit_h1(root,event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[1][1]])
        change1(MonJeu1)
        fini()

def Petit_t1(root,event=None):
    global MonJeu1
    if not FJeu.fin(MonJeu1, JeuDepart):
        MonJeu1 = FJeu.rotation(MonJeu1,Matrice_Mouv[mes_dir[1][0]])
        change1(MonJeu1)
        fini()

mouv_ordi = 0
def OrdiJoue():
    global MonJeu2, mouv_ordi
    if not FJeu.fin(MonJeu2, JeuDepart) and not FJeu.fin(MonJeu1,JeuDepart):
        root.after(2000, OrdiJoue)
        MonJeu2 = FJeu.rotation(MonJeu2, Matrice_Mouv[MesMouv[mouv_ordi]])
        print(mouv_ordi)
        print(MesMouv[mouv_ordi])
        mouv_ordi += 1
        change2(MonJeu2)
        fini()

def fini():
    if FJeu.fin(MonJeu2,JeuDepart):
        frame1.destroy()
        frame2.destroy()
        imgD = tk.Label(root,text="vous avez perdu !")
        imgD.pack()
    elif FJeu.fin(MonJeu1,JeuDepart):
        frame1.destroy()
        frame2.destroy()
        imgV = tk.Label(root,text="Vous avez gagné !")
        imgV.pack()


change1(MonJeu1)
change2(MonJeu2)

root.bind('<Key-e>', Grand_h1)
root.bind('<Key-a>', Grand_t1)
root.bind('<Key-d>', Petit_h1)
root.bind('<Key-q>', Petit_t1)

OrdiJoue()

root.mainloop()
