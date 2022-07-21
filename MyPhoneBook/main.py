from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

bg1 = '#f7ef38'
fg1 = '#0000ff'
msg_title = 'Телефона книжка'

if __name__ == '__main__':
	def disable_event():
		messagebox.showinfo(msg_title, 'Щоб завершити роботу натисніть кнопку "ВИХІД".')


	def save_data():
		with open('data.json', 'w', encoding='utf-8') as write_file:
			json.dump(data, write_file, indent=4, ensure_ascii=False)
			messagebox.showinfo('Повідомлення', 'Дані успішно збережені.')


	def clear_entry():
		name_entry.delete(0, END)
		phone_entry.delete(0, END)
		group_combo.set('')
		return


	def search_clear():
		search.delete(0, END)
		cb_search('<KeyRelease>')
		search.focus()


	def check_entry() -> list:
		if name_entry.get() == '':
			return ["Ім'я", name_entry]
		elif phone_entry.get() == '':
			return ['Телефон', phone_entry]
		elif group_combo.get() == '':
			return ['Група', group_combo]
		else:
			return []

	def check_data(elem: str, wtf: str) -> bool:
		base = [name.get(elem) for name in data.get('book')]
		return True if wtf in base else False

	def contact_add():
		case = check_entry()
		if len(case) > 0:
			messagebox.showerror('Увага!', 'Не заповнено поле "{}"'.format(case[0]))
			case[1].focus()
			return
		else:
			if check_data('name', name_entry.get()):
				tmp_str = f"Контакт з ім'ям {name_entry.get()} вже існує"
			elif check_data('phone', phone_entry.get()):
				tmp_str = f"Контакт з телефоном {phone_entry.get()} вже існує"
			else:
				if messagebox.askquestion(msg_title, 'Додати новий контакт?') == 'yes':
					data.get('book').append({"name": "2", "phone": "2", "group": "2"})
					save_data()
					return
		messagebox.showinfo(msg_title, tmp_str)


	def item_selected(event):
		# messagebox.showinfo('Повідоммлення', 'Ви вибрали: ' + ','.join([lbox.get(i) for i in lbox.curselection()]))
		tmp = ','.join([lbox.get(i) for i in lbox.curselection()])
		for contact in data.get('book'):
			if contact.get('name') == tmp:
				clear_entry()
				name_entry.insert(0, tmp)
				phone_entry.insert(0, contact.get('phone'))
				group_combo.set(contact.get('group'))
		return


	def fill_listbox(self, temp: list):
		for item_name in temp:
			self.insert(END, item_name)
		count_label.config(text='Всього контактів: ' + str(len(temp)))


	def cb_search(event):
		s_str = search_str.get()
		lbox.delete(0, END)
		if s_str == '':  # If filter removed show all data
			fill_listbox(lbox, fio)
			return
		elif len(s_str) == 1:
			s_str = s_str.upper()
			search.delete(0, END)
			search.insert(0, s_str)
		filtered_data = list()
		for item in fio:
			if item.find(s_str) >= 0:
				filtered_data.append(item)
		fill_listbox(lbox, filtered_data)


	# Create window
	root = Tk()
	root.config(bg=bg1)
	root.title('Моя телефона книжка')
	root.resizable(False, False)
	pos_r = int(root.winfo_screenwidth()/2 - root.winfo_reqwidth()/2) - 150
	pos_d = int(root.winfo_screenheight()/2 - root.winfo_reqheight()/2) - 150
	root.geometry('+{}+{}'.format(pos_r, pos_d))

	# Create frames
	f_head = Frame(root, highlightbackground="#007dff", highlightcolor="#007dff", highlightthickness=2, bd=0, bg=bg1)
	f_head.pack(padx=10, pady=10, anchor=W)
	f_body = Frame(root, bd=0, bg=bg1)
	f_body.pack(padx=10, pady=10, anchor=W)
	f_footer = Frame(root, bd=0, bg=bg1)
	f_footer.pack(pady=20, anchor=S)

	img = PhotoImage(file='pb_logo.png')
	logo = Label(f_head, image=img, bg=bg1)
	logo.pack(side=LEFT, padx=3, pady=3)
	logo_name = Label(f_head, text='Моя телефона книжка', font=('Century Gothic', 24, 'bold'), fg=fg1, bg=bg1)
	logo_name.pack(padx=10, pady=3, side=LEFT)

	lf_left = LabelFrame(f_body, text='Ваш вибір', bg=bg1)
	lf_left.pack(side=LEFT, anchor=N)
	# add_img = PhotoImage(file='add.png').subsample(4, 4)
	add_butt = Button(lf_left, text='Додати контакт', command=contact_add, font='Arial 10', width=20)
	add_butt.pack(fill=X, padx=5, pady=10)
	# del_img = PhotoImage(file='del.png').subsample(4, 4)
	del_butt = Button(lf_left, text='Видалити контакт', command='', font='Arial 10', width=20, state=DISABLED)
	del_butt.pack(fill=X, padx=5)
	# upd_img = PhotoImage(file='upd.png').subsample(4, 4)
	upd_butt = Button(lf_left, text='Змінити контакт', command='', font='Arial 10', width=20, state=DISABLED)
	upd_butt.pack(fill=X, padx=5, pady=10)

	# ListBox
	with open('data.json', 'r', encoding='utf-8') as read_file:
		data = json.load(read_file)
		fio = [name.get('name') for name in data.get('book')]
		fio.sort()
		group = data.get('member')

	search_block = Frame(f_body, bg=bg1)
	search_block.pack(anchor=W, padx=10, pady=5)
	Label(search_block, text='Пошук -> ', bg=bg1, font='Arial 10').pack(side=LEFT)
	search_str = StringVar()
	search = Entry(search_block, textvariable=search_str, width=10)
	search.pack(side=LEFT, ipadx=1, ipady=1)
	Button(search_block, command=search_clear, text='X', width=2).pack(side=LEFT, padx=3)

	f_lbox = Frame(f_body, bg=bg1)
	f_lbox.pack(padx=10)
	lbox = Listbox(f_lbox, width=30, height=6, font='Consolas 11')
	lbox.pack(side=LEFT, fill=BOTH)
	scroll = Scrollbar(f_lbox, orient=VERTICAL, command=lbox.yview)
	scroll.pack(side=RIGHT, fill=Y)
	lbox.configure(yscrollcommand=scroll.set)
	scroll.config()
	count_label = Label(f_body, font='Arial 11 bold', bg=bg1, fg=fg1)
	count_label.pack(padx=10, anchor=W)
	fill_listbox(lbox, fio)

	# FOOTER block
	top_block = Frame(f_footer)
	top_block.pack(anchor=W)
	Label(top_block, width=23, text='Ім\'я:', font='Arial 10 bold', relief=RAISED, bg='#BDD7EE').pack(side=LEFT)
	Label(top_block, width=17, text='Телефон:', font='Arial 10 bold', relief=RAISED, bg='#BDD7EE').pack(side=LEFT)
	Label(top_block, width=15, text='Група:', font='Arial 10 bold', relief=RAISED, bg='#BDD7EE').pack()
	bottom_block = Frame(f_footer, bg=bg1)
	bottom_block.pack(anchor=W)
	var_name = StringVar()
	name_entry = ttk.Entry(bottom_block, textvariable=var_name, width=23, font='Consolas 11')
	name_entry.pack(side=LEFT)
	var_phone = StringVar()
	phone_entry = ttk.Entry(bottom_block, textvariable=var_phone, width=17, font='Consolas 11')
	phone_entry.pack(side=LEFT)
	group_combo = ttk.Combobox(bottom_block, width=13, font='Consolas 11', values=group)
	group_combo.pack()
	# QUIT block
	quit_img = PhotoImage(file='quit.png').subsample(2, 2)
	Button(root, text='   Вихід   ', command=root.quit, font='Arial 11', image=quit_img, compound=LEFT).pack(pady=10)
	# Block RUN
	lbox.bind('<<ListboxSelect>>', item_selected)
	search.bind('<KeyRelease>', cb_search)
	search.focus()

	root.protocol("WM_DELETE_WINDOW", disable_event)
	root.mainloop()
