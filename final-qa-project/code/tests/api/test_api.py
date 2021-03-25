import allure

from api.fixtures import *
from conftest import *


class TestApi:

    def correct_username(self):
        faker = Faker()
        username = faker.profile(fields=['username'])['username']
        while len(username) < 6 or len(username) > 16:
            username = faker.profile(fields=['username'])['username']
        return username

    faker = Faker()

    def clear_db(self, mysql_orm_client, username='1'):
        builder = MysqlOrmBuilder(mysql_orm_client)
        builder.delete_user_by_username(username)

    @allure.feature('API')
    @pytest.mark.API
    def test_status(self, api_client):
        assert api_client.check_status() == 200

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_login(self, api_client, config, add_user):
        name, email = add_user
        assert api_client.code_after_auth(name, config['default_password']) == 302

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_login(self, api_client):
        assert api_client.code_after_auth("12345678", '1') == 401

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_registration(self, api_client, correct_username):
        assert api_client.registration(correct_username, self.faker.email(), 1, 1).status_code == 409

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_registration(self, api_client):
        assert api_client.registration(self.correct_username(), self.faker.email(), 1, 1).status_code == 302

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_add_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        correct_username = self.correct_username()

        try:
            assert api_client.add_user(correct_username, self.faker.email(), 1).status_code == 201
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, correct_username)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_add_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            assert api_client.add_user(current_name, current_email, 1).status_code == 304
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_add_user_db(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, 1, current_email)
        try:
            query_res = mysql_orm_client.session.query(User.email, User.username).filter_by(username=current_name).all()
            assert len(query_res) == 1
            assert query_res[0][1] == current_name
            assert query_res[0][0] == current_email
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_del_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            assert api_client.del_user(current_name).status_code == 204
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_del_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()

        try:
            assert api_client.del_user(current_name).status_code == 404
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_del_user_db(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            api_client.del_user(current_name)
            query_res = mysql_orm_client.session.query(User.email).filter_by(username=current_name).all()
            assert len(query_res) == 0
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_block_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            assert api_client.block_user(current_name).status_code == 200
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_unblock_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        api_client.block_user(current_name)
        try:
            assert api_client.block_user(current_name).status_code == 304
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_block_nonexistent_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()

        try:
            assert api_client.block_user(current_name).status_code == 404
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_block_user_db(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            before_block = mysql_orm_client.session.query(User.access).filter_by(username=current_name).all()[0][0]
            api_client.block_user(current_name)
            after_block = mysql_orm_client.session.query(User.access).filter_by(username=current_name).all()[0][0]
            assert before_block == 1
            assert after_block == 0
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_unblock_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        api_client.block_user(current_name)
        try:
            assert api_client.unblock_user(current_name).status_code == 200
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_unblock_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            assert api_client.unblock_user(current_name).status_code == 304
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_negative_unblock_nonexistent_user_response_code(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()

        try:
            assert api_client.unblock_user(current_name).status_code == 404
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_unblock_user_db(self, api_client, mysql_orm_client):
        api_client.login()
        current_name = self.correct_username()
        current_email = self.faker.email()

        api_client.add_user(current_name, current_email, 1)
        try:
            api_client.block_user(current_name)
            before_unblock = mysql_orm_client.session.query(User.access).filter_by(username=current_name).all()[0][0]

            api_client.unblock_user(current_name)
            after_unblock = mysql_orm_client.session.query(User.access).filter_by(username=current_name).all()[0][0]

            assert before_unblock == 0
            assert after_unblock == 1
        except AssertionError as err:
            raise err
        finally:
            self.clear_db(mysql_orm_client, current_name)

    @allure.feature('API')
    @pytest.mark.API
    def test_positive_logout(self, api_client, mysql_orm_client, correct_username):
        api_client.login()

        try:
            before_logout = mysql_orm_client.session.query(User.active).filter_by(username=correct_username).all()[0][0]
            api_client.logout()
            after_logout = mysql_orm_client.session.query(User.active).filter_by(username=correct_username).all()[0][0]

            assert before_logout == 1
            assert after_logout == 0

        except AssertionError as err:
            raise err
