from cases.case_login import Login
import unittest
import time

class OrderList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Login().login()
        cls.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-dark ant-menu-root']/li[1]").click()
        time.sleep(5)

    def test_orderlist(self):
        """金融订单列表"""
        self.driver.get("http:/gap/halfpayorder")
        time.sleep(5)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# if __name__=="__main__":
#     unittest.main()