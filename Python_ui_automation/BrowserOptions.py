from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")  # Headless mode
options.add_argument("--incognito") # incognito mode

options.add_argument("--start-maximized") # Browser arguments
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")

options.add_argument("--ignore-certificate-errors") # SSL Certificate
options.add_argument("--allow-insecure-localhost")

options.set_capability("acceptInsecureCerts", True) # Browser capabilities

download_path = r"C:\Downloads"         # Download preferences
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True

    "profile.default_content_setting_values.notifications": 2 # Disable notifications
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)