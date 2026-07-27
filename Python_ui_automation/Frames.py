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

def test_Frames_TotalFrames(driver):
    driver.get('https://demoqa.com/frames')
    driver.switch_to.frame(0)  # Frame by Index and 0 means the first iframe on the page.
    text = driver.find_element(By.ID, "sampleHeading").text
    print('After frame by index',text)
    driver.switch_to.default_content() # Come back to main page

    driver.switch_to.frame("frame1") # Switch using frame ID
    text = driver.find_element(By.ID, "sampleHeading").text
    print('After frame by id',text)
    driver.switch_to.default_content()

    frame = driver.find_element(By.ID, "frame1") # Switch using frame WebElement
    driver.switch_to.frame(frame) 
    text = driver.find_element(By.ID, "sampleHeading").text
    print('After frame by webelement',text)
    driver.switch_to.default_content()

    iframes = driver.find_elements(By.TAG_NAME, "iframe")   # Number of iFrames
    print("Number of iframes:", len(iframes))

def test_NestedFrames(driver):
    driver.get('https://demoqa.com/nestedframes')
    driver.switch_to.frame("frame1")    # parent frame
    parent_text = driver.find_element(By.TAG_NAME, "body").text
    print("Parent Frame text:", parent_text)
    child_frame = driver.find_element(By.TAG_NAME, "iframe")    # child frame
    driver.switch_to.frame(child_frame)
    child_text = driver.find_element(By.TAG_NAME, "p").text
    print("Child Frame text:", child_text)
    time.sleep(3)
    driver.switch_to.parent_frame()     # Child Frame -> Parent Frame    
    driver.switch_to.default_content()

def test_Frames_Switch(driver):
    driver.get('https://demoqa.com/frames')
    driver.switch_to.frame("frame1")  # Switch to Frame 1
    text1 = driver.find_element(By.ID, "sampleHeading").text
    print('Frame 1',text1)
    driver.switch_to.default_content() # Come back to main page
    driver.switch_to.frame("frame2") # Switch to Frame 2
    text2 = driver.find_element(By.ID, "sampleHeading").text
    print("Frame 2:", text2)
    driver.switch_to.default_content() # Come back to main page