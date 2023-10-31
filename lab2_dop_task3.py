a = int(input())
b = a % 10
c = b
a = a // 10  
while a > 0:
    b = a % 10
    a = a // 10
    c = c * 10
    c = c + b
print(c)    