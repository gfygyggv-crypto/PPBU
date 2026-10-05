# Создаём фреймы
frame1 = Frame(window)
frame1.pack()  # или frame1.pack(pady=10) для отступов

frame2 = Frame(window)
frame2.pack()

# Метка с инструкцией
m = Label(frame1, height=3, text="Введите три числа и нажмите на кнопку для вычисления суммы")
m.pack()

# Поля ввода
e1 = Entry(frame1)
e1.pack()
e2 = Entry(frame1)
e2.pack()
e3 = Entry(frame1)
e3.pack()

# Кнопки
b = Button(frame1, text="Сложить три числа", command=summ)
b.pack()
b2 = Button(frame2, text="Умножить три числа", command=multiply)
b2.pack()

# Метка для результата
m1 = Label(window)
m1.pack()
