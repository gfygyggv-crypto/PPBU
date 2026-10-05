from tkinter import *

window = Tk()
lb = Listbox(width=15, height=7)
lb.pack()
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
        'Пятница', 'Суббота', 'Воскресенье' ]
for day in days:
    lb.insert(END, day)
# lb.insert(0,'Понедельник')
# lb.insert(1,'Вторник')
# lb.insert(2,'Среда')
# lb.insert(3,'Четверг')
# lb.insert(4,'Пятница')
# lb.insert(5,'Суббота')
# lb.insert(6,'Воскресенье')


window.mainloop()