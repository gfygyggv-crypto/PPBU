from math import sqrt
a = 45
b = 34
c = 23
#s = a * b / 2
#print(s)
p = (a + b + c) /2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print(round(s, 2))