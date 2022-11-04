#https://git-scm.com/download/win
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions

from pyjavaproperties import Properties


class BaseTest:
    @pytest.fixture(autouse=True)
    def init_driver(self):
        pfile=Properties()
        #open the property file
        pfile.load(open("../config.properties"))
        #pfile.load(open('../config.properties'))
        # get the value by specifying the key
        browser = pfile['browser']
        url = pfile["url"]
        implicittimeout = pfile['implicittimeout']
        explicittimeout = pfile['explicittimeout']
        usergrid = pfile['usegrid']
        gridurl =pfile['gridurl']

        if usergrid == 'no':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print("launched chrome browser")
            else:
                self.driver = webdriver.firefox(service=Service(GeckoDriverManager().install()))
                print("launched firefox browser")
        else:
            if browser == 'chrome':
                browseroptions = ChromeOptions()
                print("launched chrome browser in remote system")
            else:
                browseroptions = FirefoxOptions()
                self.driver = webdriver.remote(gridurl)
                print("launched chrome browser in remote system")
            self.driver = webdriver.Remote(gridurl,options=browseroptions)

        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(implicittimeout)
        self.wait = WebDriverWait(self.driver,explicittimeout)
        yield
        self.driver.close()