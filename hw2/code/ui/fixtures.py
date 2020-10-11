import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.auth_page import AuthPage


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def login(driver, config):
    main_page = AuthPage(driver, config)
    main_page.click(main_page.locators.LOGIN_BUTTON)
    main_page.find(main_page.locators.LOGIN_FIELD).send_keys(config['username'])
    main_page.find(main_page.locators.PASSWORD_FIELD).send_keys(config['password'])
    main_page.click(main_page.locators.CONFIRM_LOGIN)
    return MainPage(driver, config['username'])


@pytest.fixture(scope='function')
def base_page(driver, config):
    return BasePage(driver, config)


@pytest.fixture(scope='function')
def main_page(driver, config):
    return AuthPage(driver, config)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if browser == 'chrome':
        if not selenoid:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
        else:
            options = ChromeOptions()
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True})
    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
