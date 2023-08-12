import math
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))    
a =0
b =0
while(a<1000 and b<1000):
  res = s*s + 4*(-p)
  res = int(math.sqrt(res))
  b = (-s+res)//(-2)
  a = s - b
  print(a, b)
  break