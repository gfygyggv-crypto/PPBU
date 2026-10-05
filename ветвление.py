"""Операции сравнения"""
""" >, <, >=, <=, !=, = """
a = 46
b = 36
c = a > b
print(c)

if a > b:
    print("A > B")
else:
    print("j")


color  = input("Цвет светофорв: ")
match color:
     case 'red' | 'no':
         print('STOP')
     case 'green':
         print("GO")
     case _:
         print('цвет', color)