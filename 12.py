while True:
    print("\nВыберите операцию:")
    print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление")
    print("5. Просмотр истории вычислений\n6. Выход")

    choice = input("Введите номер операции: ")

    if choice == "6":
        break

    elif choice == "5":
        print("История вычислений:")
        try:
            with open("calculations.txt", "r") as file:
                print(file.read().strip())
        except FileNotFoundError:
            print("История пуста.")

    elif choice in ["1", "2", "3", "4"]:
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))

        if choice == "1":
            stroke = f"{a} + {b} = {a + b}"
        elif choice == "2":
            stroke = f"{a} - {b} = {a - b}"
        elif choice == "3":
            stroke = f"{a} * {b} = {a * b}"
        elif choice == "4":
            if b == 0:
                print("Делить на ноль нельзя!")
                continue
            stroke = f"{a} / {b} = {a / b}"

        print("Результат:", stroke)

        with open("calculations.txt", "a") as file:
            file.write("Результат: " + stroke + "\n")