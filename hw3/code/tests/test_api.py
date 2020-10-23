import pytest


class TestApi:
    @pytest.mark.API
    def test_create_segment(self, api_client, segment):
        api_client.login()
        seg = api_client.create(segment)
        id = seg.json()['id']
        assert seg.status_code == 200
        assert api_client.find_by_id(id) is not None

    @pytest.mark.API
    def test_delete_segment(self, api_client, segment):
        api_client.login()
        id = api_client.create(segment).json()['id']
        assert api_client.delete(id) == 204
        assert api_client.find_by_id(id) is None
