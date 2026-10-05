from tkinter import *


def answer(event):
    answ = num.get().strip()
    result.configure(text=answ)

root = Tk()
root.title('Старт')
#root.geometry("300x400")
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 300
Y = 100

root.geometry(f"{X}x{Y}+{WIDTH // 2 - X //2}+"
              f"{HEIGHT // 2 - Y // 2 - 25}")

prompt = Label(text='Введите значение', font='Arial 12')

#prompt.pack(side=LEFT)
prompt.pack()
# prompt.pack(side=BOOTTON)
# prompt.pack(side=RIGHT)


num = Entry(width=5,font='Arial 12')
num.pack()

result = Label(text='    ', font='Arial 15', bg='Lightgray')
result.pack(pady=10)



num.bind('<Return>', answer)
root.mainloop()
