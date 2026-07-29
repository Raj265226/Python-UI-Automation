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

def test_JS_Click(driver):
    driver.get("https://demoqa.com/buttons")
    button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    driver.execute_script("arguments[0].click();", button)      # JS Click

def test_JS_Scroll(driver):
    driver.get("https://demoqa.com/text-box")
    username = driver.find_element(By.ID, "userName")
    Page_Title = driver.execute_script("return document.title;")   # Get Title
    Page_url = driver.execute_script("return document.URL;")       # Get URL
    print('Page title and url are:', Page_Title, 'and', Page_url)
    driver.execute_script("arguments[0].value='Rohit';", username)   # Enter value
    time.sleep(3)
    R_value = driver.execute_script("return arguments[0].value;", username)   # Retrieve value
    assert 'Rohit' == R_value, f'Current value is {R_value}'
    driver.execute_script("window.scrollBy(0,50);")    # Scroll down
    driver.execute_script("window.scrollBy(0,-60);")   # Scroll up
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();",submit_button)   # Scroll into view
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(5)

def test_JS_Bottom_Top(driver):
    driver.get("https://demoqa.com/text-box")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll to Bottom
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);") # Scroll to Top
    time.sleep(2)