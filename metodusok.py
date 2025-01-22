import random

def elso():
    lista=[]
    for i in range(10):
        lista.append(random.randint(5,15))
    print(lista)
    return lista

def megszamlalas(lista):
    i:int=0
    db:int=0
    while i < len(lista):
        if lista[i]==7:
            db+=1
        i+=1
    print(f"7-esek a listában: {db}")

def osszegzes(lista):
    ossz:int=0
    i:int=0
    while i < len(lista):
        ossz+=lista[i]
        i+=1
    print(f"A lista elemeinek osszege: {ossz}")

def eldontes(lista):
    i=0
    N=len(lista)
    while i<N and lista[i]!=13:
        i+=1
    i<N

def eldontes_masodik(lista):
    i=0
    N=len(lista)
    while i<N and lista[i]==13:
        i+=1
    i>=N

def l_kereses(lista):
    i=0
    N=len(lista)
    while i<N and lista[i]!=13:
        if lista[i]==13:
            print(lista[i])
        else:
            print("Nincs")
        i+=1
    i<N
    