n = int(input())
a = 1
b = 1
output = [1, 1]
for i in range(n):
    c = a + b
    a = b
    b = c 
    output.append(c)
print(output)