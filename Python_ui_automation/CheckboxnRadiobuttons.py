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
def test_single_multiple_checkbox(driver):
    driver.get('https://demoqa.com/checkbox')
    driver.find_element(By.XPATH, "//div[@role='treeitem']/span[2]").click()  # Expand Home
    time.sleep(3)
    desktop_cb = driver.find_element(By.XPATH,"//span[@title='Desktop']/preceding-sibling::span[@role='checkbox']")
    desktop_cb.click()  # single select
    time.sleep(3)
    desktop_cb.click()  # unselect

    checkboxes = driver.find_elements(By.XPATH,"//span[@role='checkbox' and @aria-label='Select Home']")  # multi select
    for checkbox in checkboxes:
        checkbox.click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[@role='checkbox' and @aria-label='Select Home']").click()  # unselect

    value = 'Desktop'  # using value
    driver.find_element(By.XPATH,f"//span[@title='{value}']/preceding-sibling::span[@role='checkbox']").click()
    time.sleep(3)


def test_radio_n_state(driver):
    driver.get('https://demoqa.com/radio-button')
    yes_radio = driver.find_element(By.ID, "yesRadio")
    yes_radio.click()  # radio selection
    no_radio = driver.find_element(By.ID, "noRadio")
    assert yes_radio.is_selected()  # Verify selected state
    assert not no_radio.is_selected()
    time.sleep(3)