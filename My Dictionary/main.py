from tkinter import Tk, Frame, PhotoImage, Label, Entry, Button, END
from tkinter import messagebox
import json


bg1 = '#696969'
tittle = 'Повідомлення'

if __name__ == '__main__':
	# Create window
	root = Tk()
	root.config(bg=bg1)
	root.title('Українсько-англійський словник')
	root.resizable(False, False)

	# Create main frame
	frame = Frame(root, bg=bg1)
	frame.pack(padx=25, pady=25)
	img = PhotoImage(file='logo.png')
	# img = img.subsample(2, 2)

	# create logo
	logo = Label(frame, image=img, bg=bg1)
	logo.pack(side='left')
	label1 = Label(frame, text='Введіть текст для перекладу: ', font='Calibri 14', bg=bg1, fg='white')
	label1.pack(padx=20, pady=5)

	# create Enter
	word = Entry(frame, width=24, font='Consolas 14', fg='red', justify='center')
	word.pack(pady=3)
	trans = Entry(frame, width=24, font='Consolas 14', fg='blue', justify='center')
	trans.pack(pady=3)

	# create Button in new Frame
	control = Frame(frame, bg=bg1)
	control.pack(pady=15)
	trans_butt = Button(control, text='Перекласти', font='Arial 10', width=20)
	trans_butt.pack(pady=5)
	add_butt = Button(control, text='Додати переклад', font='Arial 10', width=20)
	add_butt.pack(pady=0)
	del_butt = Button(control, text='Видалити переклад', font='Arial 10', width=20)
	del_butt.pack(pady=5)
	upd_butt = Button(control, text='Змінити переклад', font='Arial 10', width=20)
	upd_butt.pack(pady=0)

	""" Логіка управління програмою """
	with open('data.json', 'r', encoding='utf-8') as read_file:
		data = json.load(read_file)


	def save_data():
		with open('data.json', 'w', encoding='utf-8') as write_file:
			json.dump(data, write_file, indent=4, ensure_ascii=False)
			messagebox.showinfo(tittle, 'Дані успішно збережені.')


	def trans_butt_handler(event):
		print(f'Event -> TranslateButton-Click: {event}')
		input_word = word.get()
		if input_word == '':
			messagebox.showwarning(tittle, 'Відсутнє слово для перекладу')
			word.focus()
		else:
			output_trans = data.get(input_word)
			if output_trans is None:
				messagebox.showinfo(tittle, 'Дане слово відсутнє у словнику')
			else:
				trans.delete(0, END)
				trans.insert(0, output_trans)


	def add_butt_handler(event):
		print(f'Event -> AddTranslateButton_click: {event}')
		input_word = word.get()
		if input_word == '':
			messagebox.showwarning(tittle, 'Відсутнє слово для перекладу')
			word.focus()
		elif input_word in data:
			messagebox.showwarning(tittle, 'Введене слово вже є у словнику')
		else:
			output_trans = trans.get()
			if output_trans == '':
				messagebox.showwarning(tittle, 'Відсутній переклад даного слова')
				trans.focus()
			else:
				data[input_word] = output_trans
				save_data()


	def del_butt_handler(event):
		print(f'Event -> DeleteTranslateButton_click: {event}')
		input_word = word.get()
		if input_word in data:
			del data[input_word]
			save_data()
			messagebox.showinfo(tittle, 'Слово успішно видалено із словника.')
		else:
			messagebox.showwarning(tittle, 'Даного слова немає у словнику.')


	def upd_butt_handler(event):
		print(f'Event -> UpdateTranslateButton_click: {event}')
		input_word = word.get()
		if input_word not in data:
			messagebox.showwarning(tittle, 'Даного слова немає у словнику.')
		else:
			output_trans = trans.get()
			if output_trans == '':
				messagebox.showwarning(tittle, 'Відсутній переклад даного слова')
			elif output_trans == data.get(input_word):
				messagebox.showwarning(tittle, 'Переклад даного слова не був змінений')
			else:
				data[input_word] = output_trans
				save_data()
				messagebox.showinfo(tittle, 'Переклад успішно оновлений.')


	# Block RUN has to be the last
	trans_butt.bind('<Button-1>', trans_butt_handler)
	add_butt.bind('<Button-1>', add_butt_handler)
	del_butt.bind('<Button-1>', del_butt_handler)
	upd_butt.bind('<Button-1>', upd_butt_handler)
	root.mainloop()
