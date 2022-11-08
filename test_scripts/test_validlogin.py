import time

import pytest

from generic.base_test import BaseTest
from generic.exlutility import Excel
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestValidLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_validlogin(self):
        userName = Excel.get_cellValue("data/Book3.xlsx","ValidLogin",2,1)
        passWord = Excel.get_cellValue("data/Book3.xlsx", "ValidLogin", 2, 2)
        loginpage = LoginPage(self.driver)
        loginpage.set_username(userName)
        loginpage.set_password(passWord)
        loginpage.click_loginbutton()
        time.sleep(5)
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_display(self.wait)
        assert result
