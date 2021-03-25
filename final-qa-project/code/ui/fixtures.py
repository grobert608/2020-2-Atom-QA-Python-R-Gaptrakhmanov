import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.welcome_page import WelcomePage


@pytest.fixture(scope='function')
def auth(driver, add_user, config):
    name, email = add_user
    main_page = MainPage(driver, config)
    main_page.login(name, config['default_password'])
    return WelcomePage(driver, config)


@pytest.fixture(scope='function')
def base_page(driver, config):
    return BasePage(driver, config)


@pytest.fixture(scope='function')
def main_page(driver, config):
    return MainPage(driver, config)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    selenoid = config['selenoid']

    if not selenoid:
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())
    else:
        capabilities = {
            'browserName': "chrome",
            'version': '80'
        }
        options = ChromeOptions()
        driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
