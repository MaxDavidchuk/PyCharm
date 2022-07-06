# -------------------------------------------------------------------------------
# Name:        alarm_clock
# Purpose:     Створення програми Годиннника із графічним інтерфейсом
# Author:      dp_maxim
# Created:     20.06.2022
# -------------------------------------------------------------------------------
from time import strftime
from tkinter import *
from tkinter import messagebox
from os import system


root = Tk()  # Клас вікна Tool Kit
clock = Label(root)
alarm = Entry(root)
start = Button(root)
stop = Button(root)

limit = ''


def config():
  root.title('Годинник-будильник')
  root.geometry('300x220+200+200')
  root.config(bg='black')
  #
  clock.config(text='00:00:00', fg='lime', bg='black', font='Arial 45')
  clock.pack(pady=5)
  #
  alarm.config(fg='red', width=15, justify='center', font='Arial 18')
  alarm.pack(pady=5)
  #
  start.config(text='Включити будильник', width=20, font='Arial 9')
  stop.config(text='Виключити будильник', width=20, font='Arial 9')
  start.pack(pady=10)
  stop.pack(pady=0)


def tick():
  current_time = strftime('%H:%M:%S')
  clock.config(text=current_time)
  if current_time == limit:
    #messagebox.showwarning('Попередження', 'Час настав!!!')
    system('music.mp3')
  clock.after(1000, tick)


def start_click(event):
  global limit
  print(event)
  limit = alarm.get()
  messagebox.showinfo('Повідомлення', f'Будильник встановлено на {limit}')


def run():
  start.bind('<Button-1>', start_click)
  root.mainloop()


def main():
  config()
  tick()
  run()


if __name__ == '__main__':
  main()
