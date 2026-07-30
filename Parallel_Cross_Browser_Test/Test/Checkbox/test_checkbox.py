from selenium.webdriver.common.by import By

class TestCheckbox:

    def test_select_one_checkbox(self, driver):
        driver.get("https://demoqa.com/checkbox")
        driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
        desktop = driver.find_element(By.XPATH,"//span[@title='Desktop']/preceding-sibling::span[@role='checkbox']")
        desktop.click()

    def test_select_multiple_checkbox(self, driver):
        driver.get("https://demoqa.com/checkbox")
        driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
        values = ["Desktop", "Documents", "Downloads"]
        for value in values:
            driver.find_element(By.XPATH,f"//span[@title='{value}']/preceding-sibling::span[@role='checkbox']").click()

    def test_unselect_checkbox(self, driver):
        driver.get("https://demoqa.com/checkbox")
        driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
        desktop = driver.find_element(By.XPATH,"//span[@title='Desktop']/preceding-sibling::span[@role='checkbox']")
        desktop.click()

    def test_verify_checkbox_result(self, driver):
        driver.get("https://demoqa.com/checkbox")
        driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
        driver.find_element(By.XPATH,"//span[@title='Desktop']/preceding-sibling::span[@role='checkbox']").click()
        result = driver.find_element(By.ID, "result").text
        assert "desktop" in result