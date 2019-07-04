from cases.case_login import Login
import unittest
import time

class XbList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=Login().login()
        cls.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-dark ant-menu-root']/li[2]").click()
        time.sleep(5)

    def test_keepinsurance(self):
        self.driver.get("http:/gap/keepinsurance")
        time.sleep(5)

    def test_insurancefirsttrial(self):
        self.driver.get("http:/gap/insurancefirsttrial")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

