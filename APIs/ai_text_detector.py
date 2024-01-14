# -------------------------------IMPORTS------------------------------------------
from APIs.selenium_utils import setup_selenium, wait_element, wait_element_visible_text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as Expected
from time import *

# -------------------------------SELENIUM------------------------------------------
# Setup Selenium and get driver and wait
driver, wait = setup_selenium()

# -------------------------------DEBUG------------------------------------------



def __get_score_from_grammica(text_to_check: str) -> float:
    """
    This function gets the score from Grammica.com

    Parameters:
        text_to_check (str): The text to check
    Returns:
        float: The score from Grammica.com

    """
    try:
        driver.get("https://grammica.com/ai-detector")
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="text"]')
        textbox.send_keys(text_to_check)
        score = wait_element_visible_text(driver, wait, '//*[@id="fake-percentage"]').text
        print("Grammica.com score: " + score + " from AI written text!")
        return float(score.replace('%', ''))
    except:
        print("Grammica.com is not available!")
    return -1


def __get_score_from_scribbr(text_to_check: str) -> float:
    """
    This function gets the score from Scribbr.com

    Parameters:
        text_to_check (str): The text to check
    Returns:
        float: The score from Scribbr.com

    """
    try:
        driver.get("https://www.scribbr.com/ai-detector/")

        # Accept cookies
        #cookie_button = wait.until(Expected.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
        #cookie_button.click()

        # Input text and get score
        textbox = driver.find_element(by=By.XPATH, value='//*[@role="textbox"]')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="aiDetectorButton"]')
        detect_button.click()
        score = wait_element_visible_text(driver, wait, '//*[@id="aiDetector"]/div[2]/div/div[1]/div[3]/span[1]').text
        print("Scribbr.com score: " + score + " from AI written text!")
        return float(score.replace('%', ''))
    except:
        print("Scribbr.com is not available! Text could be to short!")
    return -1


def __get_score_from_detectingai(text_to_check: str)-> float:
    """
    This function gets the score from Detecting-ai.com

    Parameters:
        text_to_check (str): The text to check
    Returns:
        float: The score from Detecting-ai.com
    """
    try:
        driver.get("https://detecting-ai.com/de/detect_ai/")
        # Input text and click submit button
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="input-text"]')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="send_text"]')
        detect_button.click()

        # Get score A
        score_element = wait_element(driver, wait, '//*[@id="ai-generated"]')
        score_a = score_element.get_attribute("aria-valuenow")
        print("Detecting-ai.com Methode-A score: " + score_a + "% from AI written text!")

        # Select method B and submit
        method_dropdown = driver.find_element(by=By.XPATH, value='//*[@id="model_option"]')
        select = Select(method_dropdown)
        select.select_by_value("detector_2")
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="send_text"]')
        detect_button.click()

        # Get score B
        score_element = wait_element(driver, wait, '//*[@id="ai-generated"]')
        score_b = score_element.get_attribute("aria-valuenow")
        print("Detecting-ai.com Methode-B score: " + score_b + "% from AI written text!")

        return float(score_a), float(score_b)
    except:
        print("Detecting-ai.com is not available!")
        return -1

def __get_score_from_gptzero(text_to_check) -> float:
    try:
        driver.get("https://gptzero.me/")
        # Input text and click submit button
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/textarea')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/button')
        detect_button.click()

        # Get score
        score = wait_element(driver, wait, '//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/span[2]/b/text()[1]')
        print("GPTzero score: " + score + "% from AI written text!")
        return score
    except:
        print("GPTzero.me is not available!")
        return -1

def __get_score_from_writer(text_to_check) -> float:
    try:
        driver.get("https://writer.com/ai-content-detector/")
        # Input text and click submit button
        textbox = driver.find_element(by=By.XPATH,value='/html/body/div[3]/div[2]/div[2]/div[1]/form/div[2]/textarea')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH,value='/html/body/div[3]/div[2]/div[2]/div[1]/form/button')
        detect_button.click()

        # Get score
        sleep(5)
        score = int(wait_element(driver, wait,'//*[@id="ai-percentage"]').text)
        print("Writer score: " + str((100-score)) + "% from AI written text!")
        return 100-score
    except:
        print("Writer.com is not available!")
        return -1


def get_scores(text_to_check):
    scores = []
    scores.append(__get_score_from_grammica(text_to_check))
    #scores.append(__get_score_from_scribbr(text_to_check))
    scores.append(-1)
    arr_help = __get_score_from_detectingai(text_to_check)
    scores.append(arr_help[0])
    scores.append(arr_help[1])
    #scores.append(__get_score_from_gptzero(text_to_check))
    #scores.append(__get_score_from_writer(text_to_check))
    driver.close()
    return scores

