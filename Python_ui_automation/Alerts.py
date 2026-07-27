import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_Alerts(driver):
    driver.get('https://demoqa.com/alerts')
    driver.find_element(By.ID, "alertButton").click()  # Simple Alerts
    alert = driver.switch_to.alert
    time.sleep(3)
    print('Simple Alerts', alert.text)
    alert.accept()

    driver.find_element(By.ID, "confirmButton").click()  # Confirmation Alerts with ok
    alert = driver.switch_to.alert
    time.sleep(3)
    print('Confirmation Alerts', alert.text)
    alert.accept()

    driver.find_element(By.ID, "confirmButton").click()  # Confirmation Alerts with cancel
    alert = driver.switch_to.alert
    time.sleep(3)
    alert.dismiss()

    driver.find_element(By.ID, "promtButton").click()  # Prompt alert
    alert = driver.switch_to.alert
    alert.send_keys("Rohit")
    time.sleep(3)
    alert.accept()
    result = driver.find_element(By.ID, "promptResult").text
    print(result)

    driver.find_element(By.ID, "timerAlertButton").click()  # Timed alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Timed alert", alert.text)
    alert.accept()