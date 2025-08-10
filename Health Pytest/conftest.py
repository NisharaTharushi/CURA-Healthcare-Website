import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="module")
def browser():
    options = Options()
    # options.add_argument("--headless")  # Uncomment this line for headless mode if you want
    service = Service()  # You can specify geckodriver path like Service("/path/to/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


