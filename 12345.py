flag1 = False
flag2 = False

for _ in range(5):
    word = input()

    if word == 'Плутон':
        flag1 = True
    if 'тер' in word:
        flag2 = True

print(flag1)
print(flag2)