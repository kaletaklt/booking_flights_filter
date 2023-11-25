from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


def get_flight_card_number(x):
    flight_card = "//div[@id='flightcard-" + str(x) + "']"
    return flight_card


class SearchFlightResults(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators
    ONE_STOP_MAX = "//div[text()='1 stop max']"
    ANY_STOPS = "//div[text()='Any']"
    NUMBER_OF_RESULTS_PAGES = "//li[@class='Pagination-module__item___i0eou'][last()]"
    DEPARTURE_HOURS = "//div[@data-testid='flight_card_segment_departure_time_0']"
    FLIGHT_CARD_PRICE = "//div[@data-testid='flight_card_price_main_price']"
    FLIGHT_CARD_LINK = "//button[@data-testid='flight_card_bound_select_flight']"
    NEXT_BUTTON = "//div[@class='Pagination-module__item___i0eou Pagination-module__nextArrow___WCdsO']//button"
    CLOSE_FLIGHT_DETAILS = ("//div[@class='Button-module__aligner___Q44cD Button-module__root--alignment-top___nWUyH "
                            "Button-module__root--alignment-end___SgZ34 DismissibleContainer-module__close___Um3-I "
                            "SheetContainer-module__close___+WEtn']//button[@class='Actionable-module__root___o3y3+ "
                            "Button-module__root___2Z2KR Button-module__root--variant-tertiary___cjBJU "
                            "Button-module__root--icon-only___GOysd Button-module__root--size-medium___+UaTJ "
                            "Button-module__root--wide-false___V33Sh "
                            "Button-module__root--variant-tertiary-neutral___tEjZX']")

    def get_select_one_stop_max(self):
        return self.wait_until_element_is_clickable_flights_results(By.XPATH, self.ONE_STOP_MAX)

    def get_select_any_stops(self):
        return self.wait_until_element_is_clickable_flights_results(By.XPATH, self.ANY_STOPS)

    def get_number_of_results_pages(self):
        return self.wait_until_element_is_clickable_flights_results(By.XPATH, self.NUMBER_OF_RESULTS_PAGES)

    def get_departure_hours(self):
        return self.wait_until_presence_of_all_elements_located_flights_results(By.XPATH, self.DEPARTURE_HOURS)

    def get_next_button(self):
        return self.wait_until_element_is_clickable_flights_results(By.XPATH, self.NEXT_BUTTON)

    def getFlightCardsDetailsIfPrice(self, max_price):
        number_of_flights = 14
        for page in range(1, int(self.get_number_of_results_pages().text)):
            for i in range(0, number_of_flights):
                price = self.convert_web_element_to_float(self.wait_until_presence_of_element_located(By.XPATH,
                                                                                                      get_flight_card_number(
                                                                                                          i) + self.FLIGHT_CARD_PRICE))
                if price <= max_price:
                    self.wait_until_presence_of_element_located(By.XPATH, get_flight_card_number(
                        i) + self.FLIGHT_CARD_LINK).click()
                    print(self.driver.current_url)
                    self.wait_until_presence_of_element_located(By.XPATH,
                                                                self.CLOSE_FLIGHT_DETAILS).click()
            self.get_next_button().click()

    def get_prices(self):
        return self.wait_until_presence_of_all_elements_located_flights_results(By.XPATH, self.FLIGHT_CARD_PRICE)

    def one_stop_max(self, one_stop_max):
        if one_stop_max:
            self.get_select_one_stop_max().click()
        else:
            self.get_select_any_stops().click()

    def results_departure_hour(self):
        results = []
        for results_pages in range(1, int(self.get_number_of_results_pages().text)):
            new_results = self.get_departure_hours()
            for result in new_results:
                results.append(result.text)
            self.get_next_button().click()
        return results

    def results_prices(self):
        results = []
        for results_pages in range(1, int(self.get_number_of_results_pages().text)):
            new_results = self.get_prices()
            for result in new_results:
                results.append(result.text)
            self.get_next_button().click()
        return results
