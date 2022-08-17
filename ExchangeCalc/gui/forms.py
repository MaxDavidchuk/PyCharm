import tkinter
from tkinter import Tk, Frame, PhotoImage, Label, Entry, Button
from tkinter import ttk, END
from lib.models import CalcManager
from tkinter import messagebox


class MainForm(object):

    CHECK = 0

    def __init__(self):
        self.__val = {0: ['usd.png', 'USD', 'Долар США', 36.77972, 33.10175],
                      1: ['eur.png', 'EUR', 'Євро', 37.39329, 33.65396],
                      2: ['gbp.png', 'GBP', 'Фунт Британії', 44.44948, 40.00453]}
        self.__usd = ['usd.png', 'USD', 'Долар США', 36.77972, 33.10175]
        self.__eur = ['eur.png', 'EUR', 'Євро', 37.39329, 33.65396]
        self.__gbp = ['gbp.png', 'GBP', 'Фунт Британії', 44.44948, 40.00453]
        self.__root = Tk()
        self.__image = PhotoImage(file='logo_2.png')
        self.__logo = Label(self.__root)
        self.__fr_left = Frame(self.__root)
        self.__flag_1 = PhotoImage(file='usd.png')
        self.__flag_11 = Label(self.__fr_left)
        self.__name_11 = Label(self.__fr_left)
        self.__name_12 = Label(self.__fr_left)
        self.__amount1 = ttk.Entry(self.__fr_left)
        self.__bt21 = Button(self.__fr_left)
        self.__bt22 = Button(self.__fr_left)
        self.__bt23 = Button(self.__fr_left)
        self.__fr_midle = Frame(self.__root)
        self.__r1 = ttk.Radiobutton(self.__fr_midle)
        self.__r2 = ttk.Radiobutton(self.__fr_midle)
        self.__fr_right = Frame(self.__root)
        self.__flag_2 = PhotoImage(file='uah.png')
        self.__flag_21 = Label(self.__fr_right)
        self.__name_31 = Label(self.__fr_right)
        self.__name_32 = Label(self.__fr_right)
        self.__amount2 = ttk.Entry(self.__fr_right)
        self.__action_img = PhotoImage(file='buy_bt.png')
        self.__action = Button(self.__fr_right)
        self.__input_widgets = dict()

    def __config(self) -> None:
        """ Налаштовує властивості віджетів"""
        bg1 = 'white'
        self.__root.title('Currency')
        self.__image = self.__image.subsample(1, 1)
        self.__logo.config(image=self.__image, bg=bg1)
        self.__root.config(bg=bg1)
        self.__fr_left.config(bg=bg1)
        self.__flag_1 = self.__flag_1.subsample(3, 3)
        self.__flag_11.config(image=self.__flag_1, bg=bg1)
        self.__name_11.config(width=4, font='Arial 14', text='USD', bg=bg1, justify='left')
        self.__name_12.config(font='Arial 10', text='Долар США', bg=bg1, justify='left')
        self.__amount1.config(width=10, justify='center', font='Arial 24')
        self.__bt21.config(width=4, text='USD', bg=bg1, bd=0, command=lambda m=0: self.__val_select(m))
        self.__bt22.config(width=4, text='EUR', bg=bg1, bd=0, command=lambda m=1: self.__val_select(m))
        self.__bt23.config(width=4, text='GBP', bg=bg1, bd=0, command=lambda m=2: self.__val_select(m))
        self.__fr_midle.config(bg=bg1)
        self.__var = tkinter.IntVar()
        s = ttk.Style()
        s.configure('w.TRadiobutton', background=bg1)
        self.__r1.config(text="Купити", value=1, variable=self.__var, style='w.TRadiobutton',
                         command=lambda m=1: self.__buy_sale(m))
        self.__r2.config(text="Продати", value=2, variable=self.__var, style='w.TRadiobutton',
                         command=lambda m=2: self.__buy_sale(m))
        self.__fr_right.config(bg=bg1)
        self.__flag_2 = self.__flag_2.subsample(3, 3)
        self.__flag_21.config(image=self.__flag_2, bg=bg1)
        self.__name_31.config(font='Arial 14', text='UAH', bg=bg1)
        self.__name_32.config(font='Arial 10', text='Гривня України', bg=bg1)
        self.__amount2.config(width=10, justify='center', font='Arial 24')
        self.__action.config(image=self.__action_img, bg=bg1, bd=0)

    def __layout(self) -> None:
        """ Менеджер розміщення """
        self.__logo.pack()
        self.__fr_left.pack(padx=20, pady=20, side='left', anchor='w')
        self.__flag_11.grid(row=0, column=0, sticky='w')
        self.__name_11.grid(row=0, column=1, sticky='w')
        self.__name_12.grid(row=0, column=2, sticky='w')
        self.__amount1.grid(row=1, columnspan=3, pady=10)
        self.__bt21.grid(row=2, column=0, padx=5)
        self.__bt22.grid(row=2, column=1, padx=5)
        self.__bt23.grid(row=2, column=2, padx=5, sticky='w')
        self.__fr_midle.pack(pady=20, side='left')
        self.__r1.pack(anchor='w')
        self.__r2.pack(anchor='w')
        self.__fr_right.pack(padx=20, pady=20)
        self.__flag_21.grid(row=0, column=0)
        self.__name_31.grid(row=0, column=1)
        self.__name_32.grid(row=0, column=2)
        self.__amount2.grid(row=1, columnspan=3, pady=10)
        self.__action.grid(row=2, columnspan=3)

    def __buy_sale(self, m: int):
        self.__action_img = PhotoImage(file='buy_bt.png' if m == 1 else 'sell_bt.png')
        self.__action.configure(image=self.__action_img)
        self.__amount2.delete(0, END)
        self.__amount1.focus()

    def __on_create(self) -> None:
        self.__var.set(1)
        self.__amount1.insert(0, '100')
        self.__amount1.focus()

    def __val_select(self, m: int):
        MainForm.CHECK = m
        self.__flag_1 = PhotoImage(file=self.__val[m][0])
        self.__flag_1 = self.__flag_1.subsample(3, 3)
        self.__flag_11.configure(image=self.__flag_1)
        self.__name_11.configure(text=self.__val[m][1])
        self.__name_12.configure(text=self.__val[m][2])
        self.__amount1.delete(0, END)
        self.__amount2.delete(0, END)
        self.__amount1.insert(0, '100')

    def __change_event(self, event) -> None:
        self.__group_input_widgets()
        calc_manager = CalcManager(self.__input_widgets)
        print(calc_manager)
        temp = self.__amount1
        if calc_manager.validate():
            result = calc_manager.calc()
            self.__amount2.delete(0, END)
            self.__amount2.insert(0, str(f'{result.amount:.2f}'))

    def __binding(self) -> None:
        """ Привязка методів до подій на віджетах форм """
        self.__amount1.bind('<KeyRelease>', self.__change_event)
        self.__action.bind('<Button-1>', self.__change_event)

    def __group_input_widgets(self) -> None:
        self.__input_widgets['amount1'] = self.__amount1.get()
        self.__input_widgets['rate1'] = self.__val[MainForm.CHECK][3] if self.__var.get() == 1 \
            else self.__val[MainForm.CHECK][4]
        self.__input_widgets['amount2'] = 1
        self.__input_widgets['rate2'] = 1

    def run(self) -> None:
        """ Менеджер запуску """
        self.__config()
        self.__layout()
        self.__on_create()
        self.__binding()
        self.__root.mainloop()
