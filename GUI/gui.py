#Library
from tkinter import *
from Algo.text_algo import *
from tkinter import filedialog



#AI-Text-Methods
def convert_ai_text():
    txt = TextboxAIT.get("1.0", "end-1c")
    txt = change_text(txt)
    TextboxAIFT.delete("1.0","end")
    TextboxAIFT.insert("end", txt)

def upload_ai_text():
    file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),))
    file = open(file_path,"r",encoding="utf-8")
    text = file.read()
    file.close()
    TextboxAIT.delete("1.0", "end")
    TextboxAIT.insert("end", text)

def download_ai_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",   filetypes=[("Text files", "*.txt"),])
    if file_path:
        file = open(file_path,'w', encoding="utf-8")
        file.write(TextboxAIFT.get("1.0","end"))
        file.close()


#AI-Image-Methods
def convert_ai_image():
    pass

def upload_ai_image():
    pass

def download_ai_image():
    pass


#Objects-Selector-Methods
#Hides every non Text object and showes every Text object
def select_text_objects():
    Button_Image_Select.pack_forget()
    Button_Text_Select.pack_forget()
    Button_Exit_Menu.pack_forget()

    LabelAIT.pack()
    LabelAIFT.pack()
    TextboxAIT.pack()
    TextboxAIFT.pack()

    Button_Back_Menu.pack()
    Button_AIT_Convert.pack()
    Button_AIT_Download.pack()
    Button_AIT_Upload.pack()


#Hides every non Image object and showes every Image object
def select_image_objects():
    Button_AII_Upload.pack()
    Button_AII_Download.pack()
    Button_AII_Convert.pack()
    Button_Back_Menu.pack()

    LabelAII.pack()
    LabelAIFI.pack()
    Canvas_AII.pack()
    Canvas_AIT.pack()

    Button_Image_Select.pack_forget()
    Button_Text_Select.pack_forget()
    Button_Exit_Menu.pack_forget()


#Hides every non menu object and showes every Menu object
def select_menu_objects():
    # Hiding Buttons
    Button_AIT_Convert.pack_forget()
    Button_AIT_Download.pack_forget()
    Button_AIT_Upload.pack_forget()
    Button_AII_Upload.pack_forget()
    Button_AII_Download.pack_forget()
    Button_AII_Convert.pack_forget()


    Button_Back_Menu.pack_forget()

    Button_Image_Select.pack()
    Button_Text_Select.pack()
    Button_Exit_Menu.pack()

    # Hiding Labels
    LabelAIT.pack_forget()
    LabelAIFT.pack_forget()
    LabelAII.pack_forget()
    LabelAIFI.pack_forget()

    # Hiding Textboxes
    TextboxAIT.pack_forget()
    TextboxAIFT.pack_forget()

    Canvas_AII.pack_forget()
    Canvas_AIT.pack_forget()


#exit_object Method, exits the GUI with a exit code of 0
def exit_object():
    exit(0)



#Initialise
def open_window():
    #Gobal-Variables-Objects
    global Window
    global Button_AIT_Convert, Button_AIT_Download, Button_AIT_Upload
    global Button_AII_Upload, Button_AII_Download, Button_AII_Convert
    global Button_Image_Select, Button_Text_Select, Button_Back_Menu, Button_Exit_Menu
    global LabelAIT, LabelAIFT, LabelAII, LabelAIFI
    global TextboxAIT, TextboxAIFT
    global Canvas_AII,Canvas_AIT

    """
    Dictionary:
    AIT = AI-Text
    AIFT = AI Fool Text
    AII = AI-Image
    AIFI = AI Fool Image
    """

    # Window
    Window = Tk()
    Window.geometry('1200x900')
    Window.title('AI-NOOBS-UNLEASHED: AI FOOLER')
    Window.resizable(True, True)

    # Label
    #TODO : PLACE
    LabelAIT = Label(Window, text='Insert a AI generated text here:')
    LabelAIFT = Label(Window, text='Result of the AI generated text:')
    LabelAII = Label(Window, text='Upload a AI generated Image here:')
    LabelAIFI = Label(Window, text='Result of the AI generated Image:')

    LabelAIT.pack()
    LabelAIFT.pack()
    LabelAII.pack()
    LabelAIFI.pack()

    #LabelAIT.place(x=10, y=20, width=60, height=50)
    #LabelAIFT.place(x=10, y=200, width=150, height=50)
    #LabelAII.place(x=10, y= 300, width=150, height=50)
    #LabelAIFI.place(x=10, y=400, width=150,height=50)

    #Entry
    #NONE

    #Textbox
    # TODO: PLACE
    TextboxAIT = Text(Window)
    TextboxAIFT = Text(Window)

    TextboxAIT.pack()
    TextboxAIFT.pack()

    #TextboxAIT.place(x=200,y=400,width=300,height=300)
    #TextboxAIFT.place(x=600,y=400,width=300,height=300)

    #Canvas
    # TODO: PLACE CANAVAS
    Canvas_AII = Canvas(Window)
    Canvas_AIT = Canvas(Window)

    Canvas_AII.pack()
    Canvas_AIT.pack()




    # Buttons
    # TODO: PLACE BUTTONS

    #Text-Menu-Buttons
    Button_AIT_Convert = Button(Window, text='Change-Text', command=convert_ai_text)
    Button_AIT_Download = Button(Window, text='Download-Text', command=download_ai_text)
    Button_AIT_Upload = Button(Window, text='Upload-Text', command=upload_ai_text)

    Button_AIT_Convert.pack()
    Button_AIT_Download.pack()
    Button_AIT_Upload.pack()

    #Button_AIT_Convert.place(x=500, y=200, width=70, height=25)
    #Button_AIT_Download.place(x=600, y=200, width=80, height=25)
    #Button_AIT_Upload.place(x=600, y=200, width=80, height=25)


    #Image-Menu-Buttons
    Button_AII_Upload = Button(Window, text='Upload-Image', command=upload_ai_image)
    Button_AII_Download = Button(Window, text='Download-Image', command=download_ai_image)
    Button_AII_Convert = Button(Window, text='Change-Image', command=convert_ai_image)

    Button_AII_Upload.pack()
    Button_AII_Download.pack()
    Button_AII_Convert.pack()

    #Button_AII_Upload.place(x=400, y=200, width=80, height=25)
    #Button_AII_Convert.place(x=600, y=200, width=80, height=25)
    #Button_AII_Download.place(x=600, y=200, width=80, height=25)


    #Main-Menu-Buttons
    Button_Image_Select = Button(Window, text='Image Converter', command=select_image_objects)
    Button_Text_Select = Button(Window, text='Text Converter', command=select_text_objects)
    Button_Back_Menu = Button(Window, text='Back to Menu', command=select_menu_objects)
    Button_Exit_Menu = Button(Window, text='Exit', command=exit_object)

    Button_Image_Select.pack()
    Button_Text_Select.pack()
    Button_Back_Menu.pack()
    Button_Exit_Menu.pack()

    #Button_Image_Select.place(x=600, y=200, width=80, height=25)
    #Button_Text_Select.place(x=600,y=200, width=80, height=25)
    #Button_Back_Menu.place(x=450, y=500, width=80, height=25)
    #Button_Exit_Menu.place(x=600, y=200, width=80, height=25)




    #Window Mainloop

    select_menu_objects()
    Window.mainloop()