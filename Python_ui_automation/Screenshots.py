import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_viewpoint_n_element_screenshot(driver):
    driver.get("https://demoqa.com/text-box")
    driver.save_screenshot("Screenshots_capture_test/demoqa_viewport1.png")  # Full viewport screenshot
    driver.get_screenshot_as_file("Screenshots_capture_test/demoqa_viewport2.png") # Full viewport screenshot
    username = driver.find_element(By.ID, "userName")  # Element screenshot
    username.screenshot("Screenshots_capture_test/username_textbox.png")

def test_screenshot_on_failure(driver):
    try:
        driver.get("https://demoqa.com/text-box")
        username = driver.find_element(By.ID, "userName")
        username.send_keys("Rohit")
        value = username.get_attribute("value")
        assert value == "Raj"
    except AssertionError:
        driver.save_screenshot("Screenshots_capture_test/failure_screenshot.png") # Capture screenshot when assertion fails
        raise

def test_screenshot_on_failure_report(driver):
    driver.get("https://demoqa.com/text-box")
    username = driver.find_element(By.ID, "userName")
    username.send_keys("Rohit")
    assert username.get_attribute("value") == "Raj" # Attach screenshot to report 