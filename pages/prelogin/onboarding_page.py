from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class OnboardingPage(BasePage):

    CONTINUE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Давом этиш")'
    )

    def pass_onboarding(self, times=3):
        for _ in range(times):
            self.click(self.CONTINUE)
