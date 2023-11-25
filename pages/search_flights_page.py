from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.my_calendar import get_dates


def get_date_locators(date):
    return f"//span[@data-date='{date}']"


class FlightsPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators
    PASSENGERS_OPTIONS = "//button[@data-ui-name='button_occupancy']"
    ADULTS_NUMBER_PLUS = "//button[@data-ui-name='button_occupancy_adults_plus']"
    CONFIRM_PASSENGERS = "//button[@data-ui-name='button_occupancy_action_bar_done']"
    LOCATION_FROM_BUTTON = "//button[@class='css-1ovag24'][1]"
    DEFAULT_LOCATION_FROM = "//span[@class='css-rh2lq6']"
    LOCATION_FROM_FIELD = "//input[@class='css-x72e3o ']"
    LOCATION_FROM_SEARCH_RESULTS = "//ul[@id='flights-searchbox_suggestions']//li//span[@class='css-3cj1dx']//span"
    LOCATION_TO_BUTTON = "//button[@class='css-1ovag24'][2]"
    LOCATION_TO_FIELD = "//input[@class='css-x72e3o ']"
    LOCATION_TO_SEARCH_RESULTS = "//ul[@id='flights-searchbox_suggestions']//li//span[@class='css-3cj1dx']//span"
    CALENDAR_BUTTON = "//div[@class='css-8atqhb']//button[@class='css-1ovag24']"
    CALENDAR_LEFT_DAYS = ("//div[@class='Calendar-module__monthWrapper___6FH+y'][1]//table["
                          "@class='Calendar-module__dates___kYFZ9']//tbody//tr//td[@role='gridcell']//span//span//span")
    CALENDAR_NEXT_MONTH = "//div[@data-ui-name='calendar_body']//button[2]"
    CALENDAR_RIGHT_DAYS = ("//div[@class='Calendar-module__monthWrapper___6FH+y'][2]//table["
                           "@class='Calendar-module__dates___kYFZ9']//tbody//tr//td["
                           "@role='gridcell']//span//span//span")
    SEARCH_BUTTON = "//button[@data-ui-name='button_search_submit']"

    def get_location_from_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOCATION_FROM_BUTTON)

    def get_default_location_from(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEFAULT_LOCATION_FROM)

    def get_location_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOCATION_FROM_FIELD)

    def get_location_from_search_results(self):
        return self.wait_until_presence_of_all_elements_located(By.XPATH, self.LOCATION_FROM_SEARCH_RESULTS)

    def get_location_to_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOCATION_TO_BUTTON)

    def get_location_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOCATION_TO_FIELD)

    def get_location_to_search_results(self):
        return self.wait_until_presence_of_all_elements_located(By.XPATH, self.LOCATION_TO_SEARCH_RESULTS)

    def get_calendar_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CALENDAR_BUTTON)

    def get_calendar_next_month(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CALENDAR_NEXT_MONTH)

    def get_search_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)

    def get_passenger_options(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSENGERS_OPTIONS)

    def get_adults_passengers_plus_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADULTS_NUMBER_PLUS)

    def get_confirm_passengers_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CONFIRM_PASSENGERS)

    def set_adults_passengers(self):
        self.get_passenger_options().click()
        self.get_adults_passengers_plus_button().click()
        self.get_confirm_passengers_button().click()

    def set_location_from(self, location_from):
        self.get_location_from_button().click()
        self.get_default_location_from().click()
        self.get_location_from_field().send_keys(location_from)

    def pick_location_from(self):
        for airportsFrom in self.get_location_from_search_results():
            airportsFrom.click()
            break

    def set_location_to(self, location_to):
        self.get_location_to_button().click()
        self.get_location_to_field().send_keys(location_to)

    def pick_location_to(self):
        for airportsTo in self.get_location_to_search_results():
            airportsTo.click()
            break

    def activate_calendar(self):
        self.get_calendar_button().click()

    def calendar_from(self, yyyy, mm, dd, duration):
        while True:
            try:
                self.driver.find_element(By.XPATH, get_date_locators(
                    get_dates(yyyy, mm, dd, duration)[0].strftime("%Y-%m-%d"))).click()
                break
            except NoSuchElementException:
                self.get_calendar_next_month().click()

    def calendar_to(self, yyyy, mm, dd, duration):
        while True:
            try:
                self.driver.find_element(By.XPATH, get_date_locators(
                    get_dates(yyyy, mm, dd, duration)[1].strftime("%Y-%m-%d"))).click()
                break
            except NoSuchElementException:
                self.get_calendar_next_month().click()

    def pick_dates_in_both_calendars(self, yyyy, mm, dd, duration):
        self.activate_calendar()
        self.calendar_from(yyyy, mm, dd, duration)
        self.calendar_to(yyyy, mm, dd, duration)

    def search_click(self):
        self.get_search_button().click()
