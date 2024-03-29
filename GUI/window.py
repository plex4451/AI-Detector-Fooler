import tkinter as tk
from GUI.logic import *

"""
This file contains the GUI Window class and the setup for the GUI
"""

class Window(tk.Tk):
    """
    This class represents the GUI Window

    Attributes:
        image_AI (cv2.image): The image of the AI
        image_AIF (cv2.image): The image of the AI after the modification
        Frame_Main_Menu (tk.Frame): The main menu frame
        Frame_AI (tk.Frame): The AI frame
        TextboxAIT (tk.Text): The AI Textbox
        TextboxAIFT (tk.Text): The AI Textbox after the modification
        Label_Left (tk.Label): The left label
        Label_Right (tk.Label): The right label
        Label_Info_Menu (tk.Label): The menu label
        tk_image (tk.PhotoImage): The image of the AI
        Label_AII_Image (tk.Label): The AI image label
        Label_AIFI_Image (tk.Label): The AI image label after the modification
        Button_Text_Select (tk.Button): The text select button
        Button_Image_Select (tk.Button): The image select button
        Button_Exit_Menu (tk.Button): The exit button
        Button_Convert (tk.Button): The convert button
        Button_Download (tk.Button): The download button
        Button_Upload (tk.Button): The upload button
        Button_Back_Menu (tk.Button): The back button
    """
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.title('AI-NOOBS-UNLEASHED: AI FOOLER')
        self.resizable(True, True)
        # Variables
        self.image_AI = cv2.imread("GUI/Assets/no_image.png")
        self.image_AIF = cv2.imread("GUI/Assets/no_image.png")
        self.Frame_Main_Menu = None
        self.Frame_AI = None
        # Textboxs
        self.TextboxAIT = None
        self.TextboxAIFT = None
        # Label
        self.Label_Left = None
        self.Label_Right = None
        self.Label_Info_Menu = None
        # Label-Image
        self.tk_image = None
        self.Label_AII_Image = None
        self.Label_AIFI_Image = None
        # Buttons
        self.Button_Text_Select: Button
        self.Button_Image_Select: Button
        self.Button_Exit_Menu: Button
        self.Button_Convert = None
        self.Button_Download = None
        self.Button_Upload = None
        self.Button_Back_Menu = None
        # Setup
        self._setup()

    def _setup(self):
        """
        This function setups the GUI
        Returns:
            None
        """
        self.setup_main_menu()
        self.setup_ai_frame()
        # self.setup_image_frame()
        self._select_menu_objects()

    def setup_ai_frame(self):
        """
        This function setups the AI frame
        Returns:
            None
        """
        # Ihre Code-Logik für Frame_Text hier
        # Frame-Text
        self.Frame_AI = Frame(self, width=str(self.winfo_screenwidth()), height=str(self.winfo_screenheight()))

        # Label
        self.Label_Left = Label(self.Frame_AI, text='Insert a AI generated text here:')
        self.Label_Right = Label(self.Frame_AI, text='Result of the AI generated text:')

        # Textboxes
        self.TextboxAIT = Text(self.Frame_AI)
        self.TextboxAIFT = Text(self.Frame_AI)

        # Label-Image
        self.tk_image = ImageTk.PhotoImage(Image.open("GUI/Assets/no_image.png"))
        self.Label_AII_Image = Label(self.Frame_AI, image=self.tk_image)
        self.Label_AIFI_Image = Label(self.Frame_AI, image=self.tk_image)

        # TButtons
        self.Button_Convert = Button(self.Frame_AI, text='Change-Text')
        self.Button_Download = Button(self.Frame_AI, text='Download-Text')
        self.Button_Upload = Button(self.Frame_AI, text='Upload-Text')
        self.Button_Back_Menu = Button(self.Frame_AI, text='Back to Menu', command=self._select_menu_objects)

        # Packing the Objects
        # TODO: PACK
        self.Frame_AI.pack()
        self.Label_Left.place(x=str(40), y=str(20), width=str(800), height=str(20))
        self.Label_Right.place(x=str(1080), y=str(20), width=str(800), height=str(20))
        self.TextboxAIT.place(x=str(40), y=str(40), width=str(800), height=str(700))
        self.TextboxAIFT.place(x=str(1080), y=str(40), width=str(800), height=str(700))
        self.Button_Upload.place(x=str(340), y=str(800), width=str(200), height=str(50))
        self.Button_Download.place(x=str(1380), y=str(800), width=str(200), height=str(50))
        self.Button_Convert.place(x=str(860), y=str(390), width=str(200), height=str(50))
        self.Button_Back_Menu.place(x=str(860), y=str(800), width=str(200), height=str(50))
        self.Label_AII_Image.place(x=str(40), y=str(40), width=str(800), height=str(700))
        self.Label_AIFI_Image.place(x=str(1080), y=str(40), width=str(800), height=str(700))

    def setup_main_menu(self):
        """
        This function setups the main menu
        Returns:
            None
        """
        self.Frame_Main_Menu = Frame(self, width=str(self.winfo_screenwidth()), height=str(self.winfo_screenheight()))

        # Label
        self.Label_Info_Menu = Label(self.Frame_Main_Menu, text='AI FOOLER!', font=("Arial", 20))

        # Buttons
        self.Button_Image_Select = Button(self.Frame_Main_Menu, text='Image Converter',
                                          command=self._select_image_objects)
        self.Button_Text_Select = Button(self.Frame_Main_Menu, text='Text Converter', command=self._select_text_objects)
        self.Button_Exit_Menu = Button(self.Frame_Main_Menu, text='Exit', command=exit_object)

        # Packing the Objects
        self.Frame_Main_Menu.pack()
        self.Button_Text_Select.place(x=str(860), y=str(400), width=str(200), height=str(50))
        self.Button_Image_Select.place(x=str(860), y=str(500), width=str(200), height=str(50))
        self.Button_Exit_Menu.place(x=str(860), y=str(600), width=str(200), height=str(50))
        self.Label_Info_Menu.place(x=str(860), y=str(200), width=str(200), height=str(50))

    # Object selection functions
    def _select_text_objects(self):
        """
        This function hides every non Text object and shows every Text object
        Returns:
            None
        """
        self.Frame_AI.pack()
        self.Label_AII_Image.place_forget()
        self.Label_AIFI_Image.place_forget()
        self.Frame_Main_Menu.pack_forget()

        # Change Config of Buttons
        self.Button_Convert.config(command=lambda: convert_ai_text(self), text="Change-Text")
        self.Button_Download.config(command=lambda: download_ai_text(self), text="Download-Text")
        self.Button_Upload.config(command=lambda: upload_ai_text(self), text="Upload-Text")

        # Change Config of Labels
        self.Label_Left.config(text="Insert a AI generated text here:")
        self.Label_Right.config(text="Result of the text algorithm:")

        # Place Textboxes
        self.TextboxAIFT.place(x=str(1080), y=str(40), width=str(800), height=str(700))
        self.TextboxAIT.place(x=str(40), y=str(40), width=str(800), height=str(700))

    # Hides every non Image object and shows every Image object
    def _select_image_objects(self):
        """
        This function hides every non Image object and shows every Image object
        Returns:
            None
        """
        self.Frame_AI.pack()
        self.TextboxAIT.place_forget()
        self.TextboxAIFT.place_forget()
        self.Frame_Main_Menu.pack_forget()

        # Change Config of Buttons
        self.Button_Convert.config(command=lambda: convert_ai_image(self), text="Change-Image")
        self.Button_Download.config(command=lambda: download_ai_image(self), text="Download-Image")
        self.Button_Upload.config(command=lambda: upload_ai_image(self), text="Upload-Image")

        # Change Config of Labels
        self.Label_Left.config(text="Upload a AI generated Image here:")
        self.Label_Right.config(text="Result of the image algorithm:")

        # Place Images
        self.Label_AII_Image.place(x=str(40), y=str(40), width=str(800), height=str(700))
        self.Label_AIFI_Image.place(x=str(1080), y=str(40), width=str(800), height=str(700))

    # Hides every non menu object and shows every Menu object
    def _select_menu_objects(self):
        """
        This function hides every non menu object and shows every Menu object
        Returns:
            None
        """
        self.Frame_AI.pack_forget()
        self.Frame_Main_Menu.pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()
