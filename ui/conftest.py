import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright
from playwright_basepage import PlaywrightBasepage
from selenium_basepage import SeleniumBasepage


def selenium_driver():
    chrome = Options()
    # chrome.add_argument("--headless")
    session_driver = webdriver.Chrome(options=chrome)
    yield session_driver
    session_driver.quit()

def playwright_driver():
    driver = sync_playwright().start()
    browser = driver.chromium.launch(
        headless=False,
        channel="chrome"
    )
    yield browser.new_page()
    browser.close()
    driver.stop()

@pytest.fixture(scope='session', autouse=True)
def driver():
    load_dotenv()
    driver_option = os.getenv("DRIVER")
    if driver_option == 'selenium':
        base_object = SeleniumBasepage(selenium_driver())
    else:
        base_object = PlaywrightBasepage(playwright_driver())
    return base_object
