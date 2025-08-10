# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ===== Element Finders =====
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    # ===== Actions on Elements =====
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        element = self.find_element(locator)
        element.clear()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def is_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def is_selected(self, locator):
        return self.find_element(locator).is_selected()

    # ===== Browser Navigation =====
    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    # ===== Window Controls =====
    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def maximize_window(self):
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()

    def print_current_url(self):
        print(self.driver.current_url)