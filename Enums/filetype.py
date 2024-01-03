from enum import Enum


class Filetype(Enum):
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
