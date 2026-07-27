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

def test_ParentChild(driver):
    driver.get('https://demoqa.com/browser-windows')
    parent = driver.current_window_handle   # Store Parent Tab
    print("Parent:", parent)
    driver.find_element(By.ID, "tabButton").click() # Open Child Tab
    all_tabs = driver.window_handles
    print("All Tabs:", all_tabs)
    for tab in all_tabs:
        if tab != parent:      # Switch Parent -> Child         
            driver.switch_to.window(tab)
            break
    print("Child Tab:", driver.current_window_handle)
    driver.close()
    driver.switch_to.window(parent) # Child -> Parent

def test_multiWindows(driver):
    driver.get('https://demoqa.com/browser-windows')
    parent = driver.current_window_handle
    driver.find_element(By.ID, "windowButton").click()     # Open multiple child windows
    driver.find_element(By.ID, "windowButton").click()
    all_windows = driver.window_handles
    print("Total Windows:", len(all_windows))
    for window in all_windows:          # Switch through all child windows
        if window != parent:
            driver.switch_to.window(window)
            time.sleep(3)
            print("Child Window:", driver.current_window_handle)
            print(driver.find_element(By.ID, "sampleHeading").text)
            driver.close()
            time.sleep(3)
    driver.switch_to.window(parent) # Switch back to parent

def test_switch_on_title_n_url(driver):
    driver.get('https://demoqa.com/browser-windows')
    parent_window = driver.current_window_handle
    print("Parent Window:", parent_window)
    print("Parent Title:", driver.title)
    print("Parent URL:", driver.current_url)
    driver.find_element(By.ID, "tabButton").click()
    all_windows = driver.window_handles
    print("Total Windows:", len(all_windows))
    for window in all_windows:          
        driver.switch_to.window(window)
        print("Title:", driver.title)
        print("URL:", driver.current_url)
        if driver.title == "DEMOQA" and "/sample" in driver.current_url:
            print("Required child window found")
            break

def test_new_tab(driver):
    driver.get("https://demoqa.com")
    parent = driver.current_window_handle
    driver.switch_to.new_window("tab") # Open new tab and automatically switch to it
    driver.get("https://demoqa.com/alerts")
    print("New Tab URL:", driver.current_url)
    driver.close()
    driver.switch_to.window(parent)

def test_new_window(driver):
    driver.get("https://demoqa.com")
    parent = driver.current_window_handle
    driver.switch_to.new_window("window") # Open new browser window and automatically switch to it
    driver.get("https://demoqa.com/frames")
    print("New Window URL:", driver.current_url)
    driver.close()
    driver.switch_to.window(parent) 