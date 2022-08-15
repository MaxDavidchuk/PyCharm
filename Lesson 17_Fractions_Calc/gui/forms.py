from tkinter import Tk, Frame


class MainForm(object):

    def __init__(self):
        self.__root = Tk()
        self.__frame = Frame(self.__root)

    def __config(self) -> None:
        """ Налаштовує властивості віджетів"""
        self.__root.title('Кадькулятор дробів')

    def __layout(self) -> None:
        """ Менеджер розміщення """
        self.__frame.pack(padx=20, pady=20)

    def run(self) -> None:
        """ Менеджер запуску """
        self.__config()
        self.__layout()
        self.__root.mainloop()
