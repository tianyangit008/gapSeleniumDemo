from cases.driver import Driver
import time
import unittest

class Login(unittest.TestCase):
    """保险系统"""
    def test_login(self):
        """登录"""
        driver=Driver().get_driver()
        driver.get("http:")
        driver.maximize_window()

        driver.switch_to_frame(0)
        driver.find_element_by_xpath("//ul[@id='loginNav']/li[2]").click()
        driver.find_element_by_name("username").send_keys("tianyan")
        driver.find_element_by_name("pwd").send_keys("*********")
        driver.find_element_by_xpath("//button[@class='login-btn onsign']").click()

        time.sleep(5)
        return driver


if __name__=="__main__":
    Login().login()
