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

def test_rows_columns(driver):
    driver.get('https://demoqa.com/webtables')
    rows = driver.find_elements(By.XPATH,"//tbody/tr")
    print("Total Rows :", len(rows)) # Number of rows

    driver.get('https://demoqa.com/webtables')
    columns = driver.find_elements(By.XPATH,"//tbody/tr[1]/td[position() < last()]")
    print("Total columns :", len(columns))  # Number of columns

    for i in range(len(rows)):  # Read all data
        cells = driver.find_elements(By.XPATH,f"//tbody/tr[{i+1}]/td[position() < last()]")
        for cell in cells:
            print(cell.text, end=' | ' )
        print()

def test_find_specific_value(driver):
    driver.get("https://demoqa.com/webtables")
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    value = "Cierra"
    for i in range(len(rows)):
        cells = driver.find_elements(By.XPATH,f"//tbody/tr[{i+1}]/td[position() < last()]")
        for cell in cells:
            if cell.text == value:
                print(f"{value} Found")
                return
    print(f"{value} Not Found")

def test_edit_n_delete(driver):
    driver.get("https://demoqa.com/webtables")
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    value = "Cierra"
    for i in range(len(rows)):
        cells = driver.find_elements(By.XPATH,f"//tbody/tr[{i+1}]/td[position() < last()]")
        for cell in cells:
            if cell.text == value:
                driver.find_element(By.XPATH,f"//tbody/tr[{i+1}]//span[@title='Edit']").click()
                time.sleep(3)
                driver.find_element(By.XPATH,"//button[@class='btn-close']").click()
                driver.find_element(By.XPATH,f"//tbody/tr[{i+1}]//span[@title='Delete']").click()
                time.sleep(3)
                return
    print(f"{value} Not Found")

from selenium.webdriver.common.by import By

def test_search_employee_pagination(driver):
    driver.get("https://datatables.net/examples/core/data_sources/dom.html")
    employee = "Michael Silva"      # Present on page 2
    while True:
        names = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[1]") # Read all names on current page
        for name in names:
            print(name.text)
            if name.text.strip() == employee:
                print(f"{employee} Found")
                return
        next_btn = driver.find_element(By.XPATH, "//button[@data-dt-idx='next']") # Go to next page
        if "disabled" in next_btn.get_attribute("class"): # Last page reached
            break
        next_btn.click()
    print(f"{employee} Not Found")

def test_search_employee_sorting(driver):
    driver.get("https://datatables.net/examples/core/data_sources/dom.html")
    names = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[1]") 
    actual = [name.text for name in names]
    expected = sorted(actual)
    print("Actual  :", actual)
    print("Expected:", expected)
    assert actual == expected, "Name sorting is incorrect"