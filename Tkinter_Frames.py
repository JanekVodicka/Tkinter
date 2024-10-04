from tkinter import *                # Vytvari okna

root = Tk()

frame1 = LabelFrame(root, text = 'Frame 1', bg = '#99ffd6')
frame1.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.5)
frame2 = LabelFrame(root, text = 'Frame 2', bg = '#ffffb3')
frame2.place(relx = 0.05, rely = 0.55, relwidth = 0.4, relheight = 0.4)

frame3 = Frame(root, bg = '#b3d9ff')
frame3.place(relx = 0.45, rely = 0.05, relwidth = 0.5, relheight = 0.9)

button1 = Button(frame1, text = 'Buttton1').place(rely = 0   , relwidth = 1)
button2 = Button(frame1, text = 'Buttton2').place(rely = 0.25, relwidth = 1)
button3 = Button(frame1, text = 'Buttton3').place(rely = 0.5 , relwidth = 1)
button4 = Button(frame1, text = 'Buttton4').place(rely = 0.75, relwidth = 1)

root.mainloop()
