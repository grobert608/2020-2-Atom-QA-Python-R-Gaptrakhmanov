import pytest

from ui.pages.base_page import BasePage
from ui.pages.auth_page import AuthPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: AuthPage = request.getfixturevalue('main_page')
