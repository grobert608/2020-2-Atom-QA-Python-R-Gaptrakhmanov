import allure

from conftest import *
from tests.base import BaseCase
from ui.pages.welcome_page import WelcomePage
from ui.pages.web_instances import ApiPage, SmtpPage, PopularMechanicsPage, PythonPage, PythonHistoryPage, \
    AboutFlaskPage, DownloadCentosPage, WiresharkDownloadPage, WiresharkNewsPage, TCPDumpExamplesPage


class TestWelcome(BaseCase):

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_what_is_an_api(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_whatIsAnApi(), ApiPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_future_of_internet(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_futureOfInternet(), PopularMechanicsPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_lets_talk_about_smtp(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_letsTalkAboutSmtp(), SmtpPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_python(), PythonPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python_history(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_pythonHistory(), PythonHistoryPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python_history(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_pythonHistory(), PythonHistoryPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_about_flask(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_aboutFlask(), AboutFlaskPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_download_centos(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_downloadCentos(), DownloadCentosPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_wireshark_news(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_wiresharkNews(), WiresharkNewsPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_wireshark_download(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_wiresharkDownload(), WiresharkDownloadPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_tcpdump_examples(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.to_tcpdumpExamples(), TCPDumpExamplesPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_logout(self, auth):
        from ui.pages.main_page import MainPage
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.logout(), MainPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)
