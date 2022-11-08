import pytest

from generic.base_test import BaseTest
from pages.login_page import LoginPage


class TestInvalidLogin(BaseTest):
    @pytest.mark.run(order=2)
    def test_invalidlogin(self):
        loginPage = LoginPage(self.driver)
        loginPage.set_username("admin")
        loginPage.set_password("manager")
        loginPage.click_loginbutton()
        result = loginPage.verify_errmsg_displayed(self.wait)
        assert result
