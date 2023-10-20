# -------------------------------IMPORTS------------------------------------------
from selenium_utils import setup_selenium, wait_element, wait_element_visible_text
from selenium.webdriver.common.by import By

# -------------------------------SELENIUM------------------------------------------
# Setup Selenium and get driver and wait
driver, wait = setup_selenium()

# -------------------------------DEBUG------------------------------------------
# Define test text
test_text = "School is a place that has a significant impact on the lives of young people. It is not only an institution of learning but also a hub for social interaction and personal growth. In this essay, I would like to shed light on the importance of school as an educational institution and as a venue for social development.School is a place that has a significant impact on the lives of young people. It is not only an institution of learning but also a hub for social interaction and personal growth. In this essay, I would like to shed light on the importance of school as an educational institution and as a venue for social development."


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


def __get_score_from_detectingai(text_to_check) -> float:
    # Gets score from Detecting-ai.com -> geman & english
    try:
        driver.get("https://detecting-ai.com/de/detect_ai/")
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="input-text"]')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="send_text"]')
        detect_button.click()
        score_element = wait_element(driver, wait, '//*[@id="ai-generated"]')
        score = score_element.get_attribute("aria-valuenow")
        print("Detecting-ai.com score: " + score + "% from AI written text!")
        return float(score)
    except:
        print("Detecting-ai.com is not available!")
    return -1


def get_scores(text_to_check):
    scores = []
    scores.append(__get_score_from_grammica(text_to_check))
    scores.append(__get_score_from_scribbr(text_to_check))
    scores.append(__get_score_from_detectingai(text_to_check))
    driver.close()


get_scores(test_text)