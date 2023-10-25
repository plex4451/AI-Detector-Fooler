from enum import Enum


class Filetype(Enum):
    TXT = 1
    JPG = 2
    PNG = 3
    UNKNOWN = 4


#Filetype = Enum('Filetype', ['TXT', 'JPG', 'PNG', 'UNKNOWN'])

def getfiletype(s :str)-> Filetype:
    if s == "TXT":
        return Filetype.TXT
    elif s == "JPG":
        return Filetype.JPG
    elif s == "PNG":
        return Filetype.PNG
    else:
        return Filetype.UNKNOWN