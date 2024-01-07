from enum import Enum

"""
This file contains the Filetype enum.
"""


class Filetype(Enum):
    """
    An enum to represent the file type of a file.

    Attributes:
        TXT (int): The file is a text file.
        JPG (int): The file is a jpg file.
        JPEG (int): The file is a jpeg file.
        PNG (int): The file is a png file.
        UNKNOWN (int): The file type is unknown.
    """
    TXT = 1
    JPG = 2
    JPEG = 3
    PNG = 4
    UNKNOWN = 5


def get_file_type(file_type: str) -> Filetype:
    """
    Returns the Filetype enum based on the file type string.

    Parameters:
        file_type (str): The String to check
    Returns:
      Filetype: The corresponding Filetype enum.
    """
    filetypes = {
        "TXT": Filetype.TXT,
        "JPG": Filetype.JPG,
        "JEPG": Filetype.JPEG,
        "PNG": Filetype.PNG
    }
    return filetypes.get(file_type, Filetype.UNKNOWN)
