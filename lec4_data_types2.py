#Complex numbers
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)

print(z + w)

#Strings
s = 'hello'
print(s[0])

#s[0] = 'h'

#Tuple
t = (1, 4, 9)
print(t)
print(t[0])
#t[0] = 3

#List
l = [1, 4, 9]
l[0] = 2
print(l)

#Dictionary
d = {'a1':4, 4:'a1', 'str':'hello'}
print(d['a1'])
print(d[4])
print(d['str'])

d['str'] = 'good'
print(d)