
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from pages.confirmation_page import ConfirmationPage

def test_login_with_invalid_credentials(browser):
    page = ConfirmationPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")
    page.click_make_appointment()
    
    # Enter invalid login credentials
    page.add_username("invalid_user")
    page.add_password("invalid_pass")
    page.click_login_button()
    
    # Verify still on login page or error appears
    assert "Login" in browser.title or "login" in browser.current_url.lower()

    # Verify login failed message
    error_message = page.get_login_error_message()
    assert error_message is not None
    assert "Login failed!" in error_message


if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])