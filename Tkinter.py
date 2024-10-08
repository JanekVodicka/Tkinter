from tkinter import *                # Vytvari okna
from tkinter.ttk import Combobox     # Aplikace - combobox

WIDTH = 800
HEIGHT = 500
geometry = str(WIDTH) + 'x' + str(HEIGHT)

def click_safe():
	save_text = textentry.get()
	print(save_text)

def show_int_var():
	Variable_Int_from_Check = var1.get()
	print(Variable_Int_from_Check)

def show_str_var():
	Variable_Str_from_Chack = var2.get()
	print(Variable_Str_from_Chack)

# ----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Tkinter")                   # Popisek hlavního okna
root.geometry(geometry)                 # Rozmery hlavního okna
root.resizeable(True, True)
root.option_add('*Font', 'Arial 10')    # Font v hlavním oknu

# Widgety
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Background image - obecně
image = Image.open("prospon_logo.png")
#background_image = ImageTk.PhotoImage(image)
#background_label = Label(root, image = background_image)
#background_label.place(relwidth=1, relheight=1)

# POPISEK UVNITŘ OKNA
# Vytvořit popisek
label1 = Label(root, text='Zkouška 1', bg='#b3d9ff', fg='white', font='Times 12 bold italic', width=20)
label2 = Label(root, text='Zkouška 2', bd=1, relief="solid", width=10) # bd - tloustka ramecku
# Zasadit popisek do okna
# pack()  - => Tvori list pod sebe
# grid()  - => Mrizka
# place() - => Umístění
label1.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)
label2.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.1)

# ENTRY
textentry = Entry(root, bg='white')
textentry.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.1)

# TLAČÍTKO
button1 = Button(root, text="Safe text", command = click_safe)      # command - uloží zapsaný text
button2 = Button(root, text="Close button", command = root.destroy) # command - uzavře okno
button3 = Button(root, text="Show Int Value", command = show_int_var)
button4 = Button(root, text="Show String Value", command = show_str_var)
button1.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.1)
button2.place(relx = 0.1, rely = 0.5, relwidth = 0.8, relheight = 0.1)
button3.place(relx = 0.5, rely = 0.6, relwidth = 0.4, relheight = 0.1)
button4.place(relx = 0.5, rely = 0.7, relwidth = 0.4, relheight = 0.1)

# CHECKBUTTONS
var1 = IntVar()      # Integer Variable
var2 = StringVar()   # String Variable
var1.set(0)
var2.set(0)
Ch1 = Checkbutton(root, text ='Zaškrtávací políčko 1', variable=var1)
Ch2 = Checkbutton(root, text ='Zaškrtávací políčko 2', variable=var2, onvalue='Dobrý', offvalue="Špatný")
Ch1.place(relx = 0.1, rely = 0.6, relwidth = 0.4, relheight = 0.1)
Ch2.place(relx = 0.1, rely = 0.7, relwidth = 0.4, relheight = 0.1)

# COMBOBOX
var_combobox = StringVar()
combobox = Combobox(root, values = [1, 2, 3], textvariable = var_combobox)
combobox.place(relx = 0.1, rely = 0.8, relwidth = 0.8, relheight = 0.1)
combobox.current(0)

# Scrollbar
"""scroll = Scrollbar(frame)
scroll.pack(side = RIGHT, fill = Y)
listbox = Listbox(frame, yscrollcommand = scroll.set)
for i in range(0, len(CSN)):
	listbox.insert(END, CSN[i])
listbox.pack(side = LEFT)
scroll.config(command = listbox.yview)"""


# Otevřít okno
root.mainloop()   # Otevre okno
