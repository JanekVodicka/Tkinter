from tkinter import *
from tkinter import ttk

class Window_app:
	def __init__(self, master):
		self.master = master

		master.title('Tkinter_tabs')
		master.minsize(640, 400)

		# TabControl
		self.tabControl = ttk.Notebook(master)
		self.tab1 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1, text = 'Tab1')
		self.tab2 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2, text = 'Tab2')
		self.tabControl.pack(expand = 1, fill = "both")

		self.button1 = ttk.Button(self.tab1, text = "Button")
		self.button1.pack()

root = Tk()
my_app = Window_app(root)	# Object = Class(master)
root.mainloop()
