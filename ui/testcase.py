"""
Example usage of the common element interface for both Selenium and Playwright.
This demonstrates how to work with elements consistently regardless of the driver.
"""

import pytest
from selenium.webdriver.common.by import By


class TestElementUsage:
    """Example test class showing common element usage patterns."""
    
    @pytest.mark.example
    def test_single_element_operations(self, driver):
        """Example of working with single elements."""
        # Locators
        email_input = (By.XPATH, "//input[@type='email']")
        password_input = (By.XPATH, "//input[@type='password']")
        submit_button = (By.XPATH, "//button[@type='submit']")
        
        # Navigate to page
        driver.goto_home()
        
        # Find and interact with single elements
        email_element = driver.find_element(email_input, timeout=10)
        email_element.type("user@example.com")
        
        password_element = driver.find_element(password_input, timeout=10)
        password_element.type("password123")
        
        submit_element = driver.find_element(submit_button, timeout=10)
        submit_element.click()
        
        # Get attributes
        email_attr = email_element.get_attribute("type")
        print(f"Email input type: {email_attr}")
    
    @pytest.mark.example
    def test_multiple_elements_operations(self, driver):
        """Example of working with multiple elements."""
        # Locator for multiple elements (e.g., all buttons)
        all_buttons = (By.XPATH, "//button")
        
        # Navigate to page
        driver.goto_home()
        
        # Find all elements
        buttons = driver.find_elements(all_buttons, timeout=10)
        
        # Check how many elements found
        print(f"Found {len(buttons)} buttons")
        
        # Iterate through all elements
        for i, button in enumerate(buttons):
            button_text = button.text()
            print(f"Button {i}: {button_text}")
        
        # Get all texts at once
        all_texts = buttons.get_all_texts()
        print(f"All button texts: {all_texts}")
        
        # Get specific element by index
        if len(buttons) > 0:
            first_button = buttons[0]
            first_button.click()
    
    @pytest.mark.example
    def test_element_visibility_checks(self, driver):
        """Example of checking element visibility."""
        # Locators
        visible_element = (By.XPATH, "//header")
        hidden_element = (By.XPATH, "//div[@style='display: none']")
        
        # Navigate to page
        driver.goto_home()
        
        # Check if element is visible
        is_visible = driver.check_if_element_visible(visible_element, timeout=5)
        print(f"Header is visible: {is_visible}")
        
        # Check if element is invisible
        is_invisible = driver.check_if_element_invisible(hidden_element, timeout=5)
        print(f"Hidden div is invisible: {is_invisible}")
    
    @pytest.mark.example
    def test_conditional_element_handling(self, driver):
        """Example of handling elements that may or may not exist."""
        # Locators
        optional_element = (By.XPATH, "//div[@class='optional']")
        
        # Navigate to page
        driver.goto_home()
        
        # Try to find element, handle if not found
        try:
            element = driver.find_element(optional_element, timeout=5)
            print("Optional element found!")
            element.click()
        except Exception as e:
            print(f"Optional element not found: {e}")
            # Continue with test logic
    
    @pytest.mark.example
    def test_dynamic_element_handling(self, driver):
        """Example of handling dynamically loaded elements."""
        # Locator for elements that load dynamically
        dynamic_elements = (By.XPATH, "//div[@class='dynamic-content']")
        
        # Navigate to page
        driver.goto_home()
        
        # Wait for elements to load and then process them
        elements = driver.find_elements(dynamic_elements, timeout=20)
        
        # Process all dynamic elements
        for element in elements:
            if element.is_displayed():
                text = element.text()
                print(f"Dynamic element text: {text}")
                
                # Get all attributes
                class_attr = element.get_attribute("class")
                id_attr = element.get_attribute("id")
                print(f"Class: {class_attr}, ID: {id_attr}")


# Example of how to use the wrapper directly if needed
def direct_wrapper_usage():
    """
    Example of using the wrapper classes directly if you have raw elements.
    This is useful when you need to work with elements from other sources.
    """
    # This would be used when you have raw Selenium or Playwright elements
    # and want to use the common interface
    
    # Example with Selenium element (pseudo-code)
    # selenium_element = driver.find_element(By.ID, "my-element")
    # wrapped_element = ElementWrapper(selenium_element, 'selenium')
    # wrapped_element.click()
    
    # Example with Playwright element (pseudo-code)
    # playwright_element = page.locator("#my-element")
    # wrapped_element = ElementWrapper(playwright_element, 'playwright')
    # wrapped_element.type("text")
    
    pass 