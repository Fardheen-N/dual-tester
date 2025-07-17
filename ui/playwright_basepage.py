import os
from basepage import Basepage
from playwright.sync_api import expect
from element_wrapper import ElementWrapper, ElementsListWrapper
import logging as log

class PlaywrightBasepage(Basepage):

    def __init__(self, driver):
        self.driver = next(driver)
        self.driver_type = 'playwright'

    def goto_home(self):
        home_url = os.getenv("INS_URL")
        self.get_url(home_url)

    def get_url(self, url):
        self.driver.goto(url)

    def find_element(self, locator, timeout=10):
        element = self.driver.locator(locator[1])
        element.wait_for(timeout=timeout*1000)
        return ElementWrapper(element, self.driver_type)

    def find_elements(self, locator, timeout=10):
        # Playwright returns a locator that can be used to get all elements
        elements = self.driver.locator(locator[1])
        elements.wait_for(timeout=timeout*1000)
        # Convert to list for consistency with Selenium
        element_list = elements.all()
        return ElementsListWrapper(element_list, self.driver_type)

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def type(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.type(text)

    def hover(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.element.hover()

    def check_if_element_visible(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except Exception as e:
            log.error(f"Exception: {e}")
            return False

    def check_if_element_invisible(self, locator, timeout=10):
        try:
            expect(
                self.driver.locator(locator[1])
            ).to_be_visible(visible=False, timeout=timeout*1000)
            return True
        except Exception as e:
            log.error(f"Exception: {e}")
            return False

    def get_attribute(self, locator, attribute, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)