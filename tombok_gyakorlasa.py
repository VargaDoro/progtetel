import random

i = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
uj_lista = [] 

while i < len(lista):
    if lista[i]%2!= 0:
        szam = random.randint(1, 10)  
        if szam%2 == 0:
            uj_lista.append(szam) 
        else:
            pass
    else:
        uj_lista.append(1) 
    i += 1  

print(uj_lista)
