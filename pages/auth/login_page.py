# from appium.webdriver.common.appiumby import AppiumBy
# from pages.base.base_page import BasePage


# class LoginPage(BasePage):

#     # PHONE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     CONTINUE = (
#         AppiumBy.ANDROID_UIAUTOMATOR,
#         'new UiSelector().description("Давом этиш")'
#     )

#     def login(self, phone):
#         # self.send_keys(self.PHONE_INPUT, phone)
#         self.click(self.CONTINUE)


#     print(driver.page_source)

# from appium.webdriver.common.appiumby import AppiumBy
# from pages.base.base_page import BasePage


# class LoginPage(BasePage):

#     # 🔥 inputni aniqroq topamiz (EditText bo‘yicha)
#     PHONE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

#     CONTINUE = (
#         AppiumBy.ANDROID_UIAUTOMATOR,
#         'new UiSelector().description("Давом этиш")'
#     )

#     def login(self, phone):
#         print("📱 Login boshlandi")
#         print(self.driver.page_source)  # debug

#         # 🔥 inputni topamiz
#         inputs = self.driver.find_elements(*self.PHONE_INPUT)

#         if not inputs:
#             raise Exception("❌ Input topilmadi!")

#         # 🔥 birinchi inputni olamiz
#         phone_input = inputs[0]

#         phone_input.click()
#         phone_input.clear()
#         phone_input.send_keys(phone)

#         print(f"✅ Telefon yozildi: {phone}")

#         # 🔥 davom etish tugmasi
#         self.click(self.CONTINUE)

# pages/auth/login_page.py

import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class LoginPage(BasePage):

    PHONE_INPUT = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    CONTINUE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Давом этиш"
    )

    def login(self, phone):
        el = self.find_element(self.PHONE_INPUT)

        el.click()

        for digit in phone:
            el.send_keys(digit)
            time.sleep(0.2)

        self.click(self.CONTINUE)