def get_number(prompt):
    while  True:
        value = input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        else:
            print("Это не целое число")



def add(x,y):
    return x + y
def subtruct(x,y):
    return x - y
def multiply(a,b):
    return a * b
def devide(x, y):
    if y == 0:
        return "Ошибка. Деление на ноль"
    else:
        return  x / y

def log(result):
    try:
        with open("calculations.txt", 'a') as file:
            file.write(result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
# def show_history():
#     print("История вычислений:")
#     if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
#         print("История пуста (файл не найден или пуст).")
#         return

print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Просмотр истории вычислений")
print("0. Выход")

valid_choices = ['1', '2', '3', '4', '5']
choice = None
while choice not in valid_choices:
    choice = input("Введите номер операции (1/2/3/4/5): ")
    if choice not in valid_choices:
        print("Вы ввели не 1 2 3 4 5")



num1 = get_number("Введите первое число: ")
num2 = get_number("Введите второе число: ")

if choice == "1":
    print(f"Результат: {num1} + {num2} = {add(num1,num2)}")
elif choice == "2":
    print(f"Результат: {num1} - {num2} = {subtruct(num1,num2)}")
elif choice == "3":
    print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == "4":
    result = devide(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат: 4"
              f"{num1} / {num2} = {result}")
elif choice == "5":
        print("История вычислений:")
        try:
            with open("calculations.txt", "r") as file:
                print(file.read().strip())
        except FileNotFoundError:
            print("История пуста.")


else:
    print("Неверный выбор операциию.")


