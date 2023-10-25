import sys
from Enums.filetype import *
from Algo.textalgo import *

inputpath = sys.argv[1]
outputpath = sys.argv[2]
inputtype = getfiletype(inputpath.split('.')[-1].upper())
outputtype = getfiletype(outputpath.split('.')[-1].upper())
print("Filetype of the Input: {}".format(inputtype))
print("Filetype of the Output: {}".format(outputtype))

# ERROR Handeling with mismatching Filetypes and UKNOWN Filetypes
if ((inputtype != outputtype) or ((inputtype == Filetype.UNKNOWN) or (outputtype == Filetype.UNKNOWN))):
    if (inputtype != outputtype):
        print("ERROR 001: Output-type and Input-type are mismatching!")
        exit(1)
    else:
        print("ERROR 002: Input-type or Output-type is not known to this Program!")
        exit(2)
else:
    if(inputtype == Filetype.TXT):
        file = open(inputpath)
        text = file.read()
        file.close()

        final_text = changeText(text)

        file = open(outputpath, "x")
        file.write(final_text)
        file.close()


        print("Text-ALGO Missing.")
        #TODO: INSERT ALGO FOR TEXT HERE

    else:
        print("Image-ALGO Missing")
        #TODO: INSERT ALGO FOR IMAGE HERE
    print("Success!")
