from .base_page import BasePage
from ui.locators.locators import MainPageLocators, WelcomeLocators
from selenium.common.exceptions import TimeoutException

from .registration_page import RegistrationPage
from .welcome_page import WelcomePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def to_registration(self):
        self.click(self.locators.REGISTRATION)
        return RegistrationPage(self.driver, self.config)

    def login(self, username, password):
        self.find(self.locators.USERNAME).send_keys(username)
        self.find(self.locators.PASSWORD).send_keys(password)
        self.click(self.locators.SUBMIT)

        try:
            welcome_locators = WelcomeLocators()
            self.find(welcome_locators.LOGOUT, 1)
            return WelcomePage(self.driver, self.config)
        except TimeoutException:
            return self
