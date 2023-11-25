from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver

    # Locators
    ACCEPT_COOKIES = "onetrust-accept-btn-handler"
    GENIUS_CLOSE = "//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561']"
    FLIGHTS_TAB_BUTTON = "//a[@id='flights']"
    LANGUAGE_PICKER = "//button[@data-testid='header-language-picker-trigger']"
    ENGLISH_UK = "//span[@class='cf67405157'][text()='English (UK)']"

    def get_accept_cookies_button(self):
        return self.wait_until_element_is_clickable(By.ID, self.ACCEPT_COOKIES)

    def get_genius_close_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GENIUS_CLOSE)

    def get_flights_tab_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FLIGHTS_TAB_BUTTON)

    def get_pick_language_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LANGUAGE_PICKER)

    def get_english_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ENGLISH_UK)

    def accept_cookies(self):
        self.get_accept_cookies_button().click()

    def genius_close(self):
        try:
            self.get_genius_close_button().click()
        except TimeoutException:
            pass

    def set_language(self):
        self.get_pick_language_button().click()
        self.get_english_button().click()

    def click_flights(self):
        self.get_flights_tab_button().click()
