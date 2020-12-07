from selenium.webdriver.common.by import By


class BaseLocators:
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    SUBMIT = (By.XPATH, '//input[@name="submit"]')

    INCORRECT_USERNAME_LENGTH = (
        By.XPATH, "//div[contains(text(), 'Incorrect username length') and not(contains(@style,"
                  "'visibility: hidden;'))]")


class MainPageLocators(BaseLocators):
    REGISTRATION = (By.XPATH, '//a[@href="/reg"]')


class RegistrationLocators(BaseLocators):
    EMAIL = (By.XPATH, '//input[@name="email"]')
    REPEAT_PASSWORD = (By.XPATH, '//input[@name="confirm"]')
    SDET = (By.XPATH, '//input[@name="term"]')
    INCORRECT_EMAIL_LENGTH = (By.XPATH, "//div[contains(text(), 'Incorrect email length') and not(contains(@style,"
                                        "'visibility: hidden;'))]")
    DIFFERENT_PASSWORDS = (By.XPATH, "//div[contains(text(), 'Passwords must match') and not(contains(@style,"
                                     "'visibility: hidden;'))]")
    USER_ALREADY_EXIST = (By.XPATH, "//div[contains(text(), 'User already exist') and not(contains(@style,"
                                    "'visibility: hidden;'))]")


class WelcomeLocators:
    LOGOUT = (By.XPATH, '//a[@href="/logout"]')
    WHAT_IS_AN_API = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    FUTURE_OF_INTERNET = (By.XPATH,
                          '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of'
                          '-the-internet/"]')
    LETS_TALK_ABOUT_SMTP = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')
    PYTHON = (By.XPATH, '//a[@href="https://www.python.org/"]')
    PYTHON_HISTORY = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/History_of_Python"]')
    ABOUT_FLASK = (By.XPATH, '//a[@href="https://flask.palletsprojects.com/en/1.1.x/#"]')
    LINUX = (By.XPATH, '//a[@href="javascript:" and text()="Linux"]')
    DOWNLOAD_CENTOS = (By.XPATH, '//a[@href="https://getfedora.org/ru/workstation/download/"]')
    NETWORK = (By.XPATH, '//a[@href="javascript:" and text()="Network"]')
    WIRESHARK_NEWS = (By.XPATH, '//a[@href="https://www.wireshark.org/news/"]')
    WIRESHARK_DOWNLOAD = (By.XPATH, '//a[@href="https://www.wireshark.org/#download"]')
    TCPDUMP_EXAMPLES = (By.XPATH, '//a[@href="https://hackertarget.com/tcpdump-examples/"]')