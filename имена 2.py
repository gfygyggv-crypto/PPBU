import random

name = []
job =[]
names = int(input("Сколько имен введете?"))
jobs = int(input("Сколько профессий введете?"))
for i in range(names):
    name.append(input("Введите имя:"))
for i in range(jobs):
    job.append(input("Введите профессию:"))
print(name)
print(job)

rnd_name = random.randint(0,names)
rnd_job = random.randint(0, jobs)
age = random.randint(5,25)

print(f"Меня зовут {name[rnd_name]} мне {age} лет, я {job[rnd_job]}.")