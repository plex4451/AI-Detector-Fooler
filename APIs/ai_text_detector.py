# -------------------------------IMPORTS------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expected
from selenium.common.exceptions import StaleElementReferenceException

import time

# -------------------------------DETECTORS------------------------------------------
grammica_enabled = True

# Define test text
test_text = "School is a place that has a significant impact on the lives of young people. It is not only an institution of learning but also a hub for social interaction and personal growth. In this essay, I would like to shed light on the importance of school as an educational institution and as a venue for social development.School is a place that has a significant impact on the lives of young people. It is not only an institution of learning but also a hub for social interaction and personal growth. In this essay, I would like to shed light on the importance of school as an educational institution and as a venue for social development."

# -------------------------------SELENIUM------------------------------------------
selenium_options = webdriver.ChromeOptions()
selenium_options.add_argument('--headless')

# Initialize the web driver with the options
driver = webdriver.Chrome(options=selenium_options)

# Defines Selenium Misc Options
wait = WebDriverWait(driver, 10)


class ElementVisibilityChecker(object):
    # This class checks if a selenium web element is visible
    def __init__(self, locator):
        self.locator = locator

    # Callable method to check visibility
    def __call__(self, driver):
        try:
            element = self.locator
            return element.value_of_css_property("visibility") == "visible"
        except StaleElementReferenceException:
            return False


def wait_element(element_xpath):
    # Waits until a certain element appears, and then returns that element
    wait.until(Expected.presence_of_element_located((By.XPATH, element_xpath)))
    element = driver.find_element(By.XPATH, element_xpath)
    return element


def wait_element_visible_text(element_xpath):
    # Waits until a certain element is visible & has text, and then returns that element
    element = wait_element(element_xpath)
    wait.until(Expected.visibility_of(element))
    wait.until(ElementVisibilityChecker(element))
    while element.text == "":
        time.sleep(0.5)
    return element


def get_score_from_grammica(text_to_check) -> int:
    # Gets score from Grammica.com -> only english!
    try:
        driver.get("https://grammica.com/ai-detector")
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="text"]')
        textbox.send_keys(text_to_check)
        score = wait_element_visible_text('//*[@id="fake-percentage"]').text
        print("Grammica.com score: " + score + " from AI written text!")
    except:
        print("Grammica.com is not available!")
    return 0


def get_score_from_scribbr(text_to_check) -> int:
    # Gets score from Scribbr.com -> only english!
    try:
        driver.get("https://www.scribbr.com/ai-detector/")
        textbox = driver.find_element(by=By.XPATH, value='//*[@role="textbox"]')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="aiDetectorButton"]')
        detect_button.click()
        score = wait_element_visible_text('//*[@id="aiDetector"]/div[2]/div/div[1]/div[3]/span[1]').text
        print("Scribbr.com score: " + score + " from AI written text!")
    except:
        print("Scribbr.com is not available! Text could be to short!")
    return 0


def get_score_from_detectingai(text_to_check) -> int:
    # Gets score from Detecting-ai.com -> geman & english
    try:
        driver.get("https://detecting-ai.com/de/detect_ai/")
        textbox = driver.find_element(by=By.XPATH, value='//*[@id="input-text"]')
        textbox.send_keys(text_to_check)
        detect_button = driver.find_element(by=By.XPATH, value='//*[@id="send_text"]')
        detect_button.click()
        score_element = wait_element('//*[@id="ai-generated"]')
        score = score_element.get_attribute("aria-valuenow")
        print("Detecting-ai.com score: " + score + "% from AI written text!")
    except Exception as e:
        print("Detecting-ai.com is not available!")
    return 0


driver.close()
