def affiche_jeu(J,Lsymb):
    """ affiche un jeu à 2 cycles 2 couleurs 1 case vide \
        Lsymb permet de remplacer les int 0,1,2 par \
        des lettres approopriées (p.ex.  'o', 'A', 'B' ) \
        inapproprié pour les len(J) != 6 ou 8"""
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
            print("  "+Lcar[3]+"    |   \ ")
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
            print("  "+Lcar[4]+"     |     \ ")
            print("  |     "+Lcar[0]+"      "+Lcar[9])
            print("  "+Lcar[3]+"     |     / ")
            print("  '-"+Lcar[2]+"-"+Lcar[1]+"-'-"+Lcar[11]+"-"+Lcar[10]+"'")
    else :
        print("je ne sais pas faire")

Lcarac2 = [[0,None],[1,None],[2,"o"],[3,"A"],[4,"B"],[5,"C"],[6,"D"],[7,"E"],[8,"F"]]
JJ = [2,3,3,3,4,4]
affiche_jeu(JJ,Lcarac2)