import pytest
import platform
from datetime import date


class TestSimpleSuite:
    @pytest.fixture(autouse=True, scope='function')
    def __get_fixture(self, simple_suite_fixture):
        self.page = simple_suite_fixture

    def test_check_date(self):
        text = self.page.main_page.get_title()
        website_date = text[text.find("(") + 1:text.find(")")]
        today = date.today()
        if platform.system() == 'Linux' or 'Darwin':
            system_date = today.strftime("%B %-d, %Y")  # for Linux and MacOS
        else:
            system_date = today.strftime("%B %#d, %Y")  # for Windows
        assert website_date == system_date
