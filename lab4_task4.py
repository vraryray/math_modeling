import numpy as np

def circle(a, b, N):
    x = np.linspace(a, b, N)
    y = x **2 
    return y 

print(circle(0, 1, 1000))