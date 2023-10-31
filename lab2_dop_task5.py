a = int(input())
for i in range(a):
    b = 0
    for j in range(1, i):
        if i % j == 0:
            b += j
    if b == i:
        print(i)