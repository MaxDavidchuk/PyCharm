from tkinter import Tk, Frame, PhotoImage, Label, Entry, Button
from tkinter import ttk
from tkinter import messagebox


class MainForm(object):

    def __init__(self):
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
        self.__fr_right = Frame(self.__root)
        self.__flag_21 = Label(self.__fr_right)
        self.__name_31 = Label(self.__fr_right)
        self.__name_32 = Label(self.__fr_right)
        self.__amount2 = ttk.Entry(self.__fr_right)


        #

    def __config(self) -> None:
        """ Налаштовує властивості віджетів"""
        bg1 = 'white'
        self.__root.title('Currency')
        self.__image = self.__image.subsample(1, 1)
        self.__logo.config(image=self.__image, bg=bg1)
        self.__root.config(bg=bg1)
        self.__flag_1 =
        self.__fr_left.config(bg=bg1)
        self.__name_11.config(font='Arial 14', text='USD', bg=bg1)
        self.__name_12.config(font='Arial 10', text='Долар США', bg=bg1)
        self.__amount1.config(width=10, justify='center', font='Arial 24')
        self.__bt21.config(text='USD')
        self.__bt22.config(text='EUR')
        self.__bt23.config(text='GBP')
        self.__fr_midle.config(bg=bg1)
        self.__fr_right.config(bg=bg1)

        #

    def __layout(self) -> None:
        """ Менеджер розміщення """
        self.__logo.pack()
        self.__fr_left.pack(padx=20, pady=20, side='left')
        self.__name_11.grid(row=0, column=1)
        self.__name_12.grid(row=0, column=2)
        self.__amount1.grid(row=1, columnspan=3, pady=10)
        self.__bt21.grid(row=2, column=0, padx=5)
        self.__bt22.grid(row=2, column=1, padx=5)
        self.__bt23.grid(row=2, column=2, padx=5)
        self.__fr_midle.pack(padx=20, pady=20, side='left')
        self.__fr_right.pack(padx=20, pady=20)

        #

    def __on_create(self) -> None:
        pass

    @staticmethod
    def __on_click(event) -> None:
        print(event)
        messagebox.showinfo('Повідомлення', 'Тут буде результат')
        # ...

    def __binding(self) -> None:
        """ Привязка методів до подій на віджетах форм """
        # self.__bt.bind('<Button-1>', self.__on_click)

    def run(self) -> None:
        """ Менеджер запуску """
        self.__config()
        self.__layout()
        self.__on_create()
        self.__binding()
        self.__root.mainloop()
