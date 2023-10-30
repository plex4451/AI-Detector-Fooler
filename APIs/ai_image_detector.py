# -------------------------------IMPORTS----------------------------------------
from APIs.selenium_utils import setup_selenium, wait_for_attribute, wait_element_visible_text, wait_element_css
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expected
from selenium.webdriver import Keys

import cv2
import base64
import tempfile

# -------------------------------SELENIUM---------------------------------------
# Setup Selenium and get driver and wait
driver, wait = setup_selenium()

# -------------------------------DEBUG------------------------------------------
# Define test image url
test_image_url = "/Users/loukielhorn/Downloads/8-4fqx1SIbpiFAChp.png"


def __get_score_from_huggingface(image_path) -> float:
    # Gets score from Huggingface.co
    try:
        driver.get("https://huggingface.co/spaces/umm-maybe/AI-image-detector")

        # Switch to the iframe
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)

        # Upload image
        image_field = wait_element_css(wait, 'input.hidden-upload')
        image_field.send_keys(image_path)
        wait_for_attribute(wait, image_field, 'value')

        # Submit and get score
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="component-10"]')
        submit_button.click()
        score = wait_element_visible_text(driver, wait, '//*[@id="component-2"]/div[3]/div[2]/div/div[2]/div[3]').text

        # Switch back to default
        driver.switch_to.default_content()
        print("Huggingface.co score: " + score + " AI created image!")
        return float(score.replace('%', ''))
    except:
        print("Huggingface.co is not available!")
        return -1


def __get_score_from_illuminarty(image_path) -> float:
    # Gets score from Illuminarty.ai
    try:
        driver.get("https://app.illuminarty.ai/")

        # Accept popup
        cookie_button = wait.until(Expected.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div/div/div[2]/button[2]")))
        cookie_button.click()

        # Upload image
        image_field = wait_element_css(wait, 'input[type="file"]')
        image_field.send_keys(image_path)
        wait_for_attribute(wait, image_field, 'value')

        # Get score
        score = wait_element_visible_text(driver, wait, '//*[@id="analysisCntr"]/aside/div[1]/div[2]/div/div/p').text
        score = score.replace('AI Probability: ', '')

        print("Illuminarty.ai score: " + score + " AI created image!")
        return float(score.replace('%', ''))
    except:
        print("Illuminarty.ai is not available!")
        return -1


def __get_score_from_isitai(image_path) -> float:
    # Gets score from Isitai.com
    try:
        driver.get("https://isitai.com/ai-image-detector/")

        # Upload image
        image_field = wait_element_css(wait, 'input[type="file"]')
        image_field.send_keys(image_path)
        wait_for_attribute(wait, image_field, 'value')

        # Submit and get score
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="submit-button"]')
        submit_button.click()
        score = wait_element_visible_text(driver, wait, '//*[@id="result-container"]/div[1]/div[2]/div[2]').text

        print("Isitai.com score: " + score + " AI created image!")
        return float(score.replace('%', ''))
    except:
        print("Isitai.com is not available!")
        return -1


def get_ai_image_scores(image):
    # Convert the image to bytes and then to a base64-encoded string
    image_bytes = cv2.imencode(".png", image)[1].tobytes()
    image_base64 = base64.b64encode(image_bytes).decode()

    # Create a temporary file and write the base64-encoded image to it
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        temp_file.write(base64.b64decode(image_base64))
        temp_file_path = temp_file.name

    scores = []
    scores.append(__get_score_from_illuminarty(temp_file_path))
    scores.append(__get_score_from_isitai(temp_file_path))
