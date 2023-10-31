a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        b = a // i
        if i < b:
            print(i, b) 