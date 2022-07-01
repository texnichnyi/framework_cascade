import os

from selenium import webdriver


class Driver:
    """
      Class for working with driver
      """
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "geckodriver"))
        self.driver.get('https://www.holidayscalendar.com/')

    def close_driver(self):
        self.driver.quit()
