from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expected
from selenium.common.exceptions import StaleElementReferenceException
import time


def setup_selenium() -> (webdriver.Chrome, WebDriverWait):
    """
    This function sets up the Selenium driver and wait
    The driver is set to headless mode.

    Returns:
        driver (webdriver.Chrome): The Selenium driver
        wait (WebDriverWait): The Selenium wait
    """
    selenium_options = webdriver.ChromeOptions()
    selenium_options.add_argument('--headless')
    driver = webdriver.Chrome(options=selenium_options)
    wait = WebDriverWait(driver, 3)
    return driver, wait


def wait_element(driver: webdriver.Chrome, wait: WebDriverWait, element_xpath: str):
    """
    This function waits for an element to be present and returns it.

    Parameters:
        driver (webdriver.Chrome): The Selenium driver
        wait (WebDriverWait): The Selenium wait
        element_xpath (str): The xpath of the element
    Returns:
        element (selenium.webdriver.remote.webelement.WebElement): The Selenium element
    """
    wait.until(Expected.presence_of_element_located((By.XPATH, element_xpath)))
    element = driver.find_element(By.XPATH, element_xpath)
    return element


def wait_element_css(wait: WebDriverWait, css_path: str):
    """
    This function waits for an element to be present and returns it (for CSS elements).

    Parameters:
        wait (WebDriverWait): The Selenium wait
        css_path (str): The CSS path of the element
    Returns:
        element (selenium.webdriver.remote.webelement.WebElement): The Selenium element
    """
    element = wait.until(Expected.presence_of_element_located((By.CSS_SELECTOR, css_path)))
    return element


def wait_for_attribute(wait: WebDriverWait, element, attribute: str):
    """
    This function waits for an attribute to be present.
    Parameters:
        wait (WebDriverWait): The Selenium wait
        element (selenium.webdriver.remote.webelement.WebElement): The Selenium element
        attribute (str): The attribute to wait for
    Returns:
        None
    """
    wait.until(lambda driver: element.get_attribute(attribute).strip() != '')


def wait_element_visible_text(driver: webdriver.Chrome, wait: WebDriverWait, element_xpath: str):
    """
    This function waits for an element to be visible and returns it.

    Parameters:
        driver (webdriver.Chrome): The Selenium driver
        wait (WebDriverWait): The Selenium wait
        element_xpath (str): The xpath of the element
    Returns:
        element (selenium.webdriver.remote.webelement.WebElement): The Selenium element
    """
    element = wait_element(driver, wait, element_xpath)
    wait.until(Expected.visibility_of(element))
    wait.until(ElementVisibilityChecker(element))
    while element.text == "":
        time.sleep(0.5)
    return element


class ElementVisibilityChecker(object):
    """
    This class checks if an element is visible.

    Parameters:
        locator (selenium.webdriver.remote.webelement.WebElement): The Selenium element
    Returns:
        bool: True if the element is visible, False if not
    """

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver) -> bool:
        try:
            element = self.locator
            return element.value_of_css_property("visibility") == "visible"
        except StaleElementReferenceException:
            return False
