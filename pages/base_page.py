from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):  # test_second_registration
        """Clear and fil the field"""
        login = self.driver.find_element(by=By.XPATH, value=xpath)
        login.send_keys("testQA")
