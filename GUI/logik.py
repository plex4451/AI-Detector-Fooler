from __future__ import annotations
from Algo.text_algo import *
from Algo.imagealgo import *
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import cv2
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from GUI.window import Window


def convert_ai_text(window: Window):
    """
    Converts the text in the TextboxAIT and returns it to TextboxAIFT

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    txt = window.TextboxAIT.get("1.0", "end-1c")
    txt = change_text(txt)
    window.TextboxAIFT.delete("1.0", "end")
    window.TextboxAIFT.insert("end", txt)


def upload_ai_text(window: Window):
    """
    Uploads a text file to the TextboxAIT

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),))
    if file_path:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        file.close()
        window.TextboxAIT.delete("1.0", "end")
        window.TextboxAIT.insert("end", text)
    else:
        print("ERROR: No File selected!")


def download_ai_text(window: Window):
    """
    Downloads the text from the TextboxAIFT to a file

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ])
    if file_path:
        file = open(file_path, 'w', encoding="utf-8")
        file.write(window.TextboxAIFT.get("1.0", "end"))
        file.close()
    else:
        print("ERROR: No File selected!")


# AI-Image-Methods
def convert_ai_image(window: Window):
    image = use_alog_on_image(window.image_AI)
    window.image_AIF = image
    image_AI_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image_AI_rgb)
    tk_image = ImageTk.PhotoImage(image)
    window.Label_AIFI_Image.config(image=tk_image)
    window.Label_AIFI_Image.image = tk_image


def upload_ai_image(window: Window):
    file_path = filedialog.askopenfilename(filetypes=(("PNG files", "*.png"), ("JPGimple files", "*.jpg")))
    if file_path:
        image = Image.open(file_path)
        tk_image = ImageTk.PhotoImage(image)
        window.Label_AII_Image.config(image=tk_image)
        window.Label_AII_Image.image = tk_image
        window.image_AI = cv2.imread(file_path)


def download_ai_image(window: Window):
    image = window.image_AIF
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=([("PNG files", "*.png"), ("JPG files", "*.jpg")]))
    cv2.imwrite(file_path, image)


# exit_object Method, exits the GUI with a exit code of 0
def exit_object():
    exit(0)
