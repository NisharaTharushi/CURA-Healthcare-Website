import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from pages.login_page import LoginPage

URL = "https://katalon-demo-cura.herokuapp.com/"

def test_full_login_flow(browser):
    page = LoginPage(browser)
    page.open_page(URL)
    page.click_menu_button()
    page.click_login_button()
    
    page.add_username("John Doe")
    page.add_password("ThisIsNotAPassword")
    page.click_login()

    page.click_facility("Hongkong CURA Healthcare Center")
    page.click_apply_button()
    page.click_medicaid()
    page.add_visit_date("30/06/2025")
    page.add_comment("Automated appointment booking.")
    page.click_book_button()

    summary_text = page.get_summary_text()
    assert "Appointment Confirmation" in summary_text
    assert "Hongkong CURA Healthcare Center" in summary_text

    page.click_go_to_homepage()
    assert "CURA Healthcare Service" in browser.title
    
if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])

