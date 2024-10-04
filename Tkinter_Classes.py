""" TKINTER CLASS """
from tkinter import *                 # Vytvari okna
from PIL import Image, ImageTk

# FORMA
# class Window_app:
# 	def __init__(self, master):
# 		self.master = master
#       frame = Frame(master)
#       frame.pack()

# root = Tk()
# my_app = Window_app(root)
# root.mainloop()


WIDTH = 800
HEIGHT = 500
geometry = str(WIDTH) + 'x' + str(HEIGHT)

class Window_app:
	def __init__(self, master):                                             # Vždy
		self.master = master
		""" master = root """

		master.title("Tkinter_Class")                                       # Pojmenování okna
		master.geometry(geometry)                                           # Rozmery hlavního okna
		master.configure(background = '#b3d9ff')                            # Upraví pozadí okna
		master.option_add('*Font', 'Arial 10')                              # Font v hlavním oknu
		master.minsize(WIDTH, HEIGHT)                                       # Minimální velikost
		master.maxsize(WIDTH, HEIGHT)                                       # Maximální velikost

		# CANVAS
		self.canvas = Canvas(master, height=HEIGHT, width=WIDTH)
		self.canvas.pack()

		# BACKGROUND IMAGE - obecně
		self.image = Image.open("prospon_logo.png")
		self.background_image = ImageTk.PhotoImage(self.image)
		self.background_label = Label(master, image=self.background_image)
		self.background_label.place(relwidth=1, relheight=1)

		# POPISEK UVNITŘ OKNA
		self.label1 = Label(master, text='Zkouška 1', bg='#b3d9ff', fg='white', font='Times 12 bold italic', width=20)
		self.label2 = Label(master, text='Zkouška 2', bd=1, relief="solid", width=10)  # bd - tloustka ramecku
		self.label1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
		self.label2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

		# TLAČÍTKO
		self.button1 = Button(master, text="Safe text")  # command - uloží zapsaný text
		self.button2 = Button(master, text="Close button", command=master.destroy)  # command - uzavře okno
		self.button1.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)
		self.button2.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)

root = Tk()
App = Window_app(root)  # Object = Class(master)
root.mainloop()
