import pytest
import json
import requests


class TestServerClient:

    @pytest.fixture(autouse=True)
    def setup_class(self, socket_client_mock, mock_server, config):
        self.client = socket_client_mock
        self.mock = mock_server
        self.url = f'http://{config["mock_host"]}:{config["mock_port"]}'

    def test_get_server(self):
        info = {'company': 'BMW', 'car': 'X5'}
        self.mock.set_data(info)
        response = requests.get(self.url)
        result = json.loads(response.content.decode())
        assert response.status_code == 200
        assert result == info

    def test_get_client(self):
        info = {'company': 'BMW', 'car': 'X5'}
        self.mock.set_data(info)
        self.client.connect()
        self.client.get(self.url)
        result = self.client.receive()
        assert result['status_code'] == 200
        assert result['data'] == info
        self.client.disconnect()

    def test_post_server(self):
        info = {'company': 'BMW', 'car': 'X5'}
        response = requests.post(self.url, json.dumps(info))
        result = json.loads(response.content.decode())
        assert response.status_code == 200
        assert result == info

    def test_post_client(self):
        info = {'company': 'BMW', 'car': 'X5'}
        self.client.connect()
        self.client.post(self.url, json.dumps(info))
        result = self.client.receive()
        assert result['status_code'] == 200
        assert result['data'] == info
        self.client.disconnect()

    def test_put_server(self):
        info = {'company': 'BMW', 'car': 'X5'}
        response = requests.put(self.url, json.dumps(info))
        result = json.loads(response.content.decode())
        assert response.status_code == 200
        assert result == info
