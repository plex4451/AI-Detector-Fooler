# -------------------------------IMPORTS------------------------------------------
from APIs.selenium_utils import setup_selenium, wait_element, wait_element_visible_text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as Expected

# -------------------------------SELENIUM------------------------------------------
# Setup Selenium and get driver and wait
driver, wait = setup_selenium()

# -------------------------------DEBUG------------------------------------------
# Define test text
test_text = "This is a example Text!"


def __get_score_from_grammica(text_to_check) -> float:
    # Gets score from Grammica.com -> only english!
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


def __get_score_from_scribbr(text_to_check) -> float:
    # Gets score from Scribbr.com -> only english!
    try:
        driver.get("https://www.scribbr.com/ai-detector/")

        # Accept cookies
        cookie_button = wait.until(Expected.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
        cookie_button.click()

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


def __get_score_from_detectingai(text_to_check):
    # Gets score from Detecting-ai.com -> geman & english
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

def get_scores(text_to_check):
    scores = []
    scores.append(__get_score_from_grammica(text_to_check))
    scores.append(__get_score_from_scribbr(text_to_check))
    arr_help = __get_score_from_detectingai(text_to_check)
    scores.append(arr_help[0])
    scores.append(arr_help[1])
    driver.close()
    return scores

