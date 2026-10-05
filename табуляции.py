import math
print("Число\t        Квадратный корень\t   Кубический корень")
print("=" * 50)
for i in range(2, 10):
    k = math.sqrt(i)
    k3 = i ** (1/3)
    print(f"{i:>5} \t{k:>18.2f}\t{k3:>18.2f}")