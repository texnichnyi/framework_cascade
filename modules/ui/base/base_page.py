from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from modules.ui.base.locator import Locators


class BasePageActions:
    """
    Class for working with pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.locator_class_name = Locators.class_name
        self.locator_xpath = Locators.xpath
        self.timeout = 10

    def wait_for_element(self, locator: Locators.Locator) -> WebElement:
        return WebDriverWait(self.driver, timeout=self.timeout) \
            .until(ec.visibility_of_element_located(locator=locator))

    def get_text(self, locator: Locators.Locator):
        element = self.wait_for_element(locator)
        return element.text
