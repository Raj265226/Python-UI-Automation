import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_broken_links(driver):
    driver.get("https://demoqa.com/links")
    links = driver.find_elements(By.TAG_NAME, "a")
    broken_links = []
    for link in links:
        url = link.get_attribute("href")
        if url:
            try:
                response = requests.get(url, timeout=10)
                print(f"{url} ---> {response.status_code}")
                if response.status_code >= 400:
                    broken_links.append(url)
                    print(f"Broken Link: {url}")
            except Exception as e:
                print(f"Error: {url}")
                print(e)
    print("Number of Broken Links:", len(broken_links))
    print("Broken Links List:", broken_links)