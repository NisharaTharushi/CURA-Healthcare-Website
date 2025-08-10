from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SidebarPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    MENU_BUTTON = (By.XPATH, "//i[@class='fa fa-bars']")
    LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Login']")
    LOGIN_SECTION = (By.XPATH, "//section[@id='login']//div[@class='container']")
    USERNAME = (By.XPATH, "//input[@id='txt-username']")
    PASSWORD = (By.XPATH, "//input[@id='txt-password']")
    LOGIN = (By.XPATH, "//button[@id='btn-login']")
    PROFILE = (By.XPATH, "//a[normalize-space()='Profile']")
    PROFILE_SECTION = (By.XPATH, "//section[@id='profile']//div[@class='container']")
    HISTORY_BUTTON = (By.XPATH, "//a[normalize-space()='History']")
    HISTORY_SECTION = (By.XPATH, "//section[@id='history']//div[@class='container']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")

    def open_page(self, url):
        self.driver.get(url)

    def click_menu_button(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def add_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def add_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN).click()

    def click_profile(self):
        self.driver.find_element(*self.PROFILE).click()
        return self.driver.find_element(*self.PROFILE_SECTION).text

    def click_history_button(self):
        self.driver.find_element(*self.HISTORY_BUTTON).click()
        return self.driver.find_element(*self.HISTORY_SECTION).text

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
