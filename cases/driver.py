from selenium import webdriver

class Driver:
    def get_driver(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)

        return self.driver

