import math

def f1_Elso10SzamOsszege():
    ossz:int=0
    i:int=0
    while i<=10:
        ossz+=i
        i+=1
    return ossz

def osszead(a, b):
    eredmeny=a+b
    return eredmeny

def f2_KettoSzamOsszege(eredmeny):
    '''ketossz=szam1+szam2
    return ketossz'''

def f3_NegySzamOsszege(eredmeny):
    '''negyossz=szam1+szam2+szam3+szam4
    return negyossz'''

def f4_HaromSzamOsszegeGyoke(szam1, szam2 ,szam3):
    haromossz=szam1+szam2+szam3
    haromgyok=math.sqrt(haromossz)
    return haromgyok

def kiirKonzolra(eredmeny, haromgyok):
    print(f"A két szám összege: {eredmeny}, négy szám összege: {2*eredmeny} és három szám összegének gyöke: {haromgyok}")

eredmeny=osszead(a=4, b=5)
ossz=f1_Elso10SzamOsszege()
f2_KettoSzamOsszege(eredmeny)
f3_NegySzamOsszege(eredmeny)
haromgyok=f4_HaromSzamOsszegeGyoke(2,5,8)

kiirKonzolra(eredmeny, haromgyok)