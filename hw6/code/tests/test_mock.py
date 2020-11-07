import time

import pytest
import requests


class TestMock:
    @pytest.fixture(autouse=True)
    def setup_class(self, mock, socket_client):
        self.client = socket_client

    def test_fake_mock(self):
        self.client.connect()
        self.client.get('/fake_mock')
        result = self.client.receive()
        assert result['status_code'] == 500
        self.client.disconnect()

    def test_timeout(self):
        self.client.connect()
        self.client.get('/timeout')
        result = self.client.receive()
        time.sleep(1)
        assert result['status_code'] == 408
        self.client.disconnect()

    def test_500(self):
        self.client.connect()
        self.client.get('/errorfzz')
        result = self.client.receive()
        assert result['status_code'] == 500
        self.client.disconnect()

    def test_auth_header_success(self):
        response = requests.get('http://127.0.0.1:5001/auth', headers={'Authorization': 'Rob'})
        assert response.status_code == 200

    def test_auth_header_unsuccess(self):
        response = requests.get('http://127.0.0.1:5001/auth', headers={'Authorization': 'Max'})
        assert response.status_code == 403

    def test_auth_no_header(self):
        response = requests.get('http://127.0.0.1:5001/auth')
        assert response.status_code == 400
