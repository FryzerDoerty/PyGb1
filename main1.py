a = int(input('Введите количество монет:'))
o=0
r=0
for _ in range(0,a):
    b = int(input('Введите сторону, 0 - орел или 1 - решка:'))
    if(b==0):
        o+=1
    if(b==1):
        r+=1
if (o>r):
    print("минимум ", r)
else:
    print("минимум ", o)