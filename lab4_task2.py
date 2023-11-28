import numpy as np

def plus(sklad):
    s = 1
    for i in range(len(sklad)):
        s = s * sklad[i]
    return  s

test1 = np.arange(1, 10, 1)
print(plus(test1))