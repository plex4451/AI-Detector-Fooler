import sys
import threading
from Enums.filetype import *
from Algo.image_algo import *
from Algo.text_algo import *
from APIs.ai_text_detector import get_ai_text_scores as get_scores_txt
from APIs.ai_image_detector import *
from GUI.window import Window
import time
import cv2


# Test-Txt: This Method test the created txt with the apis
def test_txt(txt: str):
    points_array = get_scores_txt(txt)
    detector_list = ["Grammica.com", "Scribbr.com", "Detecting-ai.com Methode-A", "Detecting-ai.com Methode-B",
                     "Writer.com"]
    counter = 0
    for i in points_array:
        print(("{name:} score: {score:}%".format(name=detector_list[counter], score=i)))
        counter += 1


def main_method():
    """
    This is the main method of the program that converts the input file to the output file from the given arguments
    Returns:
        None
    """
    # ERROR Handling with mismatching Filetypes (not the sam) and UKNOWN Filetypes
    if ((input_type == Filetype.TXT or output_type == Filetype.TXT) and (output_type != input_type)) or (
            (input_type == Filetype.UNKNOWN) or (output_type == Filetype.UNKNOWN)):
        if input_type == Filetype.UNKNOWN or output_type == Filetype.UNKNOWN:
            print("ERROR 002: Input-type or Output-type is not known to this Program!")
            exit(2)
        else:
            print("ERROR 001: Output-type and Input-type are mismatching!")
            exit(1)

    else:
        if input_type == Filetype.TXT:
            """
            This is the main method for the Text-Algo
            """
            start_time = time.time()

            file = open(input_path, "r", encoding="utf-8")
            text = file.read()
            file.close()

            final_text = change_text(text)

            try:
                file = open(output_path, "x", encoding='utf-8')
            except:
                file = open(output_path, "w", encoding='utf-8')
            file.write(final_text)
            file.close()

            end_time = time.time()
            elapsed_time = end_time - start_time

            print("----------------------------------------------------------------------------")
            print("Text Algo used in: ", elapsed_time)
            print("----------------------------------------------------------------------------")

            if debug:
                print("----------------------------------------------------------------------------")
                # test_txt(final_text)
                print("test_txt is disabled!")
                print("----------------------------------------------------------------------------")
                compare_two_strings(text, final_text)
                print("----------------------------------------------------------------------------")
                print(final_text)
                print("----------------------------------------------------------------------------")
            print("Text-ALGO Completed!")

        else:
            """
            This is the main method for the Image-Algo
            """
            start_time = time.time()
            image = cv2.imread(input_path)
            final_image = use_alog_on_image(image)
            cv2.imwrite(output_path, final_image)
            end_time = time.time()
            elapsed_time = end_time - start_time

            print("----------------------------------------------------------------------------")
            print("Image Algo used in: ", elapsed_time)
            print("----------------------------------------------------------------------------")
            print("Image-Algo Completed!")



"""
This is the main method of the program
"""
# debug: Enables/Disables Debug prints and Methods for Testing
debug = False
# ERROR Handling with missing arguments
try:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
except:
    print("ERROR 003: No given Arguments! The program needs two arguments -> main.py <inputpath> <outputpath>")
    exit(3)

input_type = get_file_type(input_path.split('.')[-1].upper())
output_type = get_file_type(output_path.split('.')[-1].upper())

print("----------------------------------------------------------------------------")
print("Filetype of the Input: {}".format(input_type))
print("Filetype of the Output: {}".format(output_type))
print("----------------------------------------------------------------------------")

main_thread = threading.Thread(target=main_method())
main_thread.start()

app = Window()
app.mainloop()

main_thread.join()
print("Success!")
