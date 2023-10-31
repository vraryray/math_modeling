a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print ('Треугольник возможен')
    if a != b != c:
        print('Разносторонний треугольник')
    elif a == b == c:
        print('Равносторонний треугольник')
    else:
        print('Равнобедренный треугольник')    
else:
    print('Треугольник невозможен')    