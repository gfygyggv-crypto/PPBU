from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk

def qoit():
    window.destroy()

def open():
    try:
        file = fd.askopenfilename()
        if file:
            img = Image.open(file)
            imgconv = img
            width = int(ws.get())
            height = int(hs.get())
            img.thumbnail((width, height))
            imgtk = ImageTk.PhotoImage(img)
            img_window = Toplevel(window)
            img_window.title("Просмотр изображения")
            l = Label(img_window, image=imgtk)
            l.pack()
            l.image = imgtk
    except FileNotFoundError:
      mb.showerror("Ошибка", "Файл не найден")
    except OSError:
        mb.showerror("Ошибка", "Не удалось открыть возможно файл текстовый")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")

window = Tk()
window.title("Photo")
window.geometry("500x500")
Label(text="Ширина окна").pack()
ws = Spinbox(window, from_=100, to=500, increment=100)
ws.pack()

Label(text="Высота окна").pack()
hs = Spinbox(window, from_=100, to=500, increment=100)
hs.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=open)
filemenu.add_separator()
filemenu.add_command(label="Выход...", command=quit)
filemenu.add_separator()
mainmenu.add_cascade(label="Файл", menu=filemenu)

window.mainloop()