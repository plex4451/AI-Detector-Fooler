#Library
from tkinter import *


#Initialise
def open_window():
    """
    Dictionary:
    AIT = AI-Text
    AIFT = AI Fool Text
    AII = AI-Image
    AIFI = AI Fool Image
    """

    # Window
    Window = Tk()
    Window.geometry('900x900')
    Window.title('AI-NOOBS-UNLEASHED: AI FOOLER')
    Window.resizable(False, False)

    # Label
    LabelAIT = Label(Window, text='Insert AI generated text here:')
    LabelAIFT = Label(Window, text='Result of the AI generated text:')
    LabelAII = Label(Window, text='Upload a AI generated Image here:')
    LabelAIFI = Label(Window, text='Result of the AI generated Image:')

    LabelAIT.place(x=10, y=20, width=60, height=50)
    LabelAIFT.place(x=10, y=200, width=150, height=50)
    LabelAII.place(x=10, y= 300, width=150, height=50)
    LabelAIFI.place(x=10, y=400, width=150,height=50)

    # Entry
    Entry1 = Entry(Window)
    Entry2 = Entry(Window)
    Entry3 = Entry(Window)
    Entry1.place(x=20, y=55, width=60, height=25)
    Entry2.place(x=20, y=110, width=60, height=25)
    Entry3.place(x=90, y=110, width=60, height=25)

    #Textbox
    TextboxAIT = Text(Window)
    TextboxAIFT = Text(Window)

    TextboxAIT.place(x=400,y=400,width=300,height=300)
    TextboxAIFT.place(x=400,y=400,width=300,height=300)

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