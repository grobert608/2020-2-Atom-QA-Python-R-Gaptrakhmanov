import pytest

from api.apiclient import ApiClient


@pytest.fixture(scope='function')
def api_client(config):
    return ApiClient(config['url'], config['username'], config['password'])


@pytest.fixture(scope='function')
def segment():
    return {
        'name': 'newAPISegment',
        'relations_count': 1,
        'pass_condition': 1,
        "relations": [{"object_id": 2445950, "object_type": "remarketing_vk_group",
                       "params": {"type": "positive", "source_id": 11982368}}]
    }
