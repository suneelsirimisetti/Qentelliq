from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HomePage:
    __logout = (By.ID, "logoutLink")


    def __init__(self, driver):
        self.__driver = driver

    def verify_homepage_is_display(self,wait):
        try:
            wait.until(ec.visibility_of_element_located(self.__logout))
            print("home page is displayed")
            return True
        except:
            print("home page is not displayed")
            return False