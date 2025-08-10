import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pages.appoinment_page import AppointmentPage

URL = "https://katalon-demo-cura.herokuapp.com/"

def test_book_appointment(browser):
    # open page and click Make Appointment
    page = AppointmentPage(browser)
    page.open_page(URL)
    page.click_make_appointment()

    # fill form
    page.add_username("John Doe")
    page.add_password("ThisIsNotAPassword")
    page.click_login_button()
    page.get_login_error_message()

    page.select_facility("Hongkong CURA Healthcare Center")
    page.get_facility_options()
    page.click_apply_button()
    page.click_medicaid()
    page.add_visit_date("30/06/2025")
    page.add_comment("Follow-up visit for blood pressure check.")
    page.click_book_button()

    # test confirmation
    summary = page.get_summary_text()
    assert "Appointment Confirmation" in summary
    assert "Hongkong CURA Healthcare Center" in summary

    page.click_go_to_homepage()
    assert page.get_current_url() == URL

    assert "CURA Healthcare Service" in browser.title


if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])