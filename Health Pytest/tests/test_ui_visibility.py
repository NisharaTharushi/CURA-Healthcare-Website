import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.confirmation_page import ConfirmationPage

def test_Make_Appointment_UI_Visibility(browser):
    page = ConfirmationPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")

    # Wait for Make Appointment button
    make_appointment = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(page.MAKE_APPOINTMENT)
    )
    assert make_appointment.is_displayed()

    # Click Make Appointment to load login section
    page.click_make_appointment()

def test_Login_UI_Visibility(browser):
    page = ConfirmationPage(browser)
    # Wait for username, password and login button
    username = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(page.USERNAME)
    )
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(page.PASSWORD)
    )
    login_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(page.LOGIN_BUTTON)
    )

    assert username.is_displayed()
    assert password.is_displayed()
    assert login_button.is_displayed()


if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])
