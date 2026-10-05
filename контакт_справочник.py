contacts = {}

def input_contact():
    name = input("Введите имя: ")
    phone = input("Введите десятизначный номер телефона начинающийся с 9")
    if len(phone) == 10 and phone.isdigit() and phone.startswith("9"):
        contacts[name] = phone
        print("Контакт успешно добавлен")
        print(contacts)
    else:
        print("Ошибка! Неверный номер телефона")

def find_contact():
    name = input("Введите имя для поиска: ")
    print(contacts.get(name, "Контакт не найден"))
    # if name in contacts:
    #     print(contacts[name])
    # else:
    #     print("Контакт не найден.")

def delete_contact():
    name = input("Ввведите имя для удаления")
    if name in contacts:
        del contacts[name]
        print(contacts)
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")
while True:
    action = input("Выберите действие: добавить (1), найти (2), удалить (3), выйти (4)")
    if action == "1":
        input_contact()
    elif action == "2":
        find_contact()
    elif action == "3":
        delete_contact()
    elif action == "4":
        break
    else:
        print("Неверный ввод. Введите 1, 2,3,4")
