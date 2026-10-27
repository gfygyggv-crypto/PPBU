from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint

from bottle import response

def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://er-api.com{base_currency}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and "rates" in data:
            return data["rates"].get(target_currency, None)
        return None
    except Exception as e:
        print(f"Ошибка запроса: {e}")
        return None


def update_currencies_label(event):
    code = target_combobox.get()
    # code = combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    two_label.config(text=name)


def update_two_label():
    code = two_combobox.get()
    name = currencies[code]
    two_label.config(text=name)


def exchange():
    base_code = base_combobox.get().strip()
    two_code = two_combobox.get().strip()
    target_code = target_combobox.get().strip()
    rate1 = get_exchange_rate(base_code, target_code)
    rate2 = get_exchange_rate(two_code, target_code)
    # code = entry.get().upper().strip()
    # code = combobox.get()


    if target_code and base_code and two_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate1 = get_exchange_rate(base, target)
                exchange_rate1 = get_exchange_rate(two, target)
                base = currencies[base_code]
                target = currencies[target_code]
                two = currencies[two_code]
                # currency_name = currencies[code]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.1f} к {two} к {target} за 1 {base}')
            else:
                mb.showerror('Ошибка',
                             f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
      'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'

}

root = Tk()
root.title('Курс обмена валют USD')
root.geometry('360x180')

Label(root, text='Базовая  валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Вторая  валюта').pack()
two_combobox = ttk.Combobox(root, values=list(currencies.keys()))
two_combobox.pack(pady=3, padx=10)
two_combobox.bind('<<ComboboxSelected>>', update_two_label)
two_label = ttk.Label()
two_label.pack()


Label(root, text='Целевая валюта').pack(padx=10)
# popular_currencies = ['EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF',
#                       'CNY', 'RUB', 'KZT', 'UZS']
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=10, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currencies_label)

target_label = ttk.Label()
target_label.pack()
# entry = Entry(root)
# entry.pack()

Button(text='Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)

root.mainloop()
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)