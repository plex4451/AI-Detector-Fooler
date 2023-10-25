import sys
from Enums.filetype import *
from Algo.textalgo import *
from APIs.ai_text_detector import get_scores as get_scores_txt
from APIs.ai_image_detector import get_scores as get_scores_image


# Test-Txt: This Method test the created txt with the apis
def testTxt(txt: str):
    points_array = get_scores_txt(txt)
    for i in points_array:
        print(i)






debug = True
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
        print(final_text)
        if(debug): testTxt(final_text)

        print("Text-ALGO Missing.")
        #TODO: INSERT ALGO FOR TEXT HERE

    else:
        print("Image-ALGO Missing")
        #TODO: INSERT ALGO FOR IMAGE HERE
    print("Success!")
