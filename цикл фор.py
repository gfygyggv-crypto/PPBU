# for i in 23, 45, 22, 32:
#     print(i, 'YES') #итеррация
# for i in range(10): # Start=0, Stop, Step=+1
#     print(i, end= ' ')

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j : 2}', end=' ')
    print()