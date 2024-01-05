import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from logik import *
from tkinter import *
from PIL import Image,ImageTk
import cv2



# TODO: REWRITE LABELS
# Variables
# TODO: MAYBE REMOVE THEM LATER

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.title('AI-NOOBS-UNLEASHED: AI FOOLER')
        self.resizable(True, True)
        # Variables
        self.image_AI = cv2.imread("Assets/no_image.png")
        self.image_AIF = cv2.imread("Assets/no_image.png")
        self.Frame_Main_Menu = None
        self.Label_Info_Menu = None
        self.Button_Text_Select: Button
        self.Button_Image_Select: Button
        self.Button_Exit_Menu: Button
        self.Frame_Text = None
        self.LabelAIT = None
        self.TextboxAIT = None
        self.LabelAIFT = None
        self.TextboxAIFT = None
        self.Button_ait_convert = None
        self.Button_AIT_Download = None
        self.Button_AIT_Upload = None
        self.Button_Back_Text_Menu = None
        self.Frame_Image = None

        # Label
        self.LabelAII = None
        self.LabelAIFI = None

        # Label-Image
        self.tk_image = None
        self.Label_AII_Image = None
        self.Label_AIFI_Image = None

        # Buttons
        self.Button_AII_Upload = None
        self.Button_AII_Download = None
        self.Button_AII_Convert = None
        self.Button_Back_Image_Menu = None
        # Setup
        self._setup()

    def _setup(self):
        self.setup_main_menu()
        self.setup_text_frame()
        self.setup_image_frame()
        self._select_menu_objects()


    def setup_text_frame(self):
        # Ihre Code-Logik für Frame_Text hier
        # Frame-Text
        self.Frame_Text = Frame(self, width=str(self.winfo_screenwidth()), height=str(self.winfo_screenheight()))

        # Label
        self.LabelAIT = Label(self.Frame_Text, text='Insert a AI generated text here:')
        self.LabelAIFT = Label(self.Frame_Text, text='Result of the AI generated text:')

        # Textboxes
        self.TextboxAIT = Text(self.Frame_Text)
        self.TextboxAIFT = Text(self.Frame_Text)

        # TButtons
        self.Button_ait_convert = Button(self.Frame_Text, text='Change-Text')
        self.Button_AIT_Download = Button(self.Frame_Text, text='Download-Text')
        self.Button_AIT_Upload = Button(self.Frame_Text, text='Upload-Text')
        self.Button_Back_Text_Menu = Button(self.Frame_Text, text='Back to Menu')

        # Packing the Objects
        # TODO: PACK
        self.Frame_Text.pack()
        self.LabelAIT.place(x=str(40), y=str(20), width=str(800), height=str(20))
        self.LabelAIFT.place(x=str(1080), y=str(20), width=str(800), height=str(20))
        self.TextboxAIT.place(x=str(40), y=str(40), width=str(800), height=str(700))
        self.TextboxAIFT.place(x=str(1080), y=str(40), width=str(800), height=str(700))
        self.Button_AIT_Upload.place(x=str(340), y=str(800), width=str(200), height=str(50))
        self.Button_AIT_Download.place(x=str(1380), y=str(800), width=str(200), height=str(50))
        self.Button_ait_convert.place(x=str(860), y=str(390), width=str(200), height=str(50))
        self.Button_Back_Text_Menu.place(x=str(860), y=str(800), width=str(200), height=str(50))

    def setup_image_frame(self):
        # Ihre Code-Logik für self.Frame_Image hier
        # Frame-Image
        self.Frame_Image = Frame(self, width=str(self.winfo_screenwidth()), height=str(self.winfo_screenheight()))

        # Label
        self.LabelAII = Label(self.Frame_Image, text='Upload a AI generated Image here:')
        self.LabelAIFI = Label(self.Frame_Image, text='Result of the AI generated Image:')

        # Label-Image
        self.tk_image = ImageTk.PhotoImage(Image.open("Assets/no_image.png"))
        self.Label_AII_Image = Label(self.Frame_Image, image=self.tk_image)
        self.Label_AIFI_Image = Label(self.Frame_Image, image=self.tk_image)

        # Buttons
        self.Button_AII_Upload = Button(self.Frame_Image, text='Upload-Image')
        self.Button_AII_Download = Button(self.Frame_Image, text='Download-Image')
        self.Button_AII_Convert = Button(self.Frame_Image, text='Change-Image')
        self.Button_Back_Image_Menu = Button(self.Frame_Image, text='Back to Menu')

        # Packing the Objects
        # TODO: PACK
        self.Frame_Image.pack()
        self.LabelAII.place(x=str(40), y=str(20), width=str(800), height=str(20))
        self.LabelAIFI.place(x=str(1080), y=str(20), width=str(800), height=str(20))
        self.Label_AII_Image.place(x=str(40), y=str(40), width=str(800), height=str(700))
        self.Label_AIFI_Image.place(x=str(1080), y=str(40), width=str(800), height=str(700))
        self.Button_AII_Upload.place(x=str(340), y=str(800), width=str(200), height=str(50))
        self.Button_AII_Download.place(x=str(1380), y=str(800), width=str(200), height=str(50))
        self.Button_AII_Convert.place(x=str(860), y=str(390), width=str(200), height=str(50))
        self.Button_Back_Image_Menu.place(x=str(860), y=str(800), width=str(200), height=str(50))

    def setup_main_menu(self):
        # Ihre Code-Logik für Frame_Main_Menu hier
        self.Frame_Main_Menu = Frame(self, width=str(self.winfo_screenwidth()), height=str(self.winfo_screenheight()))

        # Label
        self.Label_Info_Menu = Label(self.Frame_Main_Menu, text='AI FOOLER!', font=("Arial", 20))

        # Buttons
        self.Button_Image_Select = Button(self.Frame_Main_Menu, text='Image Converter',command=self._select_image_objects)
        self.Button_Text_Select = Button(self.Frame_Main_Menu, text='Text Converter', command=self._select_text_objects)
        self.Button_Exit_Menu = Button(self.Frame_Main_Menu, text='Exit',command=exit_object)

        # Packing the Objects
        # TODO: PACK
        self.Frame_Main_Menu.pack()
        self.Button_Text_Select.place(x=str(860), y=str(400), width=str(200), height=str(50))
        self.Button_Image_Select.place(x=str(860), y=str(500), width=str(200), height=str(50))
        self.Button_Exit_Menu.place(x=str(860), y=str(600), width=str(200), height=str(50))
        self.Label_Info_Menu.place(x=str(860), y=str(200), width=str(200), height=str(50))

    # Weitere Methoden wie convert_ai_text, download_ai_text usw.




if __name__ == "__main__":
    app = Window()
    app.mainloop()
