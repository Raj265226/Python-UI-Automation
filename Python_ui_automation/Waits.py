import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_radio_button_with_fluent_wait(driver):
    driver.get("https://demoqa.com/radio-button")
    wait = WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=(NoSuchElementException,))
    yes_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']")))
    yes_label.click()
    yes_radio = driver.find_element(By.ID, "yesRadio")
    assert yes_radio.is_selected(), "Yes radio button is not selected"

def test_radio_n_state(driver):
    driver.implicitly_wait(10)  # Implicit Wait
    driver.get("https://demoqa.com/radio-button")
    wait = WebDriverWait(driver, 10)
    yes_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']"))) # Explicit Wait
    yes_label.click()
    yes_radio = driver.find_element(By.ID, "yesRadio")
    assert yes_radio.is_selected(), "Yes radio button is not selected"

def test_custom_wait(driver):
    driver.get("https://demoqa.com/progress-bar")
    driver.find_element(By.ID, "startStopButton").click()
    def progress_completed(driver):
        return driver.find_element(By.CSS_SELECTOR,".progress-bar").text == "100%"
    WebDriverWait(driver, 20).until(progress_completed)
    print("Custom wait 1 : Completed")

def test_custom_wait_using_lambda(driver):
    driver.get("https://demoqa.com/progress-bar")
    driver.find_element(By.ID, "startStopButton").click()
    WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CSS_SELECTOR,".progress-bar").get_attribute("aria-valuenow") == "100")
    print("Custom wait 2 : Completed")