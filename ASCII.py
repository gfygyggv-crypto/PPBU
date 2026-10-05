for i in range(256):
    print(f"Символ {chr(i)} код символа {i}")
print(ord("A"))
alf = 'abcdefghijklmnopqrstuvwxyz'
print(f"Код символа {alf[0]} - {ord(alf[0])}")
alf = 'abcdefghijklmnopqrstuvwxyz'
for b in alf:
    print(f"Код символа {b} - {ord(b)}")
smile = '( ˘⌣˘)♡(˘⌣˘ )'
# for b in smile:
#   print(f"Код символа {b} - {ord(b)}")
print(smile[:6])
print(smile[:7])
print(smile[6:])
print(smile[7:])

