from enum import Enum


class Filetype(Enum):
    TXT = 1
    JPG = 2
    JPEG = 3
    PNG = 4
    UNKNOWN = 5


#Filetype = Enum('Filetype', ['TXT', 'JPG', 'PNG', 'UNKNOWN'])

def getfiletype(s :str)-> Filetype:
    if s == "TXT":
        return Filetype.TXT
    elif s == "JPG":
        return Filetype.JPG
    elif s == "JPEG":
        return Filetype.JPEG
    elif s == "PNG":
        return Filetype.PNG
    else:
        return Filetype.UNKNOWN