from tkinter102 import MyGUI
from tkinter import *
from tkinter.messagebox import showinfo

class CustomGui(MyGUI):
	def reply(self):
		showinfo(title='popup', message='Ouch!')

if __name__=='__main__':
	CustomGui().pack()
	mainloop()