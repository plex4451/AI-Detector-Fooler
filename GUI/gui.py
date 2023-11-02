#Library
from tkinter import *


#Initialise
def open_window():
    # Window
    Window = Tk()
    Window.geometry('900x900')
    Window.title('AI-NOOBS-UNLEASHED: AI FOOLER')
    Window.resizable(False, False)

    # Label
    LabelW = Label(Window, text='Wort:')
    LabelWV = Label(Window, text='Wort Verschlüsselt:')
    LabelWVD = Label(Window, text='N/A')
    LabelK = Label(Window, text='Key:')
    LabelKW = Label(Window, text='Word Key:')

    LabelW.place(x=10, y=20, width=60, height=50)
    LabelWV.place(x=10, y=200, width=150, height=50)
    LabelWVD.place(x=10, y=240, width=150, height=25)
    LabelK.place(x=10, y=70, width=60, height=50)
    LabelKW.place(x=85, y=70, width=80, height=50)

    # Entry
    Entry1 = Entry(Window)
    Entry2 = Entry(Window)
    Entry3 = Entry(Window)
    Entry1.place(x=20, y=55, width=60, height=25)
    Entry2.place(x=20, y=110, width=60, height=25)
    Entry3.place(x=90, y=110, width=60, height=25)

    # Listbox
    Listbox1 = Listbox(Window)
    Listbox1.place(x=170, y=50, width=100, height=200)

    # Scrollbar
    Scrollbar1 = Scrollbar(Window)
    Scrollbar1.place(x=270, y=50, width=15, height=200)

    # Config
    Listbox1.config(yscrollcommand=Scrollbar1.set)
    Scrollbar1.config(command=Listbox1.yview)

    # Button
    Button1 = Button(Window, text='Codieren')
    Button1.place(x=20, y=150, width=70, height=25)

    Button2 = Button(Window, text='Decodieren')
    Button2.place(x=20, y=180, width=80, height=25)

    Button3 = Button(Window, text='Codieren W')
    Button3.place(x=90, y=150, width=80, height=25)
    Window.mainloop()