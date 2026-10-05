from tkinter import *

def read():
    t = text.get(1.0, END)
    print(t)
window = Tk()
text = Text(width=30, height=8, bg='black', fg='red')
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text='Ввод',command=read)
b.pack()
b2 = Button(text='Вставка')
b2.pack()

window.mainloop()