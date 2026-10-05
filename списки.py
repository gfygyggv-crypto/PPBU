"""List"""
"""Список - упорядоченный набор объектов"""

num = [22, 33, 44, 55, 99]
print(num[0])
print(num[2::-1])
print(num[::2])
print(num[1::-1])

nn = num
nn = num.copy()
print(num, id(num))
print(nn, id(nn))
print(nn is num)

"""Кортеж - упорядоченный набор неизменяемых объектов"""