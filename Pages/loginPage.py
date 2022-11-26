from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self ,driver):
        self.driver=driver

        self.username_txtbox="//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]"
        self.password_txtbox="//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]"
        self.loginbutton = "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]"

    def enter_username(self , username):
        self.driver.find_element(By.XPATH,
                            self.username_txtbox).send_keys(
            username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,
                                 self.password_txtbox).send_keys(
            password)
    def login(self):
        self.driver.find_element(By.XPATH,self.loginbutton).click()
