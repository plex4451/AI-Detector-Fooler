import sys
from Enums.filetype import *


print(Filetype.PNG)
inputpath = sys.argv[1]
outputpath = sys.argv[2]
inputtype = getfiletype(inputpath.split('.')[-1])
outputtype = getfiletype(outputpath.split('.')[-1])


if((inputtype != outputtype) or ( (inputtype == Filetype.UNKNOWN) or (outputtype == Filetype.UNKNOWN) ) ):
    if(inputtype != outputtype):
        print("ERROR 001: Output-type and Input-type are different!")
        exit(1)
    else:
        print("ERROR 002: Input-type or Output-type is not known to this Program!")
        exit(2)
else:
    [...]



print(inputpath)
print(outputpath)
