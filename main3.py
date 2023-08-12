N =  int(input('Введите число: '))
i=0
a=0
while(a<N):
    a = 2**i 
    i+=1
    if(a>N):
        break
    print(a)