n = int(input())
a = int(input())
if a == 0:
    print('Нельзя делить на ноль')
elif n // a:
    c = n // a
    d = n % a
    print(f'Число {n} делится на число {a}, целая часть равна {c}, остаток равен {d}')  
else:
    print('Нельзя делить')       