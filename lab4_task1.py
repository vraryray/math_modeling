import numpy as np

def plus(sklad):                      #массив sklad
    s = 0
    for i in range(len(sklad)):
        s += sklad[i]
    return s/len(s)

test1 = np.arange(0, 100, 1)
plus(test1_1)  