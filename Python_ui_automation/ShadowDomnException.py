import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import InvalidSelectorException
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shadow_dom(driver):
    driver.get("https://practice.expandtesting.com/shadowdom")
    shadow_host = driver.find_element(By.ID, "shadow-host")
    shadow_root = shadow_host.shadow_root
    text = shadow_root.find_element(By.CSS_SELECTOR, "#my-btn")
    print(text.text)

def test_no_such_element_exception(driver):
    driver.get("https://demoqa.com/text-box")
    try:
        driver.find_element(By.ID, "wrongUserName").send_keys("Rohit")
    except NoSuchElementException:
        print("Element not found. Please check locator.")

def test_stale_element_reference_exception(driver):
    driver.get("https://demoqa.com/text-box")
    username = driver.find_element(By.ID, "userName")
    driver.refresh()
    try:
        username.send_keys("Rohit")
    except StaleElementReferenceException:
        print("Element became stale. Re-locating element.")
        username = driver.find_element(By.ID, "userName")
        username.send_keys("Rohit")

def test_timeout_exception(driver):
    driver.get("https://demoqa.com/text-box")
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "wrongElement")))
    except TimeoutException:
        print("Element was not visible within the given time.")

def test_element_click_intercepted_exception(driver):
    driver.get("https://demoqa.com/text-box")
    submit_button = driver.find_element(By.ID, "submit")
    try:
        submit_button.click()
    except ElementClickInterceptedException:
        print("Click intercepted. Using scroll and JS click.")
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});",submit_button)
        driver.execute_script("arguments[0].click();",submit_button)

def test_no_alert_present_exception(driver):
    driver.get("https://demoqa.com/alerts")
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        print("No alert is present.")

def test_no_such_frame_exception(driver):
    driver.get("https://demoqa.com/frames")
    try:
        driver.switch_to.frame("wrongFrame")
    except NoSuchFrameException:
        print("Frame not found. Please check frame id/name/index.")

def test_no_such_window_exception(driver):
    driver.get("https://demoqa.com/browser-windows")
    current_window = driver.current_window_handle
    wrong_window = "invalid_window_handle"
    try:
        driver.switch_to.window(wrong_window)
    except NoSuchWindowException:
        print("Window not found. Please check window handle.")
    driver.switch_to.window(current_window)

def test_invalid_selector_exception(driver):
    driver.get("https://demoqa.com/text-box")
    try:
        driver.find_element(By.XPATH, "//input[@id='userName'")
    except InvalidSelectorException:
        print("Invalid XPath syntax.")