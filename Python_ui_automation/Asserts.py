import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hard_assert_textbox(driver):
    driver.get("https://demoqa.com/text-box")
    username = driver.find_element(By.ID, "userName")
    assert username is not None, "Username element is None"
    username.send_keys("Rohit")
    actual_value = username.get_attribute("value")
    assert actual_value == "Rohit", "Username value mismatch"   # assertEquals / Hard assert

def test_soft_assert_textbox(driver):
    driver.get("https://demoqa.com/text-box")
    username = driver.find_element(By.ID, "userName")
    username.send_keys("Rohit")
    check.equal(username.get_attribute("value"), "Rohit")
    print("All checks executed")

def test_assert_true_false(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    yes_radio = driver.find_element(By.ID, "yesRadio")
    no_radio = driver.find_element(By.ID, "noRadio")
    assert yes_radio.is_selected(), "Yes radio button is not selected"      # assertTrue
    assert not no_radio.is_selected(), "No radio button should not be selected"   # assertFalse