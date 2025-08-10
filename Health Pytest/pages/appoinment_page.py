from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AppointmentPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    MAKE_APPOINTMENT = (By.XPATH, "//a[@id='btn-make-appointment']")
    LOGIN_SECTION = (By.XPATH, "//section[@id='login']//div[@class='container']")
    USERNAME = (By.XPATH, "//input[@id='txt-username']")
    PASSWORD = (By.XPATH, "//input[@id='txt-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='btn-login']")
    FACILITY = (By.XPATH, "//select[@id='combo_facility']")
    APPLY_BUTTON = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
    MEDICAID = (By.XPATH, "//label[normalize-space()='Medicaid']")
    VISIT_DATE = (By.XPATH, "//input[@id='txt_visit_date']")
    COMMENT = (By.XPATH, "//textarea[@id='txt_comment']")
    BOOK_BUTTON = (By.XPATH, "//button[@id='btn-book-appointment']")
    SUMMARY_SECTION = (By.XPATH, "//section[@id='summary']//div[@class='container']")
    GO_TO_HOMEPAGE = (By.XPATH, "//a[@class='btn btn-default']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'text-danger')]")  # Example locator
    VISIT_DATE_ERROR = (By.XPATH, "//label[@for='txt_visit_date' and contains(@class,'error')]")  # Example, adjust as needed

    def open_page(self, url):
        self.driver.get(url)

    def click_make_appointment(self):
        self.wait.until(EC.element_to_be_clickable(self.MAKE_APPOINTMENT)).click()

    def add_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def add_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.FACILITY)) 

    def get_login_error_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR_MESSAGE)).text
        except TimeoutException:
            return None  # No error shown

    def select_facility(self, facility):
        self.wait.until(EC.presence_of_element_located(self.FACILITY))
        select = Select(self.driver.find_element(*self.FACILITY))
        select.select_by_visible_text(facility)

    def get_facility_options(self):
        self.wait.until(EC.presence_of_element_located(self.FACILITY))
        select = Select(self.driver.find_element(*self.FACILITY))
        return [option.text for option in select.options]

    def click_apply_button(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()

    def click_medicaid(self):
        self.driver.find_element(*self.MEDICAID).click()

    def add_visit_date(self, visit_date):
        self.driver.find_element(*self.VISIT_DATE).clear()
        self.driver.find_element(*self.VISIT_DATE).send_keys(visit_date)

    def get_visit_date_error_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VISIT_DATE_ERROR)).text
        except TimeoutException:
            return None  # No error shown

    def add_comment(self, comment):
        self.driver.find_element(*self.COMMENT).send_keys(comment)

    def click_book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON).click()

    def get_summary_text(self):
        self.wait.until(EC.presence_of_element_located(self.SUMMARY_SECTION))
        return self.driver.find_element(*self.SUMMARY_SECTION).text

    def click_go_to_homepage(self):
        self.driver.find_element(*self.GO_TO_HOMEPAGE).click()

    def get_current_url(self):
        return self.driver.current_url
