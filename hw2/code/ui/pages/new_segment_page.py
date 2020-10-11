from ui.locators.locators import NewSegmentsLocators
from ui.pages.base_page import BasePage


class NewSegmentsPage(BasePage):
    locators = NewSegmentsLocators()

    def create_segment(self, segment_name):
        from ui.pages.segments_page import SegmentsPage
        self.click(self.locators.VK_DATA)
        self.click(self.locators.CHOICE_GROUP)
        self.click(self.locators.ADD_SEGMENT)
        self.find(self.locators.NAME_FIELD).clear()
        self.find(self.locators.NAME_FIELD).send_keys(segment_name)
        self.click(self.locators.CONFIRM_CREATING)
        return SegmentsPage(self.driver, self.config)
