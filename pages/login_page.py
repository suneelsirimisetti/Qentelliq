from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:
    __userName = (By.ID, "username")
    __passWord = (By.NAME, "pwd")
    __loginbutton = (By.XPATH, "//div[.='Login ']")
    __errorMsg = (By.XPATH,"//div[.='Login ']")

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self, un):
        self.__driver.find_element(*self.__userName).send_keys(un)

    def set_password(self, pwd):
        self.__driver.find_element(*self.__passWord).send_keys(pwd)

    def click_loginbutton(self):
        self.__driver.find_element(*self.__loginbutton).click()

    def verify_errmsg_displayed(self,wait):
        try:
            wait.until(ec.visibility_of_element_located(self.__errorMsg))
            print("Err Msg is displayed")
            return True
        except:
            print("Err Msg is not displayed")
            return False
