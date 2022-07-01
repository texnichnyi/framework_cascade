import modules.ui.base.base_page


class Main:
    """
    Example of single page
    """
    def __init__(self, base_page):
        self.base: modules.ui.base.base_page.BasePageActions = base_page
        self.title = self.base.locator_class_name('vc_custom_heading')
        self.bla = self.base.locator_xpath("//a[@href='https://www.holidayscalendar.com/event/canada-day/']")

    def get_title(self):
        return self.base.get_text(self.title)
