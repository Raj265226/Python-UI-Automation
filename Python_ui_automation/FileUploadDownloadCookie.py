import os
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
    
def test_File_upload(driver):
    driver.get("https://demoqa.com/upload-download")
    upload = driver.find_element(By.ID, "uploadFile")
    file_path = os.path.abspath("File_for_Test/sampleFile.jpeg")
    upload.send_keys(file_path)

def test_File_download(driver):
    driver.get("https://demoqa.com/upload-download")
    driver.find_element(By.ID, "downloadButton").click() # Click Download button

def test_Cookie(driver):
    driver.get("https://demoqa.com")
    cookies = driver.get_cookies()
    print('First cookie', cookies)
    print("Total Cookies:", len(driver.get_cookies()))
    driver.add_cookie({
    "name": "TestCookie",
    "value": "Rohit123"})
    print(driver.get_cookie("TestCookie"))
    driver.delete_cookie("TestCookie")
    driver.delete_all_cookies()
    print('After delete cookie',driver.get_cookies())
    time.sleep(10)