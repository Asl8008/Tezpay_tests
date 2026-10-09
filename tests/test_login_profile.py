import allure
from pages.prelogin.language_page import LanguagePage
from pages.prelogin.onboarding_page import OnboardingPage
from pages.auth.login_page import LoginPage
from pages.auth.otp_page import OtpPage
from pages.home.home_page import HomePage
from pages.profile.profile_page import ProfilePage

@allure.feature("Smoke")
def test_login_and_profile(driver):
    LanguagePage(driver).pass_language()
    OnboardingPage(driver).pass_onboarding()

    LoginPage(driver).login("9692803381")
    OtpPage(driver).enter_otp_and_pin("111111")

    home = HomePage(driver)
    home.wait_home()

    profile = ProfilePage(driver)
    profile.open_profile()

    # profile.change_language_cyr_to_lat()
    # profile.change_language_lat_to_cyr()

    # profile.change_theme()
    profile.change_pin()
    profile.open_limits()