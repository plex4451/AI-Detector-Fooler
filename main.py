import sys
import threading
from Enums.filetype import *
from Algo.imagealgo import *
from Algo.text_algo import *
from APIs.ai_text_detector import get_scores as get_scores_txt
from APIs.ai_image_detector import *
from GUI.window import Window
import time
import cv2




# Test-Txt: This Method test the created txt with the apis
def test_txt(txt: str):
    points_array = get_scores_txt(txt)
    detector_list = ["Grammica.com","Scribbr.com","Detecting-ai.com Methode-A","Detecting-ai.com Methode-B","Writer.com","UKNOWN","UKNOWN","UKNOWN","UKNOWN","UKNOWN"]
    counter = 0
    for i in points_array:
        print(("{name:} score: {score:}%".format(name = detector_list[counter], score = i)))
        counter += 1




def main_method():
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
            start_time = time.time()
            file = open(inputpath,"r",encoding="utf-8")
            text = file.read()
            file.close()
            final_text = change_text(text)
            try:
                file = open(outputpath, "x", encoding='utf-8')
            except:
                file = open(outputpath, "w", encoding='utf-8')
            file.write(final_text)
            file.close()
            end_time = time.time()
            elapsed_time = end_time - start_time    
            
            print("----------------------------------------------------------------------------")
            print("Text Algo used in: ", elapsed_time)
            print("----------------------------------------------------------------------------")

            if(debug):
                print("----------------------------------------------------------------------------")
                #test_txt(final_text)
                print("test_txt is disabled!")
                print("----------------------------------------------------------------------------")
                compare_two_strings(text, final_text)
                print("----------------------------------------------------------------------------")
                print(final_text)
                print("----------------------------------------------------------------------------")
            print("Text-ALGO Completed")
        
        else: 
            start_time = time.time()
            image = cv2.imread(inputpath)
            final_image = use_alog_on_image(image)
            cv2.imwrite(outputpath, final_image)
            end_time = time.time()
            elapsed_time = end_time - start_time    

            print("----------------------------------------------------------------------------")
            print("Image Algo used in: ", elapsed_time)
            print("----------------------------------------------------------------------------")
            print("Image-Algo Completed!")

# MAIN-METHOD

# debug: Enables/Disables Debug prints and Methods for Testing
debug = True
# ERROR Handleing with missing arguments
try:
    inputpath = sys.argv[1]
    outputpath = sys.argv[2]
except:
    print("ERROR 003: No given Arguments! The program needs two arguments -> main.py <inputpath> <outputpath>")
    exit(3)
inputtype = get_file_type(inputpath.split('.')[-1].upper())
outputtype = get_file_type(outputpath.split('.')[-1].upper())
print("----------------------------------------------------------------------------")
print("Filetype of the Input: {}".format(inputtype))
print("Filetype of the Output: {}".format(outputtype))
print("----------------------------------------------------------------------------")
main_thread = threading.Thread(target=main_method())
main_thread.start()
app = Window()
app.mainloop()
main_thread.join()
print("Success!")
