import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class OtpPage(BasePage):

    OTP_FIELDS = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    CONTINUE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Давом этиш"
    )

    def enter_otp_and_pin(self, otp):
        # Birinchi katak paydo bo'lishini kutamiz
        self.wait_visible(self.OTP_FIELDS)
        time.sleep(1)

        fields = self.find_elements(self.OTP_FIELDS)

        if len(fields) < 6:
            raise Exception(f"OTP kataklar topilmadi, topildi: {len(fields)} ta")

        for i in range(6):
            fields[i].click()
            time.sleep(0.2)
            fields[i].send_keys(otp[i])
            time.sleep(0.3)

        time.sleep(1)
        self.click(self.CONTINUE)