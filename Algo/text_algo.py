#Variables
#max_percentage: Sets the maximum of percentage the original_txt is changed
max_percentage = 0.5




#Debug-Info-Function: Prints information about the String
def debug_info_text(original_txt: str,final_txt: str):
    x = 0
    for i in range(0,len(original_txt)):
        if(original_txt[i]!=final_txt[i]):
            x += 1
    percentage_change = (x/len(original_txt))*100
    print("The Text is changed to {}%".format(percentage_change))


#Replace-Better: Replaces evenly the letters in the text dependend on the max_percentage variable
def replace_better(txt: str, letter: str, replacment: str) -> str:

    letter_count = txt.count(letter)
    max_possibble_percentage = (letter_count/len(txt))*100
    if(max_possibble_percentage>max_percentage):
        replace_count = round((max_percentage/max_possibble_percentage)*letter_count)
    else:
        replace_count = letter_count
    print(replace_count)
    print(letter_count)
    count = 0
    txt_list = list(txt)
    for i in range(0, len(txt)):
        if ((txt_list[i] == letter) and (count < replace_count)):
            txt_list[i] = replacment
            count += 1
    txt = "".join(txt_list)
    return txt















#Exchange-Char-Same-Char: Replaces letters with identical letters
def change_letter_simillar_letter(txt: str) -> str:
    txt = replace_better(txt,"a","а")
    #txt =replace_better(txt,"a","a\ufeff")
    return(txt)

#Exchange-Char-Symbol: Replaces letters with similar symbols
def change_letter_symbol(txt: str) -> str:
    txt = replace_better(txt,"a","@")
    return(txt)



# Invisible Char: Replaces Space with a invisible char
def change_invisible_char(txt: str) -> str:
    txt = replace_better(txt," ", " ")
    return (txt)


# Leetspeak-Algo (replaces letters with numbers)
def change_leet_speak(txt: str) -> str:
    txt = replace_better(txt,"a", "4")
    txt = replace_better(txt,"A", "4")
    txt = replace_better(txt,"o", "0")
    txt = replace_better(txt,"O", "0")
    txt = replace_better(txt,"t", "7")
    txt = replace_better(txt,"T", "7")
    txt = replace_better(txt,"s", "5")
    txt = replace_better(txt,"S", "5")
    return txt

#Main Methode to change txt (Deactivate certain Methods with a "#")
def change_text(txt: str) -> str:
    original_txt = txt
    txt = change_letter_simillar_letter(txt)
    #txt = change_invisible_char(txt)
    #txt = change_letter_symbol(txt)
    #txt = change_leet_speak(txt)
    return (txt)



