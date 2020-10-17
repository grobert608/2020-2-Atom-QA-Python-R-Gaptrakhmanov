from ui.locators.locators import CampaignsLocators
from .base_page import BasePage


class MainPage(BasePage):
    locators = CampaignsLocators()

    def go_to_create_campaign(self):
        from .new_campaign_page import NewCampaignsPage

        try:
            self.click(self.locators.CREATE_CAMPAIGN_EMPTY, 20)
        except Exception:
            self.click(self.locators.CREATE_CAMPAIGN_NOT_EMPTY, 20)
        return NewCampaignsPage(self.driver, self.config)
