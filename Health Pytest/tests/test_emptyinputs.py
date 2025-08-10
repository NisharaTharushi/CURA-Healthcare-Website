import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from pages.appoinment_page import AppointmentPage

# Test empty username 
def test_empty_username(browser):
    page = AppointmentPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")
    page.click_make_appointment()

    page.add_password("ThisIsNotAPassword")  # no username on purpose
    page.click_login_button()

    error_message = page.get_login_error_message()
    assert error_message is not None
    assert "Login failed!" in error_message

# Test empty password
def test_empty_password(browser):
    page = AppointmentPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")
    page.click_make_appointment()

    page.add_username("John Doe")
    page.click_login_button()

    error_message = page.get_login_error_message()
    assert error_message is not None
    assert "Login failed!" in error_message

if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])