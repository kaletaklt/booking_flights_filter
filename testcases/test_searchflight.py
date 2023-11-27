import pytest

from pages.booking_launch_page import LaunchPage
from pages.search_flights_page import FlightsPage
from pages.search_flights_results_page import SearchFlightResults


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
        lp = LaunchPage(self.driver, self.wait)
        fp = FlightsPage(self.driver, self.wait)
        frp = SearchFlightResults(self.driver, self.wait)

        # Launch browser, accept cookies and Genius prompt if appears, set language
        lp.accept_cookies()
        lp.genius_close()
        lp.set_language()
        lp.genius_close()

        # Click Flights tab
        lp.click_flights()

        # Set number of adults
        fp.set_adults_passengers()

        # Select From
        fp.set_location_from("Warsaw")

        # Select From result
        fp.pick_location_from()

        # Select To
        fp.set_location_to("New York")

        # Select To result
        fp.pick_location_to()

        # Pick Dates
        fp.pick_dates_in_both_calendars(2024, 4, 20, 2)

        # Search button
        fp.search_click()

        # One stop max?
        frp.one_stop_max(True)

        # results page berlin departure
        # results = frp.results_departure_hour()

        frp.get_flight_cards_details_if_price_below(2200)

        # frp.results_prices()
