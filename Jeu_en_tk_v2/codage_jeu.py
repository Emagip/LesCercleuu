def encoder_jeu(jeu):
    """Encode le vecteur colonne qui représente le jeu en un int
    -> enlève 2 à chaque chiffre du vecteur colonne puis convertit en base 4"""
    nv_jeu = ''
    for val in jeu:
        nv_jeu += str(val-2)
    return int(nv_jeu, 4)

def decoder_jeu(jeu_encode,n):
    """Permet de décoder un jeu encodé pour retrouver la position de chaque côte"""
    
    resu = ''
    while jeu_encode != 0:
        resu=str(jeu_encode%4+2)+resu
        jeu_encode//=4

    while len(resu)<n:
        resu = '2'+resu
    return [int(x) for x in resu]
