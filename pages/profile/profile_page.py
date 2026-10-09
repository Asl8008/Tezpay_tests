import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class ProfilePage(BasePage):

    # -------- Profile --------
    PROFILE_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.ImageView").instance(0)'
    )

    # # -------- Language --------
    # LANGUAGE_CYR = (AppiumBy.ACCESSIBILITY_ID, "Тил\nЎзбек кирилл")
    # LANGUAGE_LAT = (AppiumBy.ACCESSIBILITY_ID, "Til\nO'zbek lotin")

    # OPT_LAT = (
    #     AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiSelector().textContains("O\'zbek")'
    # )
    # OPT_CYR = (
    #     AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiSelector().textContains("Ўзбек")'
    # )

    # -------- Theme --------
    THEME_LIGHT = (AppiumBy.ACCESSIBILITY_ID, "Мавзу\nЁрқин")
    THEME_DARK = (AppiumBy.ACCESSIBILITY_ID, "Мавзу\nҚора")

    OPT_DARK = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Қора")'
    )
    OPT_SYSTEM = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Тизим")'
    )

    # -------- Security --------
    SECURITY = (AppiumBy.ACCESSIBILITY_ID, "Хавфсизлик")
    CHANGE_PIN = (AppiumBy.ACCESSIBILITY_ID, "ПИН-кодни ўзгартириш")

    # -------- Limits --------
    LIMITS = (AppiumBy.ACCESSIBILITY_ID, "Лимитлар")

    # ================= METHODS =================

    def open_profile(self):
        self.click(self.PROFILE_ICON)
        time.sleep(1)
    #
    # def change_language_cyr_to_lat(self):
    #     self.click(self.LANGUAGE_CYR)
    #     self.wait_visible(self.OPT_LAT, timeout=15)
    #     self.click(self.OPT_LAT)
    #
    # def change_language_lat_to_cyr(self):
    #     self.click(self.LANGUAGE_LAT)
    #     self.wait_visible(self.OPT_CYR, timeout=15)
    #     self.click(self.OPT_CYR)

    def change_theme(self):
        self.click(self.THEME_LIGHT)
        self.wait_visible(self.OPT_DARK)
        self.click(self.OPT_DARK)

        self.click(self.THEME_DARK)
        self.wait_visible(self.OPT_SYSTEM)
        self.click(self.OPT_SYSTEM)

    def change_pin(self):
        self.click(self.SECURITY)
        self.click(self.CHANGE_PIN)

        for code in ["5555", "5555", "0000", "5555"]:
            for d in code:
                self.click((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().description("{d}")'
                ))

        self.driver.back()

    def open_limits(self):
        self.click(self.LIMITS)
        self.driver.back()
