import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_mouse_hover(driver):
    driver.get("https://demoqa.com/menu")
    time.sleep(3)
    actions = ActionChains(driver)
    # main_item_2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Main Item 2']")))
    main_item_2 = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    actions.move_to_element(main_item_2).perform()
    sub_sub_list = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
    actions.move_to_element(sub_sub_list).perform()
    sub_sub_item_2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Sub Item 2']")))
    actions.move_to_element(sub_sub_item_2).click().perform()

def test_right_double_click(driver):
    driver.get("https://demoqa.com/buttons")
    right_click_btn = driver.find_element(By.ID, "rightClickBtn") # Right Click
    ActionChains(driver).context_click(right_click_btn).perform()
    print(driver.find_element(By.ID, "rightClickMessage").text)

    double_click_btn = driver.find_element(By.ID, "doubleClickBtn") # Double Click
    ActionChains(driver).double_click(double_click_btn).perform()
    print(driver.find_element(By.ID, "doubleClickMessage").text)

    click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']") # Move to element with offset and click
    ActionChains(driver).move_to_element_with_offset(click_btn, 50, 20).click().perform()

def test_drag_drop(driver):
    driver.get("https://demoqa.com/droppable")
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(source, target).perform()
    time.sleep(5)

def test_drag_drop_hold_release(driver):
    driver.get("https://demoqa.com/droppable")
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    ActionChains(driver).click_and_hold(source).move_to_element(target).release().perform()
    time.sleep(5)

def test_keyboard_copy_paste(driver):
    driver.get("https://demoqa.com/text-box")
    current_address = driver.find_element(By.ID, "currentAddress")
    permanent_address = driver.find_element(By.ID, "permanentAddress")
    current_address.send_keys("Hyderabad")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() # Ctrl + A
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() # Ctrl + C
    permanent_address.click()
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() # Ctrl + V
    time.sleep(5)

def test_wheelInput_actions(driver):
    driver.get("https://demoqa.com/text-box")
    ActionChains(driver).scroll_by_amount(0, 600).perform() # Scroll down
    time.sleep(5)
    ActionChains(driver).scroll_by_amount(0, -300).perform() # Scroll up
    time.sleep(5)
    submit = driver.find_element(By.ID, "submit")
    ActionChains(driver).scroll_to_element(submit).perform() # Scroll directly to element
    time.sleep(5)