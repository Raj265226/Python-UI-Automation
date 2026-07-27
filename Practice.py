xpath syntax - //tagname[@attribute='value']
HTML Code                                                                       XPATH
<a> House</a>                                              //a[normalize-space(text())='House']
<input type=' radio' name="xyz">                           //input[normalize-space(@type)='radio']
<input type='radio' name="xyz">                            //input[@type='radio' and @name='xyz']
<a>Home</a>                                                //a[contains(text(),'Home')]

<div class='pqr'>
<div class='abc'><p>Hello1</p></div>
<div class='abc'><p>Hello2</p></div>   -- Select this      //div[@class='pqr']/child::div[2]
<div class='abc'><p>Hello3</p></div>                       //div[@class='pqr']/child::div[3]/preceding-sibling::div[1]
</div>

<table>
<tr>
<td>Name</td>
<td>Gender</td>
<td>AdharId</td>
</tr>
 <tr>
<td>Rohit</td>  -- Select this                             //td[text()='26']/preceding-sibling::td[1]
<td>91</td>                                                //td[text()='26']/parent::tr/td[1]
<td>26</td>                                                //td[text()='26']/ancestor::tr/td[1]
</tr>
</table>
                                Code Part
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager # pip install selenium webdriver-manager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.guru99.com/")
driver.maximize_window()
driver.implicitly_wait(3)  # Implicit wait
print(driver.title)  # Print title
            # Explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
driver.get("https://automationtesting.in/")
            # Navigation Command
driver.back()
driver.forward()
            # Links
links=driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.text)
            # Dropdown
select_dropdown=driver.find_element(By.XPATH,"XYZ")
drp=Select(select_dropdown)
all_options=drp.options
for option in all_options:
    print(option)
drp.select_by_index(2)  # Select 2nd value
            # Alerts
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
            # Frames
driver.switch_to.default_content()
driver.switch_to.frame("ABC")   # Select frame using iframe name
            # Window Handle
new_window=driver.find_element(By.XPATH,"xyz")
print(driver.current_window_handle)   # Id for new window
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)             # List of windows title
    if driver.title=="asd":
        driver.close()              # Close the other window
            # Scroll
driver.execute_script("window.scrollBy(0, 100);")   # Scroll down 100 pixels
element = driver.find_element("id", "element-id")   # Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scroll to the page end
           # ActionChains
admin=driver.find_element(By.XPATH,"qwe")
subadmin=driver.find_element(By.XPATH,"asd")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(subadmin).click().perform()    # Hover
actions.double_click(admin).perform()       # Double Click
actions.context_click(admin).perform()      # Right Click
actions.drag_and_drop(admin,subadmin).perform()     # Drag and Drop
        # Cookies
cookies=driver.get_cookies()
cookie={'name':'Rohit','value':'123'}
driver.add_cookie(cookie)               # Add Cookie
driver.delete_cookie('ubid-acbin')      # Delete single Cookie
driver.delete_all_cookies()             # Delete All Cookies
       # Screenshot
driver.save_screenshot("path.png")
driver.get_screenshot_as_file("path.png")

                            # BDD
1.Create directory - features
2.Create sub-directory on features - steps
3.Create feature file using under feature directory .feature - workflow.feature
4.Write code on workflow.feature then use command behave <path> then code will generate
5.Create python file under steps - workflow.py and paste the generated code from workflow.feature
6.Run code from workflow.feature it will run workflow.py file
Feature file -
Feature: Create Shop
  Scenario: Create Shop with proper data
    Given Launch Chrome Browser
    When Open Faretrack and enter data
    Then Verify that Shop is creating
Python File -
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('Launch Chrome Browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@when('Open Faretrack and enter data')
def ValidShopdataEntered(context):
    context.driver.find_element(By.XPATH, "//input[(@name='username')]").send_keys("xyz@xyz.in")

@then('Verify that Shop is creating')
def VerifyCreatedShop(context):
    try:
        WebDriverWait(context.driver, 300).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='modal-box MuiBox-root css-0']")))
    except NoSuchElementException:
        print("Modal is not visible within the given time frame.")

Background Feature -
Feature: OrangeHRM Login

  Background: common steps
    Given  I Launch browser
    When  I open application
    And  Enter valid username and password
    And  Click on login

  Scenario:  Login to HRM Applicaion
    Then User must login to the Dashboard page

  Scenario:  Search User
    When  navigate to search page
    Then  search page should display

Outline Feature -
Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I Open orange hrm homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When I Open orange hrm homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |

Python File -
from behave import *
from selenium import webdriver

@given('I launch chrome browser')
def Launch_Browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when('I Open orange hrm homepage')
def OpenHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')   # To make params into arguments we need to curly braces {}
def EnterUserPwd(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

                            # Unit-test
import unittest

class Apptest(unittest.TestCase):

    @classmethod                        # This will run first
    def setUpClass(cls):
        print("SetUp Class")

    @classmethod                        # This will run last
    def tearDownClass(cls):
        print("TearDown Class")

    def setUp(self):                    # This will run on every testcases
        print("Setup Method")

    def test_one(self):
        print("Test One")

    @unittest.skip("This is for test two")              # This is to skip test
    def test_two(self):
        print("Test Two")

    def test_three(self):
        print("Test Three")

    def tearDown(self):                 # This will run on every testcases
        print("Teardown method")

if __name__ == "__main__":
    unittest.main()

                            # POM and Batch Testing
1.Create Python Package unitTest_Flow
2.Create Python Package pageObjects. Here only page element is defined. Also defined constructor and initiate driver to
local variable.
3.Create Python Package TestSuites for Batch Test only
Structure -
POM_Rateshop
    pageObjects
        login.py
    unitTest_Flow
        login_test.py
    TestSuites
        testSuites.py
login.py -
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username_xpath = "//input[@name='handle']"
    password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.button_login_xpath)))
        element.click()

login_test.py -
import unittest
import time
import HtmlTestRunner           # For HTML Report
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import sys
sys.path.append("/home/ai/Python projects/POM_rateshop")  # Instead path set in env variable, It's defined
from PageObjects.login import LoginPage
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):
    driver = None
    baseUrl = "https://rateshops-dashboard-stg.aggregateintelligence.com/login"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def test_Login(self):
        self.driver.get(self.baseUrl)
        self.username = "admin"
        self.password = "admin"
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)

    def test_LoginWIthInvalid(self):
        self.driver.get(self.baseUrl)
        self.username = "xyz"
        self.password = "xyz"
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))  # Generate HTML Report

testSuites.py -                 # Batch Testing
import unittest
import sys
sys.path.append("/home/ai/Python projects/POM_rateshop")
from unitTest_Flow.login_test import LoginTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create Test suites
sanityTestSuite = unittest.TestSuite([tc1])  # Sanity test suite
unittest.TextTestRunner().run(sanityTestSuite)
                                # Pytest
1.Package name must be started with keyword test
2.myPack here is python package
Structure -
    myPack
        test_Package1.py
        test_Package2.py
test_Package1.py -
import pytest
import allure

@pytest.fixture()
def setup():
    print("test setup1")
    yield
    print("test after setup1")

def test_method11(setup):
    print("test method 11")

def test_method21(setup):
    print("test method 21")
test_Package2.py -
import pytest

@pytest.fixture()
def setup():
    print("test setup2")
    yield
    print("test after setup2")

@pytest.mark.sanity
def test_method1(setup):
    print("test method 12")

def test_method2(setup):
    print("test method 22")
Command to run -
pytest -v -s myPack/                                            # Run both packages
pytest -v -s myPack/test_Package1.py::test_method11             # Run single function inside Package1
pytest -v -s myPack/ --html=report.html --self-contained-html   # Generate html report as well
pytest -v -s -m "sanity" pytest1.py                             # To run only marked with sanity
pytest -v -s --alluredir="Test Report" myPack/                  # Report will generate in Test Report
allure serve Test\ Report/                                      # Open The report in Allure Framework

[pytest]                        -- pytest.ini        # use for markers
markers =
            sanity
            regression

                                # Data Driven Framework
Structure -
DataDrivenUsingExcel
    XLUtils.py
    DataDrivenTestCase.py
XLUtils.py -
import openpyxl

def getRowCount(file,sheetname):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetname)
    return (sheet.max_row)

def getColumnCount(file,sheetname):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetname)
    return (sheet.max_column)

def readData(file,sheetname,rownum,columnnum):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetname)
    return sheet.cell(row=rownum, column=columnnum).value

def WriteData(file,sheetname,rownum,columnnum,data):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetname)
    sheet.cell(row=rownum, column=columnnum).value = data
    workbook.save(file)
DataDrivenTestCase.py -
import time

import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "Files/Login.xlsx"

rows = XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    driver = webdriver.Chrome(service=Service("Files/chromedriver"))
    driver.get("https://rateshops-dashboard-stg.aggregateintelligence.com/login")
    driver.maximize_window()
    time.sleep(2)
    username = XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.XPATH, "//input[@name='handle']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    try:
        text = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[3]/a").text
        if text == "Sources Master":
            XLUtils.WriteData(path, 'Sheet1', r, 3, "Passed")
            driver.quit()
        else:
            XLUtils.WriteData(path, 'Sheet1', r, 3, "Failed")
            driver.quit()

    except:
        XLUtils.WriteData(path,'Sheet1',r,3,"Failed")
        driver.quit()

                    PYTEST PARAMETERIZE
@pytest.mark.parametrize("username,password", [("usr1","pwd1"),("usr2","pwd2"),("usr3","pwd3")])
def test_with_dynamic_values(username, password):
    print(username+"-"+password)
# Parameterize is a default marker of pytest