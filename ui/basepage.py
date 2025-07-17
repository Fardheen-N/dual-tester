from abc import ABC, abstractmethod

class Basepage(ABC):

    @abstractmethod
    def goto_home(self):
        pass

    @abstractmethod
    def get_url(self, url):
        pass

    @abstractmethod
    def find_element(self, locator, timeout):
        pass

    @abstractmethod
    def click(self, locator, timeout):
        pass

    @abstractmethod
    def type(self, locator, text, timeout):
        pass

    @abstractmethod
    def hover(self, locator, timeout):
        pass

    @abstractmethod
    def check_if_element_visible(self, locator, timeout):
        pass

    @abstractmethod
    def check_if_element_invisible(self, locator, timeout):
        pass

    @abstractmethod
    def get_attribute(self, locator, attribute, timeout):
        pass

    @abstractmethod
    def find_elements(self, locator, timeout):
        pass


