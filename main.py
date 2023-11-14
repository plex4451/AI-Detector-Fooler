import sys
import threading
from Enums.filetype import *
from Algo.text_algo import *
from APIs.ai_text_detector import get_scores as get_scores_txt
from APIs.ai_image_detector import get_scores as get_scores_image
from GUI.gui import open_window


#open_window_thread: This Method opens the GUI (exist for sepret threading)
def open_window_thread():
    pass

# Test-Txt: This Method test the created txt with the apis
def test_txt(txt: str):
    points_array = get_scores_txt(txt)
    detector_list = ["Grammica.com","Scribbr.com","Detecting-ai.com Methode-A","Detecting-ai.com Methode-B","Writer.com","UKNOWN","UKNOWN","UKNOWN","UKNOWN","UKNOWN"]
    counter = 0
    for i in points_array:
        print(("{name:} score: {score:}%".format(name = detector_list[counter], score = i)))
        counter += 1





#debug: Enables/Disables Debug prints and Methods for Testing
debug = True

open_window()
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
        file = open(inputpath,"r",encoding="utf-8")
        text = file.read()
        file.close()
        final_text = change_text(text)

        file = open(outputpath, "x", encoding='utf-8')
        file.write(final_text)
        file.close()

        if(debug):
            print("----------------------------------------------------------------------------")
            #test_txt(final_text)
            print("----------------------------------------------------------------------------")
            debug_info_text(text, final_text)
            print("----------------------------------------------------------------------------")
            print(final_text)
            print("----------------------------------------------------------------------------")
        print("Text-ALGO Missing.")
        #TODO: INSERT ALGO FOR TEXT HERE

    else:
        print("Image-ALGO Missing")
        #TODO: INSERT ALGO FOR IMAGE HERE
    print("Success!")
