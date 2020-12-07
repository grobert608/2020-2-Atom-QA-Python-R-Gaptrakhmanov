import allure

from conftest import *
from db_orm.builder import MysqlOrmBuilder
from tests.base import BaseCase
from ui.pages.registration_page import RegistrationPage
from ui.pages.welcome_page import WelcomePage


class TestRegistration(BaseCase):
    faker = Faker()

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_positive_registration(self, correct_username):
        reg_page = self.main_page.to_registration()
        assert isinstance(
            reg_page.registration(correct_username, self.faker.email(), 1, 1),
            WelcomePage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_positive_registration',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_without_sdet(self, correct_username):
        reg_page = self.main_page.to_registration()
        assert isinstance(reg_page.registration(correct_username, self.faker.email(), 1, 1, sdet=False), RegistrationPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_without_sdet',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_without_name(self):
        reg_page = self.main_page.to_registration()
        assert isinstance(reg_page.registration("", self.faker.email(), 1, 1), RegistrationPage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_without_name',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    @pytest.mark.parametrize("username",
                             [str(i) * i for i in range(1, 6)])
    def test_registration_with_shortname(self, username):
        reg_page = self.main_page.to_registration()
        reg_page.registration(username, self.faker.email(), 1, 1).find(reg_page.locators.INCORRECT_USERNAME_LENGTH)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_with_shortname_{}'.format(username),
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_with_longname(self):
        reg_page = self.main_page.to_registration()
        reg_page.registration('12345678912345678', self.faker.email(), 1, 1).find(
            reg_page.locators.INCORRECT_USERNAME_LENGTH)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_with_longname',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_with_cyrillic_name(self):
        fake = Faker('ru_RU')
        reg_page = self.main_page.to_registration()
        assert isinstance(
            reg_page.registration(fake.last_name(), self.faker.email(), 1, 1),
            WelcomePage)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_with_cyrillic_name',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    @pytest.mark.parametrize("email",
                             ['simple@example.com', 'very.common@example.com',
                              'disposable.style.email.with+symbol@example.com',
                              'other.email-with-hyphen@example.com', 'fully-qualified-domain@example.com',
                              'user.name+tag+sorting@example.com', 'x@example.com',
                              'example-indeed@strange-example.com', 'example@s.example', 'java..best@example.org',
                              'mailhost!username@example.org', 'user%example.com@example.org'])
    def test_correct_email(self, email, mysql_orm_client, correct_username):
        reg_page = self.main_page.to_registration()
        try:
            assert isinstance(reg_page.registration(correct_username, email, 1, 1), WelcomePage)
        except AssertionError as err:
            raise AssertionError(err, email)
        finally:
            builder = MysqlOrmBuilder(mysql_orm_client)
            builder.delete_user_by_email(email)
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name='/registration/test_correct_email_{}'.format(email),
                          attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    @pytest.mark.parametrize("email",
                             ['Abc.example.com', 'A@b@c@example.com', 'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
                              '1234567890123456789012345678901234567890123456789012345678901234+x@example.com'])
    def test_incorrect_email(self, email, mysql_orm_client, correct_username):
        reg_page = self.main_page.to_registration()
        try:
            assert isinstance(reg_page.registration(correct_username, email, 1, 1), RegistrationPage)
        except AssertionError as err:
            raise AssertionError(err, email)
        finally:
            builder = MysqlOrmBuilder(mysql_orm_client)
            builder.delete_user_by_email(email)
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name='/registration/est_incorrect_email_{}'.format(email),
                          attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_without_email(self, correct_username):
        reg_page = self.main_page.to_registration()
        reg_page.registration(correct_username, "", 1, 1).find(reg_page.locators.INCORRECT_EMAIL_LENGTH)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_without_email',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_with_different_passwords(self, correct_username):
        reg_page = self.main_page.to_registration()
        reg_page.registration(correct_username, self.faker.email(), 1, 2).find(reg_page.locators.DIFFERENT_PASSWORDS)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_with_different_passwords',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_with_few_errors(self):
        reg_page = self.main_page.to_registration()
        result_page = reg_page.registration('12345678912345678', self.faker.email(), 1, 2)
        assert result_page.find(reg_page.locators.DIFFERENT_PASSWORDS) == \
               result_page.find(reg_page.locators.INCORRECT_USERNAME_LENGTH)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_with_few_errors',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_without_password(self, correct_username):
        reg_page = self.main_page.to_registration()
        assert isinstance(
            reg_page.registration(correct_username, self.faker.email(), "", 1), RegistrationPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_without_password',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('registration')
    @pytest.mark.UI_REG
    def test_registration_existing_user(self, config, add_user):
        name, email = add_user
        reg_page = self.main_page.to_registration()
        reg_page.registration(name, email,
                              config['default_password'], config['default_password']).find(reg_page.locators.USER_ALREADY_EXIST)
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)
