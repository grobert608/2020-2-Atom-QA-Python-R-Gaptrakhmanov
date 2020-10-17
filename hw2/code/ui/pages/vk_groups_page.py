from ui.locators.locators import VkGroupsLocators
from .base_page import BasePage

class VkGroupsPage(BasePage):
    locators = VkGroupsLocators()

    def add_group(self, name):
        self.find(self.locators.LINK_FIELD).send_keys(name)
        self.click(self.locators.SHOW_ALL)
        self.click(self.locators.CHOICE_FIRST_GROUP)
        self.click(self.locators.ADD_GROUP)
        self.find(self.locators.GROUP_NAME_IN_TABLE(name))
