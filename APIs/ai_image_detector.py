# -------------------------------IMPORTS------------------------------------------
from APIs.selenium_utils import setup_selenium, wait_for_attribute, wait_element_visible_text, wait_element_css
from selenium.webdriver.common.by import By

# -------------------------------SELENIUM------------------------------------------
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
        score = wait_element_visible_text(driver, wait,'//*[@id="result-container"]/div[1]/div[2]/div[2]').text

        print("Isitai.com score: " + score + " AI created image!")
        return float(score.replace('%', ''))
    except:
        print("Isitai.com is not available!")
        return -1


def get_scores(image_to_check):
    scores = []
    scores.append(__get_score_from_huggingface(image_to_check))
    scores.append(__get_score_from_illuminarty(image_to_check))
    scores.append(__get_score_from_isitai(image_to_check))
    driver.close()
    return scores
