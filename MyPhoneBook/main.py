"""
	Завдання 1 пвсля Уроку 11
	-----------------------------------------------------------------------
	Розробіть додаток із графічним інтерфейсом для управління записником
	із номерами телефонів певних контактів. Слід використати tkinter, json
	та роботу із словниками.
	-----------------------------------------------------------------------
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

bg1 = '#f7ef38'
bg2 = '#BDD7EE'
fg1 = '#0000ff'
msg_title = 'Телефона книжка'


if __name__ == '__main__':
	data = dict()
	fio = list()
	group = list()

	def disable_event():
		""" Відключення дії кнопки Закрити вікно """
		show_msg('Щоб завершити роботу натисніть кнопку "ВИХІД"', False)


	def refresh_data():
		""" Оновлення словаря та списків """
		global data, fio, group
		with open('data.json', 'r', encoding='utf-8') as read_file:
			data = json.load(read_file)
			fio = [name.get('name') for name in data.get('book')]
			group = data.get('member')


	def save_data():
		""" Функція збереження даних """
		with open('data.json', 'w', encoding='utf-8') as write_file:
			json.dump(data, write_file, indent=4, ensure_ascii=False)
			show_msg('Дані успішно збережені!')


	def show_msg(err_str: str, t=True):
		""" Фунція сповіщення про дії користувача """
		error.config(text='')
		error.config(text=err_str)
		foo_block.config(highlightbackground='green' if t else 'red')


	def clear_entry():
		""" Очитска полей вводу даних """
		name_entry.delete(0, END)
		phone_entry.delete(0, END)
		group_combo.set('')


	def search_clear():
		""" Очитска полня Пошуку """
		search.delete(0, END)
		cb_search('<KeyRelease>')
		search.focus()


	def check_entry(yes=True) -> bool:
		""" Перевірка, чи заповнені необхідні поля """
		if not name_entry.get():
			choice = ["Ім'я", name_entry]
		elif not phone_entry.get():
			choice = ['Телефон', phone_entry]
		elif not group_combo.get() and yes:
			choice = ['Група', group_combo]
		else:
			choice = []
		if choice:
			show_msg('Увага! Не заповнено поле "{}"'.format(choice[0]), False)
			choice[1].focus()
			return False
		else:
			return True


	def check_data(elem: str, wtf: str, act: str) -> bool:
		""" Перевірка, чи існують дані у записній книжці """
		if wtf in [name.get(elem) for name in data.get('book')]:
			return True if act == 'add' else False
		else:
			return False if act == 'add' else True


	def button_clicked(t: str):
		""" Функція виконання дій при настиукані відповідних кнопок """
		action = {'add': 'Додати новий контакт?', 'del': 'Видалити обраний контакт?', 'upd': 'Оновити дані контакту?'}
		sel_str = 'вже' if t == 'add' else 'не'
		if check_entry(True if t == 'add' else False):
			tmp_name = name_entry.get()
			tmp_phone = phone_entry.get()
			if check_data('name', tmp_name, t):
				tmp_str = f"Контакт з ім'ям '{tmp_name}' {sel_str} існує"
			elif check_data('phone', tmp_phone, t):
				tmp_str = f"Контакт з телефоном '{tmp_phone}' {sel_str} існує"
			else:
				if messagebox.askquestion(msg_title, action.get(t)) == 'yes':
					new = {"name": tmp_name, "phone": tmp_phone, "group": group_combo.get()}
					if t == 'add':
						data.get('book').append(new)
					else:
						index = -1
						for book in data.get('book'):    # Пошук індекса
							index += 1
							if book.get('phone') == tmp_phone:
								break
						if index > -1:
							if t == 'del':
								data.get('book').pop(index)
							else:
								data.get('book')[index].update(new)
					save_data()
					clear_entry()
					refresh_data()
					fill_listbox(fio)
				else:
					show_msg('')
				return
			show_msg(tmp_str, False)
			lbox.selection_clear(0, END)


	def item_selected(event):
		""" Заполвнення даних вибраним із списку ім'ям"""
		show_msg('')
		tmp = ','.join([lbox.get(i) for i in lbox.curselection()])
		# tmp = lbox.get(ANCHOR)
		for contact in data.get('book'):
			if contact.get('name') == tmp:
				clear_entry()
				name_entry.insert(0, tmp)
				phone_entry.insert(0, contact.get('phone'))
				group_combo.set(contact.get('group'))


	def fill_listbox(temp):
		""" Заопвнення/оновлення списку """
		temp.sort()
		lbox.delete(0, END)
		for item_name in temp:
			lbox.insert(END, item_name)
		count_label.config(text='Всього контактів: ' + str(len(temp)))


	def cb_search(event):
		""" Функція пошуку контакту у вікні Пошук """
		s_str = search_str.get()
		lbox.delete(0, END)
		if s_str == '':
			fill_listbox(fio)
			return
		s_str = s_str[0].upper() + s_str[1:]
		search.delete(0, END)
		search.insert(0, s_str)
		filtered_data = list()
		for item in fio:
			if item.find(s_str) >= 0:
				filtered_data.append(item)
		fill_listbox(filtered_data)


	# Create window
	root = Tk()
	root.config(bg=bg1)
	root.title('Моя телефона книжка')
	root.resizable(False, False)
	pos_r = int(root.winfo_screenwidth()/2 - root.winfo_reqwidth()/2) - 150
	pos_d = int(root.winfo_screenheight()/2 - root.winfo_reqheight()/2) - 150
	root.geometry('+{}+{}'.format(pos_r, pos_d))

	# HEAD
	f_head = Frame(root, highlightbackground="#007dff", highlightcolor="#007dff", highlightthickness=2, bd=0, bg=bg1)
	img = PhotoImage(file='pb_logo.png')
	logo = Label(f_head, image=img, bg=bg1)
	logo.pack(side=LEFT, padx=3, pady=3)
	logo_name = Label(f_head, text='Моя телефона книжка', font=('Century Gothic', 24, 'bold'), fg=fg1, bg=bg1)
	logo_name.pack(padx=10, pady=3, side=LEFT)
	f_head.pack(padx=10, pady=10, side=TOP, fill=X)

	# BODY
	f_body = Frame(root, bg=bg1)
	left_body = Frame(f_body, bg=bg1)
	Label(left_body, text='Управління контактами: ', font='Arial 10', bg=bg1).pack(anchor=W, padx=5, pady=5)
	add_butt = Button(left_body, text='Додати контакт', width=20, command=lambda m='add': button_clicked(m))
	add_butt.pack(fill=X, padx=5, pady=10)
	del_butt = Button(left_body, text='Видалити контакт', width=20, command=lambda m='del': button_clicked(m))
	del_butt.pack(fill=X, padx=5)
	upd_butt = Button(left_body, text='Оновити контакт', width=20, command=lambda m='upd': button_clicked(m))
	upd_butt.pack(fill=X, padx=5, pady=10)
	left_body.pack(side=LEFT, anchor=N)

	refresh_data()
	right_body = Frame(f_body, bg=bg1)
	top_body = Frame(right_body, bg=bg1)
	Label(top_body, text='Пошук -> ', bg=bg1, font='Arial 10').pack(side=LEFT)
	search_str = StringVar()
	search = ttk.Entry(top_body, textvariable=search_str, width=20)
	search.pack(ipadx=5, ipady=2, side=LEFT)
	Button(top_body, command=search_clear, text='X', width=2).pack(padx=3)
	top_body.pack(padx=10, pady=5, side=TOP)

	bottom_body = Frame(right_body, bg='white', bd=1, relief=SUNKEN)
	lbox = Listbox(bottom_body, width=25, height=6, font='Consolas 11', bd=0, highlightthickness=0)
	scroll = ttk.Scrollbar(bottom_body, orient=VERTICAL, command=lbox.yview)
	lbox['yscrollcommand'] = scroll.set
	scroll.pack(side=RIGHT, fill=Y)
	lbox.pack(side=TOP, fill=BOTH, expand=True, pady=5, padx=5)
	bottom_body.pack(padx=10, anchor=W)
	count_label = Label(right_body, font='Arial 11 bold', bg=bg1, fg=fg1)
	count_label.pack(side=BOTTOM, padx=10, anchor=W)
	right_body.pack(side=RIGHT)
	f_body.pack(padx=10, fill=X)

	# FOOTER
	fill_listbox(fio)
	f_footer = Frame(root, bd=0, bg=bg1)
	top_block = Frame(f_footer)
	Label(top_block, width=20, text='Ім\'я:', font='Arial 10 bold', relief=RAISED, bg=bg2).pack(side=LEFT)
	Label(top_block, width=20, text='Телефон:', font='Arial 10 bold', relief=RAISED, bg=bg2).pack(side=LEFT)
	Label(top_block, width=10, text='Група:', font='Arial 10 bold', relief=RAISED, bg=bg2).pack(fill=X)
	top_block.pack(fill=X)

	bottom_block = Frame(f_footer)
	var_name = StringVar()
	name_entry = ttk.Entry(bottom_block, textvariable=var_name, width=20, font='Consolas 11')
	name_entry.pack(side=LEFT)
	var_phone = StringVar()
	phone_entry = ttk.Entry(bottom_block, textvariable=var_phone, width=20, font='Consolas 11')
	phone_entry.pack(side=LEFT)
	group_combo = ttk.Combobox(bottom_block, width=10, font='Consolas 11', values=group)
	group_combo.pack(fill=X)
	bottom_block.pack(fill=X)

	foo_block = Frame(f_footer, highlightthickness=1, bg='white')
	error = Label(foo_block, text='', bg='white', anchor=W)
	error.pack(pady=5, padx=5, side=TOP, fill=X)
	foo_block.pack(pady=10, fill=X)

	quit_img = PhotoImage(file='quit.png').subsample(2, 2)
	Button(f_footer, text='   Вихід   ', command=root.quit, font='Arial 11', image=quit_img, compound=LEFT).pack(pady=10)
	f_footer.pack(padx=10, pady=10, fill=X)

	# Block RUN
	lbox.bind('<<ListboxSelect>>', item_selected)
	search.bind('<KeyRelease>', cb_search)
	search.focus()

	root.protocol("WM_DELETE_WINDOW", disable_event)
	root.mainloop()
