"""
Element wrapper utility to handle differences between Selenium and Playwright element objects.
This provides a common interface for working with elements regardless of the underlying driver.
"""

class ElementWrapper:
    """
    Wrapper class to provide a common interface for elements from both Selenium and Playwright.
    """
    
    def __init__(self, element, driver_type):
        """
        Initialize the wrapper with an element and driver type.
        
        Args:
            element: The element object from Selenium or Playwright
            driver_type: 'selenium' or 'playwright'
        """
        self.element = element
        self.driver_type = driver_type
    
    def click(self):
        """Click the element."""
        if self.driver_type == 'selenium':
            self.element.click()
        else:  # playwright
            self.element.click()
    
    def type(self, text):
        """Type text into the element."""
        if self.driver_type == 'selenium':
            self.element.clear()
            self.element.send_keys(text)
        else:  # playwright
            self.element.fill(text)
    
    def get_attribute(self, attribute):
        """Get an attribute value from the element."""
        if self.driver_type == 'selenium':
            return self.element.get_attribute(attribute)
        else:  # playwright
            return self.element.get_attribute(attribute)
    
    def is_displayed(self):
        """Check if element is displayed."""
        if self.driver_type == 'selenium':
            return self.element.is_displayed()
        else:  # playwright
            return self.element.is_visible()
    
    def text(self):
        """Get the text content of the element."""
        if self.driver_type == 'selenium':
            return self.element.text
        else:  # playwright
            return self.element.text_content()


class ElementsListWrapper:
    """
    Wrapper class to provide a common interface for lists of elements.
    """
    
    def __init__(self, elements, driver_type):
        """
        Initialize the wrapper with a list of elements and driver type.
        
        Args:
            elements: List of elements from Selenium or Playwright
            driver_type: 'selenium' or 'playwright'
        """
        self.elements = elements
        self.driver_type = driver_type
    
    def __len__(self):
        """Return the number of elements."""
        return len(self.elements)
    
    def __getitem__(self, index):
        """Get element at specific index."""
        element = self.elements[index]
        return ElementWrapper(element, self.driver_type)
    
    def __iter__(self):
        """Iterate over elements."""
        for element in self.elements:
            yield ElementWrapper(element, self.driver_type)
    
    def get_all_texts(self):
        """Get text from all elements."""
        texts = []
        for element in self:
            texts.append(element.text())
        return texts
    
    def get_all_attributes(self, attribute):
        """Get specific attribute from all elements."""
        attributes = []
        for element in self:
            attributes.append(element.get_attribute(attribute))
        return attributes 