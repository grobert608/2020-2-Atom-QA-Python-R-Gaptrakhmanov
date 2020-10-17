from selenium.webdriver.common.by import By


class BaseLocators:
    HOME = (By.XPATH, '//a[ @ href = "//target.my.com"]')
    SEGMENTS = (By.XPATH, '//a[@href="/segments"]')


class AuthPageLocators(BaseLocators):
    LOGIN_BUTTON = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOGIN_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    CONFIRM_LOGIN = (By.XPATH, '//div[contains(@class,"authForm-module-button")] ')


class CampaignsLocators(BaseLocators):

    @staticmethod
    def USER_TITLE(username):
        return By.XPATH, '//div[contains(@title,"{}")]'.format(username)

    @staticmethod
    def CAMPAIGN_NAME(name):
        return By.XPATH, '//a[@title="{}"]'.format(name)

    CREATE_CAMPAIGN_EMPTY = (
        By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div')
    CREATE_CAMPAIGN_NOT_EMPTY = (By.XPATH,
                                 '//a[@class="campaigns-tbl-settings__button campaigns-tbl-settings__button_new" and'
                                 ' @href="/campaign/new"]')
    INVALID_LOGIN_TRY_EMAIL = (By.XPATH, '//div[contains(text(), "Введите email или телефон")]')


class NewCampaignsLocators(BaseLocators):
    TRAFFIC = (By.XPATH, '//div[contains(text(), "Трафик")]')
    LINK_FIELD = (By.XPATH,
                  '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')
    CLEAR_NAME_BUTTON = (By.XPATH,
                         '//div[contains(@class,"campaign-name")]//div[contains(@class,"input__clear js-input-clear")]')
    NAME_FIELD = (By.XPATH, '//div[contains(@class,"campaign-name")]//input')

    SEX_FIELD = (By.XPATH, '//span[contains(text(), "Мужчины, Женщины")]')
    MALE_CHECKBOX = (By.XPATH, '//input[@targeting="sex-male"]')
    FEMALE_CHECKBOX = (By.XPATH, '//input[@targeting="sex-female"]')

    AGE_FIELD = (By.XPATH, '//div[@data-scroll-name="setting-age"]')
    AGE_CHOICE = (By.XPATH,
                  '//div[@class="age-setting"]//div[@class="select__item select__item_value js-select-button"]')
    RANDOM_AGE = (By.XPATH,
                  '//span[@class="select-item__text js-list-item-text"  and contains(text(), "Произвольный набор")]')
    AGE_INPUT = (By.XPATH, '//div[@class="age-setting__text js-age-setting-text"]//textarea')

    FORMAT_TEASER = (By.XPATH, '//div[@id="149"]')

    BANNER_TITLE = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')
    BANNER_TEXT = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')
    UPLOAD_FILE = (By.XPATH, '//div[contains(@class,"banner-form")]//input[@type="file"]')
    SAVE_FILE = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')

    ADD_ADVERT = (By.XPATH, '//div[contains(text(), "Добавить объявление")]')
    CONFIRM_CREATING = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')


class InvalidAuthLocators:
    INVALID_LOGIN = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class SegmentsLocators(BaseLocators):
    VK_GROUPS = (By.XPATH, '//a[@href="/segments/groups_list"]')

    CREATE_SEGMENT_EMPTY = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    CREATE_SEGMENT_NOT_EMPTY = (By.XPATH, '//div[contains(text(),"Создать сегмент")]')

    @staticmethod
    def SEGMENT_NAME(name):
        return By.XPATH, '//a[@title="{}"]'.format(name)

    SORT_BY_ID = (By.XPATH, '//th[@data-group-id="id" and @class="flexi-table__header-th"]')
    DELETE = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[6]/span')
    CONFIRM_DELETE = (By.XPATH, '//div[contains(text(),"Удалить")]')


class NewSegmentsLocators(BaseLocators):
    VK_DATA = (By.XPATH, '//div[@class="adding-segments-item" and contains(text(),"VK")]')
    CHOICE_GROUP = (By.XPATH,
                    '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    ADD_SEGMENT = (By.XPATH, '//div[contains(text(),"Добавить сегмент")]')
    NAME_FIELD = (By.XPATH, '//div[@class="js-segment-name"]//input')
    CONFIRM_CREATING = (By.XPATH, '//div[contains(text(),"Создать сегмент")]')


class VkGroupsLocators(BaseLocators):
    LINK_FIELD = (By.XPATH, '//div[@class="multiSelectSuggester-module-wrapper-1bpXA5"]//input')
    SHOW_ALL = (By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div[2]/div[1]')
    CHOICE_FIRST_GROUP = (By.XPATH, '/html/body/div[6]/div/div/div[2]/ul/li[1]')
    ADD_GROUP = (By.XPATH, '/html/body/div[6]/div/div/div[3]/div/div')

    @staticmethod
    def GROUP_NAME_IN_TABLE(name):
        return By.XPATH, '//tr[@class="flexi-table__row"]/td[@data-id="name"]//span[contains(text(), "{}")]'.format(name)
