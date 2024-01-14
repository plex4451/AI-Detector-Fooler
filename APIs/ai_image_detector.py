# -------------------------------IMPORTS------------------------------------------
from APIs.selenium_utils import setup_selenium, wait_for_attribute, wait_element_visible_text, wait_element_css
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expected
import time

# -------------------------------SELENIUM---------------------------------------
# Setup Selenium and get driver and wait
driver, wait = setup_selenium()

# -------------------------------DEBUG------------------------------------------
# Define test image url
test_image_url = "/Users/loukielhorn/Downloads/8-4fqx1SIbpiFAChp.png"


def __get_score_from_huggingface(image_path: str) -> float:
    """
    This function gets the score from Huggingface.co

    Parameters:
        image_path (str): The path to the image
    Returns:
        float: The score from Huggingface.co

    """
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


def __get_score_from_illuminarty(image_path: str) -> float:
    """
    This function gets the score from Illuminarty.ai

    Parameters:
        image_path (str): The path to the image
    Returns:
        float: The score from Illuminarty.ai

    """
    try:
        driver.get("https://app.illuminarty.ai/")

        # Accept popup
        try:
            cookie_button = wait.until(Expected.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div/div/div[2]/button[2]")))
            cookie_button.click()
        except:
            print("Illuminarty.ai no cookie popup found!")

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


def __get_score_from_isitai(image_path: str) -> float:
    """
    This function gets the score from Isitai.com

    Parameters:
        image_path (str): The path to the image
    Returns:
        float: The score from Isitai.com

    """
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


def __get_score_from_hivemoderation(image_path: str) -> float:
    """
    This function gets the score from Hivemoderation.com

    Parameters:
        image_path (str): The path to the image
    Returns:
        float: The score from Hivemoderation.com

    """
    try:
        driver.get("https://hivemoderation.com/ai-generated-content-detection")
        time.sleep(3)
        image_detection = wait.until(Expected.element_to_be_clickable((By.CSS_SELECTOR, 'div.jss142[data-attr="2"]')))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", image_detection)
        time.sleep(3)
        image_detection.click()

        # Upload image
        image_field = wait_element_css(wait, 'input[type="file"][accept="image/png,image/jpeg,image/jpg,image/webp"]')
        image_field.send_keys(image_path)

        time.sleep(2.5)
        score = wait_element_visible_text(driver, wait, "//span[contains(text(), '%') and not(contains(text(), '>'))]").text

        print("Hivemoderation.com score: " + score + " AI created image!")
        return float(score.replace('%', ''))
    except:
        print("Hivemoderation.com is not available!")
        return -1


def get_ai_image_scores(path):
    scores = []
    scores.append(__get_score_from_hivemoderation(path))
    scores.append(__get_score_from_illuminarty(path))
    scores.append(__get_score_from_isitai(path))
