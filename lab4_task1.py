import numpy as np

def plus(sklad):                      #массив sklad
    s = 0
    for i in range(len(sklad)):
        s = s + sklad[i]
    return s / len(sklad)

test1 = np.arange(0, 100, 1)
print(plus(test1))  