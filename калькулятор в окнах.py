from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено целое число")
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено целое число")
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено целое число")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)
    summ = slag_1 + slag_2 + slag_3
    m1['text'] = f"{s1} + {s2}  + {s2} = {summ}"
    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

def multiply():

    j1 = e1.get()
    if not j1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено целое число")
        return
    j2 = e2.get()
    if not j2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено целое число")
        return
    j3 = e3.get()
    if not j3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено целое число")
        return
    multiply_1 = int(j1)
    multiply_2 = int(j2)
    multiply_3 = int(j3)
    multiply = multiply_1 * multiply_2 * multiply_3
    m2['text'] = f"{j1} * {j2}  * {j2} = {multiply}"

    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()


window = Tk()
window.title("Калькулятор")
m = Label(height=3, text="Введите три числа и нажмите на кнопку для вычисления суммы")
m.pack()

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()


e1 = Entry(frame1)
e1.pack()
e2 = Entry(frame1)
e2.pack()
e3 = Entry(frame1)
e3.pack()
b = Button(frame1, text="Сложить три числа", command=summ)
b.pack()
m1 = Label(window)
m1.pack()
b2 = Button(frame1, text="Умножить три числа", command=multiply)
b2.pack()
m2 = Label()
m2.pack()


window.mainloop()