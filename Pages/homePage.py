from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self,driver):
        self.driver =driver

        self.accountsettingsdropdown="//header/div[1]/div[2]/ul[1]/li[1]/span[1]"
        self.logoutbutton ="//a[contains(text(),'Logout')]"

    def click_accountsettingsdropdown(self):
        self.driver.find_element(By.XPATH, self.accountsettingsdropdown).click()
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logoutbutton).click()