from conftest import *
from tests.base import BaseCase
from time import sleep


class Test(BaseCase):

    @pytest.mark.UI
    def test_positive_login_with_fixture(self, login):
        page_after_login = login
        page_after_login.find(page_after_login.locators.USER_TITLE(self.config['username']))

    @pytest.mark.UI
    def test_negative_login(self):
        page_after_login = self.main_page.login("python", "123456")
        page_after_login.find(page_after_login.locators.INVALID_LOGIN_TRY_EMAIL)

    @pytest.mark.UI
    def test_create_campaign(self, login):
        link = "https://10minutemail.com/"
        name = "campaign for {}".format(link)

        page_after_login = login
        creation_page = page_after_login.go_to_create_campaign()
        page_with_campaign = creation_page.create_campaign(link, name)
        sleep(3)
        page_with_campaign.find(page_after_login.locators.CAMPAIGN_NAME(name)).is_displayed()

    @pytest.mark.UI
    def test_create_segment(self, login):
        group_name = "Forbes"
        segment_name = "newSegment"

        page_after_login = login
        vk_groups_page = page_after_login.go_to_segments().go_to_vk_groups()
        vk_groups_page.add_group(group_name)

        creation_page = vk_groups_page.go_to_segments().go_to_create_segment()
        page_with_segment = creation_page.create_segment(segment_name)
        sleep(3)
        page_with_segment.find(page_with_segment.locators.SEGMENT_NAME(segment_name)).is_displayed()

    @pytest.mark.UI
    def test_delete_segment(self, login):
        group_name = "Forbes"
        segment_name = "newSegmentToDelete"

        page_after_login = login
        vk_groups_page = page_after_login.go_to_segments().go_to_vk_groups()
        vk_groups_page.add_group(group_name)

        creation_page = vk_groups_page.go_to_segments().go_to_create_segment()
        page_with_segment = creation_page.create_segment(segment_name)
        sleep(3)
        page_with_segment.find(page_with_segment.locators.SEGMENT_NAME(segment_name)).is_displayed()

        cnt_before = page_with_segment.count_elements(page_with_segment.locators.SEGMENT_NAME(segment_name))

        page_with_segment.click(page_with_segment.locators.DELETE)
        page_with_segment.click(page_with_segment.locators.CONFIRM_DELETE, 15)

        sleep(3)

        cnt_after = page_with_segment.count_elements(page_with_segment.locators.SEGMENT_NAME(segment_name))

        assert cnt_after == cnt_before - 1
