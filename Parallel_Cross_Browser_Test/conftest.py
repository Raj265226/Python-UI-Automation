import pytest
from selenium import webdriver

def create_driver(browser):
    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver

@pytest.fixture(params=["edge", "chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param
    driver = create_driver(browser)
    yield driver
    driver.quit()