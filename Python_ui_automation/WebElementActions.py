import pytest 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope='module') 
def driver():
    driver = webdriver.Chrome() # Initialize browser once
    driver.maximize_window()
    yield driver
    driver.quit()

def test_text_n_get_attribute(driver):
    driver.get('https://demoqa.com/text-box') 
    time.sleep(3)
    name = driver.find_element(By.ID,'userName')
    name.send_keys('Raj')
    name.clear()                                                # Clear textbox
    name.send_keys('Rohit')
    assert name.get_attribute('placeholder') == 'Full Name'     # get_attribute
    time.sleep(3)
    submit_button = driver.find_element(By.ID, "submit")
    assert submit_button.is_displayed()                         # verify element is displayed
    assert submit_button.is_enabled()                           # verify element is enabled
    submit_button.click()
    time.sleep(3)
    output = driver.find_element(By.ID,'name')                  # Retrieve textbox value
    assert 'Rohit' in output.text                               # Retrieve visible text

def test_checkbox_selected(driver):
    driver.get("https://demoqa.com/checkbox")
    checkbox = driver.find_element(By.CLASS_NAME,"rc-tree-checkbox")
    assert not checkbox.is_selected()                           # verify enabled or not
    checkbox.click()