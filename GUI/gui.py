#Library
from tkinter import *
from Algo.text_algo import *
from Algo.image_algo import *
from tkinter import filedialog
from PIL import Image,ImageTk
import cv2

#TODO: REWRITE LABELS
#Variables
#TODO: MAYBE REMOVE THEM LATER
image_AI = cv2.imread("GUI/Assets/no_image.png")
image_AIF = cv2.imread("GUI/Assets/no_image.png")

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
    global image_AIF
    image = use_alog_on_image(image_AI)
    image_AIF = image
    image_AI_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image_AI_rgb)
    tk_image = ImageTk.PhotoImage(image)
    Label_AIFI_Image.config(image=tk_image)
    Label_AIFI_Image.image = tk_image


def upload_ai_image():
    global image_AI
    file_path = filedialog.askopenfilename(filetypes=(("PNG files", "*.png"),("JPGimple files","*.jpg")))
    if file_path:
        image = Image.open(file_path)
        tk_image = ImageTk.PhotoImage(image)
        Label_AII_Image.config(image=tk_image)
        Label_AII_Image.image = tk_image
        image_AI = cv2.imread(file_path)
    


def download_ai_image():
    image = image_AIF
    file_path = filedialog.asksaveasfilename(defaultextension=".png",   filetypes=([("PNG files", "*.png"),("JPG files","*.jpg")]))
    cv2.imwrite(file_path, image)







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
    Window.geometry(str(Window.winfo_screenwidth())+"x"+str(Window.winfo_screenheight()))
    Window.title('AI-NOOBS-UNLEASHED: AI FOOLER')
    Window.resizable(True, True)

    # Frame-Text
    Frame_Text = Frame(Window, width=str(Window.winfo_screenwidth()), height=str(Window.winfo_screenheight()))

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
    LabelAIT.place(x=str(40),y=str(20),width=str(800),height=str(20))
    LabelAIFT.place(x=str(1080),y=str(20),width=str(800),height=str(20))
    TextboxAIT.place(x=str(40),y=str(40),width=str(800),height=str(700))
    TextboxAIFT.place(x=str(1080),y=str(40),width=str(800),height=str(700))
    Button_AIT_Upload.place(x=str(340), y=str(800), width=str(200), height=str(50))
    Button_AIT_Download.place(x=str(1380), y=str(800), width=str(200), height=str(50))
    Button_AIT_Convert.place(x=str(860), y=str(390), width=str(200), height=str(50))
    Button_Back_Text_Menu.place(x=str(860),y=str(800),width=str(200),height=str(50))





    # Frame-Image
    Frame_Image = Frame(Window,  width=str(Window.winfo_screenwidth()), height=str(Window.winfo_screenheight()))

    #Label
    LabelAII = Label(Frame_Image, text='Upload a AI generated Image here:')
    LabelAIFI = Label(Frame_Image, text='Result of the AI generated Image:')

    #Label-Image
    tk_image = ImageTk.PhotoImage(Image.open("GUI/Assets/no_image.png"))
    Label_AII_Image = Label(Frame_Image, image=tk_image)
    Label_AIFI_Image = Label(Frame_Image, image=tk_image)

    #Buttons
    Button_AII_Upload = Button(Frame_Image, text='Upload-Image', command=upload_ai_image)
    Button_AII_Download = Button(Frame_Image, text='Download-Image', command=download_ai_image)
    Button_AII_Convert = Button(Frame_Image, text='Change-Image', command=convert_ai_image)
    Button_Back_Image_Menu = Button(Frame_Image, text='Back to Menu', command=select_menu_objects)



    # Packing the Objects
    # TODO: PACK
    Frame_Image.pack()
    LabelAII.place(x=str(40),y=str(20),width=str(800),height=str(20))
    LabelAIFI.place(x=str(1080),y=str(20),width=str(800),height=str(20))
    Label_AII_Image.place(x=str(40),y=str(40),width=str(800),height=str(700))
    Label_AIFI_Image.place(x=str(1080),y=str(40),width=str(800),height=str(700))
    Button_AII_Upload.place(x=str(340), y=str(800), width=str(200), height=str(50))
    Button_AII_Download.place(x=str(1380), y=str(800), width=str(200), height=str(50))
    Button_AII_Convert.place(x=str(860), y=str(390), width=str(200), height=str(50))
    Button_Back_Image_Menu.place(x=str(860),y=str(800),width=str(200),height=str(50))






    #Frame-Main-Menu
    Frame_Main_Menu = Frame(Window,  width=str(Window.winfo_screenwidth()), height=str(Window.winfo_screenheight()))

    #Label
    Label_Info_Menu = Label(Frame_Main_Menu,text='AI FOOLER!',font=("Arial", 20))

    #Buttons
    Button_Image_Select = Button(Frame_Main_Menu, text='Image Converter', command=select_image_objects)
    Button_Text_Select = Button(Frame_Main_Menu, text='Text Converter', command=select_text_objects)
    Button_Exit_Menu = Button(Frame_Main_Menu, text='Exit', command=exit_object)

    # Packing the Objects
    # TODO: PACK
    Frame_Main_Menu.pack()
    Button_Text_Select.place(x=str(860), y=str(400), width=str(200), height=str(50))
    Button_Image_Select.place(x=str(860), y=str(500), width=str(200), height=str(50))
    Button_Exit_Menu.place(x=str(860), y=str(600), width=str(200), height=str(50))
    Label_Info_Menu.place(x=str(860), y=str(200), width=str(200), height=str(50))


    #Window Mainloop

    select_menu_objects()
    Window.mainloop()