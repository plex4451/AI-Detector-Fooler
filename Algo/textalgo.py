#Debug-Info-Function: Prints information about the String
def debugInfo(original_txt: str,final_txt: str):
    x = 0
    for i in range(0,len(original_txt)):
        if(original_txt[i]!=final_txt[i]):
            x += 1
    percentage_change = (x/len(original_txt))*100
    print("The Text is changed to {}%".format(percentage_change))


#Exchange-Char-Symbol: Replaces letters with similar symbols
def changeLetterSymbol(txt: str) -> str:



# Invisible Char: Replaces Space with a invisible char
def changeInvisibleChar(txt: str) -> str:
    txt = txt.replace(" ", " ")
    return (txt)


# Leetspeak-Algo (replaces letters with numbers)
def changeLeetspeak(txt: str) -> str:
    txt = txt.replace("a", "4")
    txt = txt.replace("A", "4")
    txt = txt.replace("o", "0")
    txt = txt.replace("O", "0")
    txt = txt.replace("t", "7")
    txt = txt.replace("T", "7")
    txt = txt.replace("s", "5")
    txt = txt.replace("S", "5")
    return txt


def changeText(txt: str) -> str:
    txt = changeLeetspeak(txt)
    txt = changeInvisibleChar(txt)
    txt = changeLetterSymbol(txt)
    return (txt)



example_txt = "This is a example Text!"
final_txt = changeText(example_txt)

print(example_txt + "\n")
print(final_txt + "\n")