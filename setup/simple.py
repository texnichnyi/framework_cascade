from modules.ui.base.base_page import BasePageActions
from modules.ui.base.driver import Driver
from modules.ui.pages.main import Main


class SimpleSuite:
    """
    Setup module
    """
    def __init__(self):
        self.__runner = Driver()
        self.__driver = self.__runner.driver
        self.__base_page = BasePageActions(driver=self.__driver)
        self.main_page = Main(
            base_page=self.__base_page
        )
        # add all pages that should exist for test suite

    def tear_down(self):
        self.__runner.close_driver()
