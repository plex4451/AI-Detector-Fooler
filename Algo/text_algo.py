# Variables
# max_percentage: Sets the maximum of percentage the original_txt is changed
# TODO: MAX_PERCENTAGE DOESN'T WORK

max_percentage = 200


def compare_two_strings(first_txt: str, second_txt: str):
    """
    Compares two Strings and prints the percentage of difference

    Parameters:
        first_txt (str): The original Text
        second_txt (str): The modified Text
    Returns:
        None
    """
    num_difference = 0
    for i in range(0, len(first_txt)):
        if first_txt[i] != second_txt[i]:
            num_difference += 1
    percentage_change = (num_difference / len(first_txt)) * 100
    print("The Text is changed to "f"{percentage_change}%")


def replace_last_letter(txt: str, letter: str, replacement: str) -> str:
    """
    Replaces the last valid letter in the text

    Parameters:
        txt (str): The Text to modify
        letter (str): The letter to replace
        replacement (str): The replacement for the letter
    Returns:
        str: The modified Text with the replaced letter
    """
    last_letter_index = txt.rfind(letter)
    return txt[:last_letter_index] + replacement + txt[last_letter_index + 1:]


def replace_better(txt: str, letter: str, replacement: str) -> str:
    """
    Replaces letters in the text evenly dependent on the max_percentage variable
    
    Parameters:
        txt (str): The Text to modify
        letter (str): The letter to replace
        replacement (str): The replacement for the letter
    Returns:
        str: The modified Text
    """
    letter_count = txt.count(letter)
    if letter_count == 0:
        return txt

    max_possible_percentage = (letter_count / len(txt)) * 100
    if max_possible_percentage > max_percentage:
        replace_count = round((max_percentage / max_possible_percentage) * letter_count)
    else:
        replace_count = letter_count

    print(f"{replace_count} letters to replace!")
    print(f"{letter_count} letters can be replaced!")
    count = 0
    goal_count = round(letter_count / replace_count + 1)

    final_txt = ""
    for char in txt:
        if char == letter:
            count += 1
            if count == goal_count:
                final_txt += replacement
                count = 0
                continue

        final_txt += char

    final_txt = replace_last_letter(final_txt, letter, replacement)

    print(f"{final_txt.count(replacement)} letters replaced!")

    return final_txt


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
