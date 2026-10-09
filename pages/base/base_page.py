# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.appiumby import AppiumBy
# import allure
# import os
# import time

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver

#     def wait_visible(self, locator, timeout=30): # CI uchun default 30s
#         try:
#             return WebDriverWait(self.driver, timeout).until(
#                 EC.visibility_of_element_located(locator)
#             )
#         except Exception:
#             self.take_screenshot(f"not_visible_{int(time.time())}")
#             print(f"❌ Ko'rinmadi: {locator} | Activity: {self.driver.current_activity}")
#             raise

#     def wait_clickable(self, locator, timeout=30):
#         try:
#             return WebDriverWait(self.driver, timeout).until(
#                 EC.element_to_be_clickable(locator)
#             )
#         except Exception:
#             print(f"❌ Bosib bo'lmaydi: {locator}")
#             raise

#     def click(self, locator, timeout=30):
#         """CI dagi kechikishlarni hisobga olgan holda qayta urinish bilan bosish"""
#         try:
#             el = self.wait_clickable(locator, timeout)
#             el.click()
#         except Exception:
#             print(f"⚠️ Oddiy click o'xshadi, qayta urinib ko'ramiz...")
#             time.sleep(2) # Kichik pauza
#             el = self.wait_visible(locator, timeout)
#             el.click()

#     def send_keys(self, locator, text, timeout=30):
#         el = self.wait_visible(locator, timeout)
#         el.clear()
#         # Ba'zida CI da send_keys tez ishlab ketadi, sekinlashtirish uchun:
#         for char in text:
#             el.send_keys(char)
#             time.sleep(0.1)

#     def take_screenshot(self, name):
#         os.makedirs("screenshots", exist_ok=True)
#         path = f"screenshots/{name}.png"
#         self.driver.save_screenshot(path)
#         allure.attach.file(path, name=name, attachment_type=allure.attachment_type.PNG)
#         return path


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# class BasePage:

#     def __init__(self, driver):
#         self.driver = driver

#     def find(self, locator):
#         return self.driver.find_element(*locator)

#     def click(self, locator, timeout=10):
#         el = WebDriverWait(self.driver, timeout).until(
#             EC.element_to_be_clickable(locator)
#         )
#         el.click()

#     def send_keys(self, locator, text, timeout=10):
#         el = WebDriverWait(self.driver, timeout).until(
#             EC.visibility_of_element_located(locator)
#         )
#         el.click()
#         el.clear()
#         el.send_keys(text)

#     def get_text(self, locator, timeout=10):
#         el = WebDriverWait(self.driver, timeout).until(
#             EC.visibility_of_element_located(locator)
#         )
#         return el.text

# pages/base/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import allure
import os
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=30):
        return self.wait_visible(locator, timeout)

    def find_elements(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except Exception:
            self.take_screenshot(f"not_found_{int(time.time())}")
            print(f"❌ Elementlar topilmadi: {locator}")
            raise

    def wait_visible(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception:
            self.take_screenshot(f"not_visible_{int(time.time())}")
            print(f"❌ Ko'rinmadi: {locator} | Activity: {self.driver.current_activity}")
            raise

    def wait_clickable(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception:
            print(f"❌ Bosib bo'lmaydi: {locator}")
            raise

    def click(self, locator, timeout=30):
        try:
            el = self.wait_clickable(locator, timeout)
            el.click()
        except Exception:
            print(f"⚠️ Oddiy click o'xshadi, qayta urinib ko'ramiz...")
            time.sleep(2)
            el = self.wait_visible(locator, timeout)
            el.click()

    def send_keys(self, locator, text, timeout=30):
        el = self.wait_visible(locator, timeout)
        el.clear()
        for char in text:
            el.send_keys(char)
            time.sleep(0.1)

    def take_screenshot(self, name):
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{name}.png"
        self.driver.save_screenshot(path)
        allure.attach.file(path, name=name, attachment_type=allure.attachment_type.PNG)
        return path