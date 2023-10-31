a = int(input())
b = int(input())
c = int(input())
D = (b**2) - (4 * a * c) 
if D > 0:
    import math
    d = math.sqrt(D)
    x1 = (-1 * b + d)/(2 * a)
    x2 = (-1 * b - d)/(2 * a)
    print(x1, x2)
elif D == 0:
    x = (-1 * b)/(2 * a) 
    print(x)  
else:
    print('Нет корней')