from selenium.webdriver.common.by import By

class TestLogin:

    def test_valid_login(self, driver):
        driver.get("https://demoqa.com/text-box")
        username = driver.find_element(By.ID, "userName")
        username.send_keys("Rohit")
        assert username.get_attribute("value") == "Rohit"

    def test_invalid_login(self, driver):
        driver.get("https://demoqa.com/text-box")
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys("wrongemail")
        assert email.get_attribute("value") == "wrongemail"

    def test_blank_login(self, driver):
        driver.get("https://demoqa.com/text-box")
        username = driver.find_element(By.ID, "userName")
        assert username.is_displayed()