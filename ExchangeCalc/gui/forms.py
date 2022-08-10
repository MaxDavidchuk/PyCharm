from tkinter import Tk, Frame, PhotoImage, Label, Entry, Button
from tkinter import ttk
from tkinter import messagebox


class MainForm(object):

    def __init__(self):
        self.__root = Tk()
        self.__frame = Frame(self.__root)
        self.__panel = Frame(self.__frame)
        self.__image = PhotoImage(file='logo_2.png')
        self.__logo = Label(self.__frame)
        #
        self.__a1 = Entry(self.__panel)
        self.__div1 = Label(self.__panel)
        self.__b1 = Entry(self.__panel)

        #
        self.__a2 = Entry(self.__panel)
        self.__div2 = Label(self.__panel)
        self.__b2 = Entry(self.__panel)

        #
        self.__a3 = Entry(self.__panel)
        self.__div3 = Label(self.__panel)
        self.__b3 = Entry(self.__panel)

        #
        self.__op = Entry(self.__panel)
        self.__bt = Button(self.__panel)
        self.__ip = Entry(self.__panel)

    def __config(self) -> None:
        """ Налаштовує властивості віджетів"""
        bg1 = 'white'
        self.__root.title('Currency')
        self.__root.config(bg=bg1)
        self.__panel.config(bg=bg1)
        self.__image = self.__image.subsample(1, 1)
        self.__logo.config(image=self.__image, bg=bg1)
        #
        self.__a1.config(width=4, justify='center', font='Arial 24', fg='blue')
        self.__div1.config(text='-----------', font='Arial 16')
        self.__b1.config(width=4, justify='center', font='Arial 24', fg='blue')
        #
        self.__a2.config(width=4, justify='center', font='Arial 24', fg='blue')
        self.__div2.config(text='-----------', font='Arial 16')
        self.__b2.config(width=4, justify='center', font='Arial 24', fg='blue')
        #
        self.__a3.config(width=4, justify='center', font='Arial 24', fg='purple')
        self.__div3.config(text='-----------', font='Arial 16')
        self.__b3.config(width=4, justify='center', font='Arial 24', fg='purple')
        #
        self.__op.config(width=3, justify='center', font='Arial 20', fg='red')
        self.__bt.config(font=24, text='=', width=3, fg='red')
        self.__ip.config(width=4, justify='center', font='Arial 24', fg='purple')

    def __layout(self) -> None:
        """ Менеджер розміщення """
        self.__frame.pack(padx=20, pady=20)
        self.__logo.pack()
        self.__panel.pack(pady=20)
        #
        self.__a1.grid(row=0, column=0)
        self.__div1.grid(row=1, column=0)
        self.__b1.grid(row=2, column=0)
        #
        self.__a2.grid(row=0, column=2)
        self.__div2.grid(row=1, column=2)
        self.__b2.grid(row=2, column=2)
        #
        self.__op.grid(row=1, column=1, padx=10)
        self.__bt.grid(row=1, column=3, padx=10)
        self.__ip.grid(row=1, column=4)
        #
        self.__a3.grid(row=0, column=5)
        self.__div3.grid(row=1, column=5)
        self.__b3.grid(row=2, column=5)

    def __on_create(self) -> None:
        self.__a1.insert(0, '1')
        self.__b1.insert(0, '2')
        self.__a2.insert(0, '1')
        self.__b2.insert(0, '3')
        self.__op.insert(0, '+')
        self.__ip.insert(0, '0')
        self.__a3.insert(0, '5')
        self.__b3.insert(0, '6')

    @staticmethod
    def __on_click(event) -> None:
        print(event)
        messagebox.showinfo('Повідомлення', 'Тут буде результат')
        # ...

    def __binding(self) -> None:
        """ Привязка методів до подій на віджетах форм """
        self.__bt.bind('<Button-1>', self.__on_click)

    def run(self) -> None:
        """ Менеджер запуску """
        self.__config()
        self.__layout()
        self.__on_create()
        self.__bt.focus()
        self.__binding()
        self.__root.mainloop()
