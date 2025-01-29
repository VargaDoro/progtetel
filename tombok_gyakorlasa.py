import random

def feltoltes():
    uj_lista = [] 
    for i in range(1,10):
        if i % 2 != 0:
            szam = random.randint(1, 10)
            while szam % 2 != 0: 
                szam = random.randint(1, 10)
            uj_lista.append(szam) 
        else:
            uj_lista.append(1)
    return uj_lista


def kiir(uj_lista):
    print(f"A lista elemei a feladat szerint: {uj_lista}")