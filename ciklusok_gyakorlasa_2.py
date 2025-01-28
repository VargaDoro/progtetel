kerdes:str=str(input("Melyik variációt szeretnéd?(ismétlődő/nem simétlődő): "))

while kerdes!="nem ismétlődő" and kerdes!="ismétlődő":
    print("Helytelen válasz!")
    kerdes:str=str(input("Melyik variációt szeretnéd?(ismétlődő/nem simétlődő): "))

if kerdes=="nem ismétlődő":
    ossz=0
    for y in range(2,5):
        for x in range(2,5):
            for i in range(2,5):
                if y!=x and y!=i and x!=i:
                    print(y, x, i)
                    ossz+=1
    print("A variációk száma: ",ossz)

if kerdes=="ismétlődő":
    ossz=0
    for y in range(2,5):
        for x in range(2,5):
            for i in range(2,5):
                    print(y, x, i)
                    ossz+=1
    print("A variációk száma: ",ossz)