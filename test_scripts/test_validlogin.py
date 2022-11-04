import time

from generic.base_test import BaseTest
from generic.exlutility import Excel
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestValidLogin(BaseTest):

    def test_validlogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_username("admin")
        loginpage.set_password("mwanager")
        loginpage.click_loginbutton()
        time.sleep(5)
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_display(self.wait)
        assert result


