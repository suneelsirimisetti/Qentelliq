from generic.base_test import BaseTest
from generic.exlutility import Excel

class TestScript1(BaseTest):

    def test_script1(self):
        print("This is my script")
        print(self.driver.title)
        vdata = Excel.get_cellValue("../data/Book3.xlsx","Sheet1",2,1)
        print(vdata)