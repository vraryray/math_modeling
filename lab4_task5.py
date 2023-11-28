from constant import p_number as p

def square(who, a = 1, b = 1, h = 1, r = 1):
    if who == 'rectangle':
        S = a * b
    elif who == 'triangle':
        S = (a * h)/ 2
    else:
        S = p*r**2
    return S
print(square('triangle', a = 2, h = 3))       