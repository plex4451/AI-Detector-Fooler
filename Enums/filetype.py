from enum import Enum


class Filetype(Enum):
    TXT = 1
    JPEG = 2
    PNG = 3
    UNKNOWN = 4


#Filetype = Enum('Filetype', ['TXT', 'JPEG', 'PNG', 'UNKNOWN'])

def getfiletype(s :str)-> Filetype:
    if s == "TXT":
        return Filetype.TXT
    elif s == "JPEG":
        return Filetype.JPEG
    elif s == "PNG":
        return Filetype.PNG
    else:
        return Filetype.UNKNOWN