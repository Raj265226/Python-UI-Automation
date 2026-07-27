import pytest 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
@pytest.fixture(scope='module') 
def driver():
    driver = webdriver.Chrome() # Initialize browser once
    driver.maximize_window()
    yield driver
    driver.quit()

def test_single_n_multi_selected(driver):
    driver.get('https://demoqa.com/select-menu') 
    time.sleep(3)
    dropdown = Select(driver.find_element(By.ID,'oldSelectMenu'))           # single selection
    dropdown.select_by_value("1")
    time.sleep(3)
    dropdown_cars = Select(driver.find_element(By.ID, "cars"))              # multi selection
    dropdown_cars.select_by_visible_text("Volvo")
    dropdown_cars.select_by_visible_text("Audi")

def test_custom(driver):
    driver.get('https://demoqa.com/select-menu') 
    time.sleep(3)
    driver.find_element(By.ID,'withOptGroup').click()          
    driver.find_element(By.XPATH, "//*[contains(text(),'Another root option')]").click()

def test_search(driver):
    driver.get('https://demoqa.com/select-menu') 
    time.sleep(3)
    search = driver.find_element(By.ID,'react-select-4-input')
    search.send_keys("Green")
    search.send_keys(Keys.ENTER)         