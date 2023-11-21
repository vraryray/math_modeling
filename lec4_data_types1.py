def changer(a, b):
    a = 2
    b[0] = 'good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(L)