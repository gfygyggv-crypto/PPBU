import random

name = ["Маша", "Марат", "Ашот", "Аюр", "Кар"]
job = ["Строитель", "доставщик", "повар", "балерина", "школьник", "бомж"]
rnd_name = random.randint(0,4)
rnd_job = random.randint(0,6)
age = random.randint(5,25)
print(f"Меня зовут {name[rnd_name]} мне {age} лет, я {job[rnd_job]}.")