import sys
import os
import pytest

# Ensure root path is added
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.sidebar_page import SidebarPage

URL = "https://katalon-demo-cura.herokuapp.com/"

def test_sidebar_icon(browser):
    page = SidebarPage(browser)
    page.open_page(URL)
    page.click_menu_button()
    page.click_login_button()
    page.add_username("John Doe")
    page.add_password("ThisIsNotAPassword")
    page.click_login()

    page.click_menu_button()
    

def test_sidebar_profile_icon(browser):
    page = SidebarPage(browser)
    page.open_page(URL)
    page.click_menu_button()
    profile_text = page.click_profile()
    assert "Profile" in profile_text

def test_sidebar_history_icon(browser): 
    page = SidebarPage(browser)
    page.open_page(URL)
    page.click_menu_button()
    history_text = page.click_history_button()
    assert "History" in history_text

def test_sidebar_logout_icon(browser):
    page = SidebarPage(browser)
    page.open_page(URL)
    page.click_menu_button()
    page.click_logout_button()


if __name__ == "__main__":
    import pytest
    import os
    pytest.main(["-v", os.path.abspath(__file__)])