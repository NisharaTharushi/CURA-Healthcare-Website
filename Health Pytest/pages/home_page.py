from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    SUB_TITLE = (By.XPATH, "//h3[normalize-space()='We Care About Your Health']")
    MAKE_APPOINTMENT = (By.XPATH, "//a[@id='btn-make-appointment']")
    MENU_BUTTON = (By.XPATH, "//i[@class='fa fa-bars']")
    HOME_BUTTON = (By.XPATH, "//a[normalize-space()='Home']")
    LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Login']")
    FOOTER = (By.XPATH, "//div[@class='container']")
    BODY = (By.TAG_NAME, "body")
   
    def open_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_sub_title(self):
        return self.driver.find_element(*self.SUB_TITLE).text

    def click_make_appointment(self):
        self.driver.find_element(*self.MAKE_APPOINTMENT).click()

    def get_current_url(self):
        return self.driver.current_url

    def go_back(self):
        self.driver.back()

    def click_menu_button(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

    def click_home_button(self):
        self.driver.find_element(*self.HOME_BUTTON).click()

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_footer_text(self):
        return self.driver.find_element(*self.FOOTER).text

    def get_body_text(self):
        return self.driver.find_element(*self.BODY).text
