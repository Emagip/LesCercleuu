matrice_test = [[0,0,0,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[1,0,0,0,0,0],[0,0,0,0,1,0]]
def conv_str(matrice_in):
    conv_out = str(len(matrice_in))+"$"
    for lignes in matrice_in:
        actu = ""
        for bits in lignes:
            actu += str(bits)
        conv_out += str(int(actu,2)) + ":"
    return conv_out

def conv_matrice(str_in):
    conv_out = []
    long_ligne = ""
    i = 0
    while str_in[i] != "$":
        char = str_in[i]
        long_ligne += char
        i += 1
    long_ligne = int(long_ligne)
    i+=1
    char = str_in[i]
    print(f'long_ligne: {long_ligne}')
    print(f'len: {len(str_in)}')
    lastr = ""
    for char in str_in[i:]:
        lastr += char
    actu = ""
    for char in lastr:
        if char == ":":
            actu = ("{0:b}".format(int(actu)))
            if len(actu) < long_ligne:
                actu  = "0"*(long_ligne-len(actu)) + actu
            conv_out.append([int(c) for c in actu])
            actu = ""
        else :
            actu += char
    return conv_out


a = conv_str(matrice_test)
print(a)
print(conv_matrice(a))
