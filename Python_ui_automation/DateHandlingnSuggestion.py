import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_simple_date_picker(driver):
    driver.get("https://demoqa.com/date-picker")
    date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_input.send_keys(Keys.CONTROL + "a")
    date_input.send_keys("08/15/2026")
    date_input.send_keys(Keys.ENTER)
    selected_date = date_input.get_attribute("value")
    print("Selected Date:", selected_date)
    assert selected_date == "08/15/2026"

def select_date(driver, target_date):
    dt = datetime.strptime(target_date, "%d/%m/%Y")
    day = str(dt.day)
    month = dt.strftime("%B")
    year = str(dt.year)
    driver.find_element(By.ID, "datePickerMonthYearInput").click()
    while True:
        current_month_year = driver.find_element(By.CLASS_NAME,"react-datepicker__current-month").text
        if current_month_year == f"{month} {year}":
            break
        driver.find_element(By.XPATH,"//button[@aria-label='Next Month']").click()
    driver.find_element(By.XPATH,f"//div[contains(@class,'react-datepicker__day') and text()='{day}']").click()

def test_dynamic_date_picker(driver):
    driver.get("https://demoqa.com/date-picker")
    select_date(driver, "15/08/2027")

def test_google_search_suggestions(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium python")
    suggestions = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))
    print("Available Suggestions:")
    target = "selenium python automation"
    found = False
    for suggestion in suggestions:
        suggestion_text = suggestion.text.strip()
        print(suggestion_text)
        if suggestion_text.lower() == target.lower():
            print(f"Clicking: {suggestion_text}")
            try:
                suggestion.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();",suggestion)
            found = True
            break
    assert found, f"Suggestion '{target}' was not found"