from urllib.parse import urljoin

import requests


class VkClient:
    def __init__(self, url):
        self.base_url = url
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, redirect=False):
        url = urljoin(self.base_url, location)
        return self.session.request(method, url, headers=headers, data=data, allow_redirects=redirect)

    def add_user(self, user, vk_id):
        location = '/add'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': user,
            'vk_id': vk_id
        }

        response = self._request('POST', location, data=data, headers=headers)
        return response.status_code

    def get_user(self, user):
        location = '/vk_id/{}'.format(user)

        response = self._request('GET', location)
        return response.status_code

    def del_user(self, user):
        location = '/del_user/{}'.format(user)

        response = self._request('GET', location)
        return response.status_code
