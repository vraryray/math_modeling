y = 0
for i in range(1, 10):
    for x in range(1, 10):
        y += 1
        print(i * x, end = ' ')
        if y % 9 == 0:
            print(end='\n')
