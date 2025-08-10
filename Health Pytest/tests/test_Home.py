import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.home_page import Homepage
import pytest

URL = "https://katalon-demo-cura.herokuapp.com/"

def test_home_page_load(browser):
    home = Homepage(browser)
    home.open_page(URL)
    assert "CURA Healthcare Service" in home.get_title()
    
def test_home_page_title(browser):
    home = Homepage(browser)
    home.open_page(URL)
    assert "CURA Healthcare" in home.get_title()

def test_sub_title_visible(browser):
    home = Homepage(browser)
    home.open_page(URL)
    assert "We Care About Your Health" in home.get_sub_title()

def test_make_appointment_redirect(browser):
    home = Homepage(browser)
    home.open_page(URL)
    home.click_make_appointment()
    assert "profile.php#login" in home.get_current_url()

def test_menu_navigation_to_home(browser):
    home = Homepage(browser)
    home.open_page(URL)
    home.click_menu_button()
    home.click_home_button()
    assert URL in home.get_current_url()

def test_login_button_redirect(browser):
    home = Homepage(browser)
    home.open_page(URL)
    home.click_menu_button()
    home.click_login_button()
    assert "profile.php#login" in home.get_current_url()

def test_footer_text_contains_cura(browser):
    home = Homepage(browser)
    home.open_page(URL)
    assert "CURA" in home.get_footer_text()

def test_body_text_contains_information(browser):
    home = Homepage(browser)
    home.open_page(URL)
    body_text = home.get_body_text()
    assert "CURA" in body_text or "We Care" in body_text

if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])