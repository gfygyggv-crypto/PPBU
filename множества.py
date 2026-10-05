f = {"яблоко", "банан", "вишня", "груша", "апельсин", "манго"}
f2 = {"груша", "апельсин", "манго"}
f4 = f.intersection(f2)
f3 = f.union(f2)
# f.add("мандарин")
# f.discard("банан")
print(f2.issubset(f))
# print("яблоко" in f)
