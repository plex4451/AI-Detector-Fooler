#Library
from tkinter import *
from Algo.text_algo import *
from Algo.imagealgo import * 
from tkinter import filedialog
from PIL import Image,ImageTk


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
    file_path = filedialog.askopenfilename(filetypes=(("PNG files", "*.png"),("JPG files","*.jpg")))
    if file_path::
        image = Image.open(path)
        tk_image = ImageTk.PhotoImage(image)
        Label_AII_Image.config(image=tk_image)
        Label_AII_Image.image = tk_image
    


def download_ai_image():
    pass






#Objects-Selector-Methods
#Hides every non Text object and showes every Text object
def select_text_objects():
    Frame_Text.pack()
    Frame_Main_Menu.pack_forget()


#Hides every non Image object and showes every Image object
def select_image_objects():
    Frame_Image.pack()
    Frame_Main_Menu.pack_forget()


#Hides every non menu object and showes every Menu object
def select_menu_objects():
    # Hiding Buttons
    Frame_Image.pack_forget()
    Frame_Text.pack_forget()
    Frame_Main_Menu.pack()

#exit_object Method, exits the GUI with a exit code of 0
def exit_object():
    exit(0)



#Initialise
def open_window():
    #Gobal-Variables-Objects
    global Window
    global Button_AIT_Convert, Button_AIT_Download, Button_AIT_Upload, Button_Back_Text_Menu
    global Button_AII_Upload, Button_AII_Download, Button_AII_Convert, Button_Back_Image_Menu
    global Button_Image_Select, Button_Text_Select, Button_Exit_Menu
    global LabelAIT, LabelAIFT, LabelAII, LabelAIFI
    global TextboxAIT, TextboxAIFT
    global Label_AII_Image,Label_AIFI_Image
    global Frame_Text,Frame_Image,Frame_Main_Menu

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


    # Frame-Text
    Frame_Text = Frame(Window, width=Window.winfo_width(), height=Window.winfo_height())

    #Label
    LabelAIT = Label(Frame_Text, text='Insert a AI generated text here:')
    LabelAIFT = Label(Frame_Text, text='Result of the AI generated text:')

    #Textboxes
    TextboxAIT = Text(Frame_Text)
    TextboxAIFT = Text(Frame_Text)

    #TButtons
    Button_AIT_Convert = Button(Frame_Text, text='Change-Text', command=convert_ai_text)
    Button_AIT_Download = Button(Frame_Text, text='Download-Text', command=download_ai_text)
    Button_AIT_Upload = Button(Frame_Text, text='Upload-Text', command=upload_ai_text)
    Button_Back_Text_Menu = Button(Frame_Text, text='Back to Menu', command=select_menu_objects)



    #Packing the Objects
    #TODO: PACK
    Frame_Text.pack()
    LabelAIT.pack()
    LabelAIFT.pack()
    TextboxAIT.pack(side="left")
    TextboxAIFT.pack(side="right")
    Button_AIT_Convert.pack()
    Button_AIT_Download.pack()
    Button_AIT_Upload.pack()
    Button_Back_Text_Menu.pack()





    # Frame-Image
    Frame_Image = Frame(Window, width=Window.winfo_width(), height=Window.winfo_height())

    #Label
    LabelAII = Label(Frame_Image, text='Upload a AI generated Image here:')
    LabelAIFI = Label(Frame_Image, text='Result of the AI generated Image:')

    #Label-Image
    Label_AII_Image = Label(Frame_Image)
    Label_AIFI_Image = Label(Frame_Image)

    #Buttons
    Button_AII_Upload = Button(Frame_Image, text='Upload-Image', command=upload_ai_image)
    Button_AII_Download = Button(Frame_Image, text='Download-Image', command=download_ai_image)
    Button_AII_Convert = Button(Frame_Image, text='Change-Image', command=convert_ai_image)
    Button_Back_Image_Menu = Button(Frame_Image, text='Back to Menu', command=select_menu_objects)



    # Packing the Objects
    # TODO: PACK
    Frame_Image.pack()
    LabelAII.pack()
    LabelAIFI.pack()
    Label_AII_Image.pack()
    Label_AIFI_Image.pack()
    Button_AII_Upload.pack()
    Button_AII_Download.pack()
    Button_AII_Convert.pack()
    Button_Back_Image_Menu.pack()






    #Frame-Main-Menu
    Frame_Main_Menu = Frame(Window, width=Window.winfo_width(), height=Window.winfo_height())

    #Buttons
    Button_Image_Select = Button(Frame_Main_Menu, text='Image Converter', command=select_image_objects)
    Button_Text_Select = Button(Frame_Main_Menu, text='Text Converter', command=select_text_objects)
    Button_Exit_Menu = Button(Frame_Main_Menu, text='Exit', command=exit_object)

    # Packing the Objects
    # TODO: PACK
    Frame_Main_Menu.pack()
    Button_Image_Select.pack()
    Button_Text_Select.pack()
    Button_Exit_Menu.pack()


    #Window Mainloop

    select_menu_objects()
    Window.mainloop()