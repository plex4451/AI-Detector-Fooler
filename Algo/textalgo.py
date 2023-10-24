# Invisible Char: Replaces Space with a invisible char
def changeInvisiblechar(txt: str) -> str:
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
    txt = changeInvisiblechar(txt)
    return (txt)



example_txt = "This is a example Text!"
final_txt = changeText(example_txt)

print(example_txt + "\n")
print(final_txt + "\n")