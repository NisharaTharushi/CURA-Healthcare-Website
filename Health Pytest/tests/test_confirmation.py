import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from pages.confirmation_page import ConfirmationPage

def test_appointment_booking_flow(browser):
    page = ConfirmationPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")

    # Step 1: Click Make Appointment
    page.click_make_appointment()

    # Step 2: Login
    page.add_username("John Doe")
    page.add_password("ThisIsNotAPassword")
    page.click_login_button()

    # Step 3: Fill form
    page.select_facility("Hongkong CURA Healthcare Center")
    page.click_apply_button()
    page.click_medicaid()
    page.add_visit_date("06/06/2025")
    page.add_comment("Booking test comment")
    page.click_book_button()

    # Step 4: Assert confirmation
    assert "Appointment Confirmation" in browser.page_source
    summary_text = page.get_summary_text()
    print("Summary:\n", summary_text)
    assert len(summary_text) > 0

    # Step 5: Return to homepage
    page.click_go_to_homepage()
    assert "CURA Healthcare Service" in browser.title

# Step 6: Confirm the appointment in history page - assert on actual visible text
def test_Confirmation(browser):
    page = ConfirmationPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")
    page.click_side_menu()
    page.click_history_button()
    history_text = page.get_history_text()
    print("History:\n", history_text)
    assert "History" in history_text
    assert "Hongkong CURA Healthcare Center" in history_text
    assert "Booking test comment" in history_text

    # Step 7: Logout
def test_logout(browser):
    page = ConfirmationPage(browser)
    page.open_page("https://katalon-demo-cura.herokuapp.com/")
    page.click_side_menu()
    page.click_logout()
    assert "Login" in browser.page_source or "login" in browser.current_url.lower()


if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])