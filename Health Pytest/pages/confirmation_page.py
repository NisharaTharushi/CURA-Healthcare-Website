from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    MAKE_APPOINTMENT = (By.ID, "btn-make-appointment")
    LOGIN_SECTION = (By.XPATH, "//section[@id='login']//div[@class='container']")
    USERNAME = (By.ID, "txt-username")
    PASSWORD = (By.ID, "txt-password")
    LOGIN_BUTTON = (By.ID, "btn-login")
    FACILITY = (By.ID, "combo_facility")
    APPLY_BUTTON = (By.ID, "chk_hospotal_readmission")
    MEDICAID = (By.XPATH, "//label[normalize-space()='Medicaid']")
    VISIT_DATE = (By.ID, "txt_visit_date")
    COMMENT = (By.ID, "txt_comment")
    BOOK_BUTTON = (By.ID, "btn-book-appointment")
    SUMMARY_SECTION = (By.XPATH, "//section[@id='summary']//div[@class='container']")
    GO_TO_HOMEPAGE = (By.XPATH, "//a[@class='btn btn-default']")
    SIDE_MENU = (By.ID, "menu-toggle")
    HISTORY_BUTTON = (By.LINK_TEXT, "History")
    HISTORY_SECTION = (By.XPATH, "//section[@id='history']//div[@class='container']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

    def open_page(self, url):
        self.driver.get(url)

    def click_make_appointment(self):
        self.wait.until(EC.element_to_be_clickable(self.MAKE_APPOINTMENT)).click()

    def add_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)

    def add_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def select_facility(self, facility):
        facility_element = self.wait.until(EC.element_to_be_clickable(self.FACILITY))
        facility_element.send_keys(facility)

    def click_apply_button(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_BUTTON)).click()

    def click_medicaid(self):
        self.wait.until(EC.element_to_be_clickable(self.MEDICAID)).click()

    def add_visit_date(self, visit_date):
        self.wait.until(EC.visibility_of_element_located(self.VISIT_DATE)).send_keys(visit_date)

    def add_comment(self, comment):
        self.wait.until(EC.visibility_of_element_located(self.COMMENT)).send_keys(comment)

    def click_book_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BOOK_BUTTON)).click()

    def get_summary_text(self):
        summary = self.wait.until(EC.visibility_of_element_located(self.SUMMARY_SECTION))
        return summary.text

    def click_go_to_homepage(self):
        self.wait.until(EC.element_to_be_clickable(self.GO_TO_HOMEPAGE)).click()

    def click_side_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDE_MENU)).click()

    def click_history_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HISTORY_BUTTON)).click()

    def get_history_text(self):
        history = self.wait.until(EC.visibility_of_element_located(self.HISTORY_SECTION))
        return history.text
    
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        print("Logout button clicked")
