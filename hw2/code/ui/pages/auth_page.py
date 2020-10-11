from ui.locators.locators import AuthPageLocators
from .base_page import BasePage
from .main_page import MainPage


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, username, password):
        self.click(self.locators.LOGIN_BUTTON)
        self.find(self.locators.LOGIN_FIELD).send_keys(username)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.click(self.locators.CONFIRM_LOGIN)
        return MainPage(self.driver, self.config)
