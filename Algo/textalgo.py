#Variables
max_percentage = 100




#Debug-Info-Function: Prints information about the String
def debug_info(original_txt: str,final_txt: str):
    x = 0
    for i in range(0,len(original_txt)):
        if(original_txt[i]!=final_txt[i]):
            x += 1
    percentage_change = (x/len(original_txt))*100
    print("The Text is changed to {}%".format(percentage_change))


#Exchange-Char-Symbol: Replaces letters with similar symbols
def change_letter_symbol(txt: str) -> str:
    txt = txt.replace("a","@")
    return(txt)



# Invisible Char: Replaces Space with a invisible char
def change_invisible_char(txt: str) -> str:
    txt = txt.replace(" ", " ")
    return (txt)


# Leetspeak-Algo (replaces letters with numbers)
def change_leet_speak(txt: str) -> str:
    txt = txt.replace("a", "4")
    txt = txt.replace("A", "4")
    txt = txt.replace("o", "0")
    txt = txt.replace("O", "0")
    txt = txt.replace("t", "7")
    txt = txt.replace("T", "7")
    txt = txt.replace("s", "5")
    txt = txt.replace("S", "5")
    return txt

#Main Methode to change txt (Deactivate certain Methods with a "#")
def change_text(txt: str) -> str:
    original_txt = txt
    txt = change_invisible_char(txt)
    #txt = change_letter_symbol(txt)
    #txt = change_leet_speak(txt)
    return (txt)



