from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_clickable_flights_results(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_presence_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return element

    def wait_until_presence_of_all_elements_located_flights_results(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return element

    def wait_until_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def convert_web_element_to_float(self, web_element):
        web_element = web_element.text
        web_element = web_element[:web_element.find(" zł")].replace(" ", "").replace(",", ".")
        web_element = float(web_element)
        return web_element
