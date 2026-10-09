from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class LanguagePage(BasePage):

    CONTINUE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Давом этиш")'
    )

    def pass_language(self):
        self.click(self.CONTINUE)
