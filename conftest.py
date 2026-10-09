# import pytest
# import os
# import allure
# from appium import webdriver
# from appium.options.android import UiAutomator2Options


# @pytest.fixture(scope="function")
# def driver():
#     options = UiAutomator2Options()

#     # 🔹 Asosiy sozlamalar
#     options.platform_name = "Android"
#     options.automation_name = "UiAutomator2"
#     options.device_name = "Android"
#     options.udid = "4baa1641"  # sizning telefon ID

#     # 🔹 APK yo‘li
#     apk_path = os.path.abspath(
#         "/home/asilbek/Projects/mobile-appium-tests-main/app/tezpay-debug.apk"
#     )
#     options.app = apk_path
#     options.app_package = "pro.tezpay.app"
#     options.app_activity = "pro.tezpay.app.MainActivity"

#     # 🔹 App sozlamalari
#     options.auto_grant_permissions = True
#     options.no_reset = True          # 🔥 qayta install qilmaydi (MUHIM)
#     options.full_reset = False

#     # 🔹 Timeoutlar (ENG MUHIM)
#     options.set_capability("uiautomator2ServerInstallTimeout", 200000)
#     options.set_capability("adbExecTimeout", 200000)
#     options.set_capability("androidInstallTimeout", 200000)
#     options.set_capability("uiautomator2ServerLaunchTimeout", 60000)
#     options.set_capability("androidDeviceReadyTimeout", 60)
#     options.set_capability("appWaitDuration", 60000)
#     options.set_capability("appWaitActivity", "*")

#     print(f"🚀 Appium sessiyasi boshlanmoqda... APK: {apk_path}")

#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

#     # 🔹 Kutish
#     driver.implicitly_wait(15)

#     yield driver

#     print("🛑 Session yopildi")
#     driver.quit()


# # 📸 Test yiqilsa screenshot olish
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         try:
#             if "driver" in item.funcargs:
#                 driver = item.funcargs["driver"]

#                 allure.attach(
#                     driver.get_screenshot_as_png(),
#                     name="failed_screen",
#                     attachment_type=allure.attachment_type.PNG
#                 )

#                 print("📸 Screenshot olindi (test yiqildi)")

#         except Exception as e:
#             print(f"❌ Screenshot olishda xato: {e}")



import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.device_name = "Android"
    options.udid = "4baa1641"

    options.app = "/home/asilbek/Projects/mobile-appium-tests-main/app/tezpay-debug.apk"
    options.app_package = "pro.tezpay.app"
    options.app_activity = ".MainActivity"

    options.no_reset = False
    options.full_reset = True

    # options.no_reset = True
    # options.auto_grant_permissions = True

    # 🔥 TIMEOUT
    options.set_capability("uiautomator2ServerInstallTimeout", 200000)
    options.set_capability("adbExecTimeout", 200000)
    options.set_capability("androidInstallTimeout", 200000)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(15)

    yield driver

    driver.quit()