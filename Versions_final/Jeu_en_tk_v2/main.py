import tkinter as tk
from miseEnPlace import *

#interface

Acceuil = tk.Tk()
Acceuil.title("Le jeu des cercles")
Acceuil.config(bg="White")

Cadre = tk.Canvas(Acceuil,bg="black",width=1000, height = 1000)

#fonctions de lancement

def Jeu1v1_6():
    import main_tk6_duo

def Jeu1v1_8():
    import main_tk8_duo

def Jeu1v1_10():
    import main_tk10_duo

def JeuPvE_6(n,exen):
    mise_en_place(n,exen)
    give_coords(n)
    import tk_6_ordi

def JeuSolo6():
    import main_tk6

def JeuSolo8():
    import main_tk8

def JeuSolo10():
    import main_tk10

def afficheDiff():
    difficult.destroy()
    t1 = tk.Label(Cadre,text="Difficultés",fg="red")
    t1.pack(fill="x")
    diff_1 = tk.Button(Cadre,text="extrèmement facile",command=lambda :JeuPvE_6(6,2))
    diff_1.pack(fill="x")
    diff_2 = tk.Button(Cadre,text="très facile",command=lambda :JeuPvE_6(6,1))
    diff_2.pack(fill="x")
    diff_3 = tk.Button(Cadre,text="facile",command=lambda :JeuPvE_6(6,0))
    diff_3.pack(fill="x")
    diff_4 = tk.Button(Cadre,text="moyen facile",command=lambda :JeuPvE_6(8,4))
    diff_4.pack(fill="x")
    diff_5 = tk.Button(Cadre,text="moyen",command=lambda :JeuPvE_6(8,2))
    diff_5.pack(fill="x")
    diff_6 = tk.Button(Cadre,text="moyen dur",command=lambda :JeuPvE_6(8,0))
    diff_6.pack(fill="x")
    diff_7 = tk.Button(Cadre,text="dur",command=lambda :JeuPvE_6(10,6))
    diff_7.pack(fill="x")
    diff_8 = tk.Button(Cadre,text="extrème",command=lambda :JeuPvE_6(10,4))
    diff_8.pack(fill="x")
    diff_9 = tk.Button(Cadre,text="expert",command=lambda :JeuPvE_6(10,0))
    diff_9.pack(fill="x")

def affiche1v1():
    b1v1.destroy()
    t2 = tk.Label(Cadre,text="Modes de Jeu 1v1",fg="red")
    t2.pack(fill="x")
    b1v1_6 = tk.Button(Cadre,text="Jeu 1v1 sur la taille 6 du cercle",command=Jeu1v1_6)
    b1v1_6.pack(fill="x")
    b1v1_8 = tk.Button(Cadre,text="Jeu 1v1 sur la taille 8 du cercle",command=Jeu1v1_8)
    b1v1_8.pack(fill="x")
    b1v1_10 = tk.Button(Cadre,text="Jeu 1v1 sur la taille 10 du cercle",command=Jeu1v1_10)
    b1v1_10.pack(fill="x")

def afficheSolo():
    bsolo.destroy()
    t3 = tk.Label(Cadre,text="Modes de Jeu Solo",fg="red")
    t3.pack(fill="x")
    bc6 = tk.Button(Cadre,text="Jeu solo sur la taille 6 du cercle",command=JeuSolo6)
    bc6.pack(fill="x")
    bc8 = tk.Button(Cadre,text="Jeu solo sur la taille 8 du cercle",command=JeuSolo8)
    bc8.pack(fill="x")
    bc10 = tk.Button(Cadre,text="Jeu solo sur la taille 10 du cercle",command=JeuSolo10)
    bc10.pack(fill="x")

#boutons mode de jeu solo

bsolo = tk.Button(Cadre,text="Modes de Jeu solo",command=afficheSolo,fg="red")
bsolo.pack(side="left",fill="y")

#boutons mode de jeu 1v1

b1v1 = tk.Button(Cadre,text="Modes de Jeu 1v1",command=affiche1v1,fg="red")
b1v1.pack(side="left",fill="y")

#les boutons de diff

difficult = tk.Button(Cadre,text="Modes de Jeu ordi vs joueur",command=afficheDiff,fg="red")
difficult.pack(side="left",fill="y")

Cadre.pack()
Acceuil.mainloop()