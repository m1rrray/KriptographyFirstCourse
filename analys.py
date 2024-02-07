from methods import Affine_rec
from itertools import product

dig = [i for i in range(1,26)]
alpabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'KUYUMC GEVSSJC TSBCUTCW TCSMSRT KCKMPR KUYUMC TJGNWS UQLA ECPBAKLLWT RCGBGL TMEUWCQY'
text = text.split(' ')

for i in product(dig, repeat = 4):
    k1,k2,k3,k4 = i[0],i[1],i[2],i[3]
    mes = []
    for j in text:
        mes += [Affine_rec.decode(alpabet_upper, j, k1,k2,k3,k4)]
    print(*mes)
    if mes[0] == 'LONDON':
        break

    

