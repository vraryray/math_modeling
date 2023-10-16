year = int(input())
if year % 4 == 0:
    print('Високосноый год')
elif year % 4 == 0 and year % 100 != 0:
    print('Високосноый год')
else:
    print('Невисокосный год')    