def disable_event():
	messagebox.showinfo(msg_title, 'Щоб завершити роботу натисніть кнопку "ВИХІД".')


def load_data() -> dict:
	with open('data.json', 'r', encoding='utf-8') as read_file:
		return json.load(read_file)


def save_data():
	with open('data.json', 'w', encoding='utf-8') as write_file:
		json.dump(data, write_file, indent=4, ensure_ascii=False)
		messagebox.showinfo('Повідомлення', 'Дані успішно збережені.')


def clear_entry():
	name_entry.delete(0, END)
	phone_entry.delete(0, END)
	group_combo.set('')


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
		tmp_name = name_entry.get()
		tmp_phone = phone_entry.get()
		if check_data('name', tmp_name):
			tmp_str = f"Контакт з ім'ям {tmp_name} вже існує"
		elif check_data('phone', tmp_phone):
			tmp_str = f"Контакт з телефоном {tmp_phone} вже існує"
		else:
			if messagebox.askquestion(msg_title, 'Додати новий контакт?') == 'yes':
				data.get('book').append({"name": tmp_name, "phone": tmp_phone, "group": group_combo.get()})
				save_data()
				clear_entry()
				lbox.delete(0, END)
				fill_listbox(fio)
				return
	messagebox.showinfo(msg_title, tmp_str)
