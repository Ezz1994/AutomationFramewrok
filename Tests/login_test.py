import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Utilis import utils as utils
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.login()
        assert "OrangeHRM" in driver.title

    def test_logut(self):

     try:
        driver = self.driver
        homepage=HomePage(driver)
        homepage.click_accountsettingsdropdown()
        homepage.click_logout()
        x = driver.title
        assert x =="444"

     except AssertionError as error:
         print("There was an exception")
         print(error)
         currTime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
         screenshotName="screenshot"+currTime
         allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                       attachment_type=allure.attachment_type.PNG)
         #driver.get_screenshot_as_file("C:/Users/user/PycharmProjects/AutomationFramewrok/Screenshots/"+"image"+".png")
         raise

     else:
         print("no exceptions")

     finally:
         print("no exception occurred")

     # except :
     #     print("There was an exception")
     #     raise


