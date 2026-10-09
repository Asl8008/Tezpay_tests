from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class HomePage(BasePage):

    HOME_INDICATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Тўлов")'
    )

    def wait_home(self):
        self.wait_visible(self.HOME_INDICATOR)
