import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from basepage import Basepage
from element_wrapper import ElementWrapper, ElementsListWrapper


class SeleniumBasepage(Basepage):

    def __init__(self, driver):
        self.driver = next(driver)
        self.driver_type = 'selenium'

    def wait_for_element_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def goto_home(self):
        home_url = os.getenv("INS_URL")
        self.driver.get(home_url)

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        self.wait_for_element_visibility(locator, timeout)
        element = self.driver.find_element(*locator)
        return ElementWrapper(element, self.driver_type)

    def find_elements(self, locator, timeout=10):
        # Wait for at least one element to be visible
        self.wait_for_element_visibility(locator, timeout)
        elements = self.driver.find_elements(*locator)
        return ElementsListWrapper(elements, self.driver_type)

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def type(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.type(text)

    def hover(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element.element).perform()

    def check_if_element_visible(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except Exception:
            return False

    def check_if_element_invisible(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_attribute(self, locator, attribute, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)
