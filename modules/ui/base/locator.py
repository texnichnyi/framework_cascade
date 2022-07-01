from collections import namedtuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Locators:
    """
    Class of Locator object builder
    """
    Locator = namedtuple("Locator", ["by", "value"])

    @staticmethod
    def class_name(value: str) -> Locator:
        """
        Building Locator object by class name selector
        """
        return Locators.Locator(By.CLASS_NAME, value)

    @staticmethod
    def xpath(value: str) -> Locator:
        """
        Building Locator object by xpath selector
        """
        return Locators.Locator(By.XPATH, value)
