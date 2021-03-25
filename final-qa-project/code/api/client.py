import json
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


class Client:
    def __init__(self, user, password):
        self.base_url = 'http://192.168.0.64:8083/'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.headers = None


    def _request(self, method, location, headers=None, data=None, redirect=False):
        url = urljoin(self.base_url, location)
        return self.session.request(method, url, headers=headers, data=data, allow_redirects=redirect)

    def check_status(self):
        location = 'status'
        response = self._request('GET', location)
        return response.status_code

    def code_after_auth(self, user, password):
        location = 'login'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1'
        }
        data = {
            'username': user,
            'password': password,
            'submit': 'Login'
        }

        response = self._request('POST', location, data=data, headers=headers)
        return response.status_code

    def login(self):
        location = 'login'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1'
        }
        data = {
            'username': self.user,
            'password': self.password,
            'submit': 'Login'
        }

        response = self._request('POST', location, headers=headers, data=data)
        cookies = response.headers['Set-Cookie'].split(';')
        session_token = [c for c in cookies if c.startswith('session=')][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({'session': session_token})
        return response

    def registration(self, user, email, password, confirm_password):
        location = 'reg'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://192.168.0.64:8083/reg',
            'Upgrade-Insecure-Requests': '1'
        }
        data = {
            'username': user,
            'email': email,
            'password': password,
            'confirm': password,
            'term': confirm_password,
            'submit': 'Reg'
        }

        return self._request('POST', location, headers=headers, data=data)

    def add_user(self, username, password, email):
        location = 'api/add_user'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "username": username,
            "password": password,
            "email": email
        }

        return self._request('POST', location, headers=headers, data=json.dumps(data))

    def del_user(self, username):
        location = 'api/del_user/{}'.format(username)

        return self._request('GET', location)

    def block_user(self, username):
        location = 'api/block_user/{}'.format(username)

        return self._request('GET', location)

    def unblock_user(self, username):
        location = 'api/accept_user/{}'.format(username)

        return self._request('GET', location)

    def logout(self):
        location = 'logout'

        return self._request('GET', location)