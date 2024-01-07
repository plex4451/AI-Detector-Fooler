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
    Changes the text in the TextboxAIT and returns it to TextboxAIFT

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


def convert_ai_image(window: Window):
    """
    Changes the image in the Label_AII_Image and returns it to Label_AIFI_Image

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    image = use_alog_on_image(window.image_AI)
    window.image_AIF = image
    image_AI_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image_AI_rgb)
    tk_image = ImageTk.PhotoImage(image)
    window.Label_AIFI_Image.config(image=tk_image)
    window.Label_AIFI_Image.image = tk_image


def upload_ai_image(window: Window):
    """
    Uploads an image file to the Label_AII_Image

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    file_path = filedialog.askopenfilename(filetypes=(("PNG files", "*.png"), ("JPGimple files", "*.jpg")))
    if file_path:
        image = Image.open(file_path)
        tk_image = ImageTk.PhotoImage(image)
        window.Label_AII_Image.config(image=tk_image)
        window.Label_AII_Image.image = tk_image
        window.image_AI = cv2.imread(file_path)
    else:
        print("ERROR: No File selected!")


def download_ai_image(window: Window):
    """
    Downloads the image from the Label_AIFI_Image to a file

    Parameters:
        window (Window): The Window object
    Returns:
        None
    """
    image = window.image_AIF
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=([("PNG files", "*.png"), ("JPG files", "*.jpg")]))
    if file_path:
        cv2.imwrite(file_path, image)
    else:
        print("ERROR: No File selected!")


def exit_object():
    """
    Exits the GUI with an exit code of 0

    Parameters:
        None
    Returns:
        None
    """
    exit(0)
