# Variables
# max_percentage: Sets the maximum of percentage the original_txt is changed
# TODO: MAX_PERCENTAGE DOESN'T WORK
max_percentage = 200


# Debug-Info-Function: Prints information about the String
def debug_info_text(original_txt: str, final_txt: str):
    x = 0
    for i in range(0, len(original_txt)):
        if (original_txt[i] != final_txt[i]):
            x += 1
    percentage_change = (x / len(original_txt)) * 100
    print("The Text is changed to {}%".format(percentage_change))


# Replace-Better: Replaces evenly the letters in the text dependend on the max_percentage variable
def replace_better(txt: str, letter: str, replacment: str) -> str:
    letter_count = txt.count(letter)
    if (letter_count == 0):
        return (txt)
    max_possibble_percentage = (letter_count / len(txt)) * 100
    if (max_possibble_percentage > max_percentage):
        replace_count = round((max_percentage / max_possibble_percentage) * letter_count)
    else:
        replace_count = letter_count

    print("{} letters to replace!".format(replace_count))
    print("{} letters can be replaced!".format(letter_count))
    count = 0
    goal_count = round(letter_count / replace_count + 1)

    txt_list = list(txt)
    for i in range(0, len(txt)):
        if ((txt_list[i] == letter)):
            count += 1
            letter_count -= 1
            if ((letter_count == 0) and (count > 0)) or (count == goal_count):
                txt_list[i] = replacment
                count = 0
    txt = "".join(txt_list)
    print("{} letters replaced!".format(txt.count(replacment)))

    return txt


def change_letter_similar_letter(txt: str) -> str:
    """
    Replaces letters with similar letters from different alphabets

    Parameters:
        txt (str): The Text to modify
    Returns:
        str: The modified Text
    """
    return replace_better(txt, "a", "а")


def change_letter_symbol(txt: str) -> str:
    """
    Replaces letters with similar symbols

    Parameters:
        txt (str): The Text to modify
    Returns:
        str: The modified Text
    """
    return replace_better(txt, "a", "@")


def change_invisible_char(txt: str) -> str:
    """
    Replaces Spaces with non-breaking Spaces

    Parameters:
        txt (str): The Text to modify
    Returns:
        str: The modified Text

    """
    return replace_better(txt, " ", " ")

def change_leet_speak(txt: str) -> str:
    """
    Leetspeak-Algo (replaces letters with numbers)
    Parameters:
        txt (str): The Text to modify
    Returns:
        str: The modified Text
    """

    replacements = {
        "a": "4", "A": "4",
        "o": "0", "O": "0",
        "t": "7", "T": "7",
        "s": "5", "S": "5"
    }
    for original, replacement in replacements.items():
        txt = replace_better(txt, original, replacement)
    return txt


def change_text(txt: str) -> str:
    """
   Modify the Text with a combination of Algos
    Parameters:
        txt (str): The Text to modify
    Returns:
        str: The modified Text
    """
    modified_txt = change_letter_similar_letter(txt)
    # modified_txt = change_invisible_char(modified_txt)
    # modified_txt = change_letter_symbol(modified_txt)
    # modified_txt = change_leet_speak(modified_txt)
    return modified_txt
