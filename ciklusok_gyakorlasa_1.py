import random

#13-ig megy a lista, 13 nincs kiirva
lista=[]
i:int=0
lista.append(random.randint(10, 15))
while lista[i]!=13:
    lista.append(random.randint(10, 15))
    i+=1
lista.remove(13)
print(lista)

#első 10 páros szám összege 
paros_ossz:int=0
i:int=0
while i <= 10:
    if i%2==0:
        paros_ossz+=i
    i+=1
print(paros_ossz)

#első 38db páratlan szám összege 24-től
paratan_ossz:int=0
for i in range(23, 38, 2):
    paratan_ossz+=i
i+=1
print(paratan_ossz)

#számok abszolút értéke 3-(-3)-ig
for x in range(-3, 4):
    print(f"|{x}| = {abs(x)}")