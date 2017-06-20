from tkinter import *
import shelve
from tkinter.messagebox import showerror

shelvename = 'class-shelve'
fieldsname1 = ('name','age','pay','job')
fieldsname = ('1','2','3','4')


def makeWidgets(db, fieldsname):
	global entries
	window = Tk()
	window.title('People shelve')
	form = Frame(window)
	form.pack()
	entries = {}

	for (ix,label) in enumerate(('key',) + fieldsname):
		lab = Label(form, text=label)
		ent = Entry(form)
		lab.grid(row=ix, column=0)
		ent.grid(row=ix, column=1)
		entries[label] = ent
	Button(window, text='Fetch', command=(lambda: fetchRecord(fieldsname))).pack(side=LEFT)
	Button(window, text='Update', command=(lambda: updateRecord(fieldsname))).pack(side=LEFT)
	Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
	return window

def fetchRecord(fieldsname):
	key = entries['key'].get()
	try:
		record = db[key]
	except:
		showerror(title='Error', message='No such key!')
	else:
		for field in fieldsname:
			entries[field].delete(0, END)
			entries[field].insert(0, repr(getattr(record, field)))

def updateRecord(fieldsname):
	key = entries['key'].get()
	if key in db:
		record = db[key]
	else:
		from person import Person
		record = Person(name = '?', age = '?')
	for field in fieldsname:
		setattr(record, field, eval(entries[field].get()))
	db[key] = record

db = shelve.open(shelvename)
window = makeWidgets(db, fieldsname)
window.mainloop()
db.close()