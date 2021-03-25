from ui.locators.locators import WelcomeLocators
from ui.pages.base_page import BasePage
from ui.pages.web_instances import ApiPage, SmtpPage, PopularMechanicsPage, PythonPage, PythonHistoryPage, \
    AboutFlaskPage, DownloadCentosPage, WiresharkDownloadPage, WiresharkNewsPage, TCPDumpExamplesPage


class WelcomePage(BasePage):
    locators = WelcomeLocators

    def to_whatIsAnApi(self):
        self.click(self.locators.WHAT_IS_AN_API)
        return ApiPage(self.driver, self.config)

    def to_futureOfInternet(self):
        self.click(self.locators.FUTURE_OF_INTERNET)
        return PopularMechanicsPage(self.driver, self.config)

    def to_letsTalkAboutSmtp(self):
        self.click(self.locators.LETS_TALK_ABOUT_SMTP)
        return SmtpPage(self.driver, self.config)

    def to_python(self):
        self.click(self.locators.PYTHON)
        return PythonPage(self.driver, self.config)

    def to_pythonHistory(self):
        self.move_to_element(self.locators.PYTHON)
        self.click(self.locators.PYTHON_HISTORY)
        return PythonHistoryPage(self.driver, self.config)

    def to_aboutFlask(self):
        self.move_to_element(self.locators.PYTHON)
        self.click(self.locators.ABOUT_FLASK)
        return AboutFlaskPage(self.driver, self.config)

    def to_downloadCentos(self):
        self.move_to_element(self.locators.LINUX)
        self.click(self.locators.DOWNLOAD_CENTOS)
        return DownloadCentosPage(self.driver, self.config)

    def to_wiresharkNews(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.WIRESHARK_NEWS)
        return WiresharkNewsPage(self.driver, self.config)

    def to_wiresharkDownload(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.WIRESHARK_DOWNLOAD)
        return WiresharkDownloadPage(self.driver, self.config)

    def to_tcpdumpExamples(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.TCPDUMP_EXAMPLES)
        return TCPDumpExamplesPage(self.driver, self.config)

    def logout(self):
        from ui.pages.main_page import MainPage
        self.click(self.locators.LOGOUT)
        return MainPage(self.driver, self.config)
