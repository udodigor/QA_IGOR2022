import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_incorrect_login(self):
        """
        - Create driver
        - Open page
        - Fill login
        - Fill password
        - Click button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\QA_IGOR2022\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        random_loging = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        login.send_keys(random_loging)
        sleep(3)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        random_email = random_loging + "@gmail.com"
        email.send_keys(random_email)
        sleep(3)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        random_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
        password.send_keys(random_password)
        sleep(3)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(3)

        # Successful registration check
        success_reg_nam = driver.find_element(by=By.XPATH, value=".//span[@class='text-white mr-2']")
        assert success_reg_nam.text == f"{random_loging}", f"Actual message: {success_reg_nam.text}"
        sleep(3)

# Add new text to text 22222222
