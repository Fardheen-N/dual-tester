import time
from time import sleep
import pytest
from selenium.webdriver.common.by import By
import logging as log


class TestMain:

    @staticmethod
    def product_price(product_name):
        return (By.XPATH, f"//div[a[contains(@title, '{product_name}')]]//div[@class='Nx9bqj']")

    @pytest.mark.login
    def test_flipkart_product(self, driver):
        s_box = (By.XPATH, "//input[@name='q']")
        s_button = (By.XPATH, "//button[contains(@aria-label, 'Search ')]")
        price_tag = (By.XPATH, "//div[@class='Nx9bqj']")

        driver.goto_home()
        if driver.check_if_element_visible(s_box, timeout=20):
            log.info("Element is visible")
        driver.type(s_box, "CMF buds 2 pro")
        driver.click(s_button)
        log.info("search successful")
        p_xpath = self.product_price("CMF by Nothing Buds Pro 2")
        log.info(f"Product XPATH: {p_xpath}")
        price = driver.find_elements(p_xpath, timeout=10)
        lowest_price = price[0].text()
        lowest_price_product = None
        for p in price:
            if p.text() <= lowest_price:
                lowest_price = p.text()
                lowest_price_product = p
        log.info(f"Product: {lowest_price_product.text()}")
        lowest_price_product.click()
        # driver.click((By.XPATH, "//button[contains(@aria-label, 'Add to Cart')]"))
        # driver.click((By.XPATH, "//button[contains(@aria-label, 'Go to Cart')]"))
        # driver.click((By.XPATH, "//button[contains(@aria-label, 'Checkout')]"))
        # driver.click((By.XPATH, "//button[contains(@aria-label, 'Continue')]"))
        # driver.click((By.XPATH, "//button[contains(@aria-label, 'Continue')]"))
        sleep(10)
