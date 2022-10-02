from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.utils import random_str, random_number


class TestStartPage:

    def test_registration_form(self):
        """
        *Registration with random username and email
        - Create driver
        - Open page
        - Fill login
        - Fill email
        - Fill password
        - Click button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\QA_IGOR2022\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = random_str(10)
        login_value = f"{login}"
        user_login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        user_login.send_keys(login_value)
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        email_value = f"{random_str(6)}{random_number()}@gmail.com"
        email.send_keys(email_value)
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        password_value = f"{random_str(12)}"
        password.send_keys(password_value)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Successful registration check
        success_reg = driver.find_element(by=By.XPATH, value=".//span[@class='text-white mr-2']")
        assert login.lower() == f"{success_reg.text}"
        sleep(1)

    def test_second_registration(self):
        """
        - Create driver
        - Open page
        - Fill login (login that already been used)
        - Fill email (email that already been used)
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
        login.send_keys("testQA")
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        email.send_keys("testQA@gmail.com")
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        password_value = f"{random_str(12)}"
        password.send_keys(password_value)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Username error expect
        username_error = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
        assert username_error.text == "The username is already taken."
        sleep(1)

        # Email error expect
        email_error = driver.find_element(by=By.XPATH, value=".//*[@id='registration-form']/div[2]")
        assert email_error.text == "The email is already being used."
        sleep(1)

    def test_logout_check(self):
        """
        # Checking log out button
       - Create driver
       - Open page
       - Fill login
       - Fill password
       - Click button
       - Click on log out button
       - Verify success
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\QA_IGOR2022\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = random_str(10)
        login_value = f"{login}"
        user_login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        user_login.send_keys(login_value)
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        email_value = f"{random_str(6)}{random_number()}@gmail.com"
        email.send_keys(email_value)
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        password_value = f"{random_str(12)}"
        password.send_keys(password_value)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Click log out button
        button = driver.find_element(by=By.XPATH, value=".//button[@class='btn btn-sm btn-secondary']")
        button.click()
        sleep(1)

        # Check of existing SIGNIN button
        success_reg_nam = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        assert success_reg_nam.text == "Sign up for OurApp"
        sleep(1)

    #
    def test_login_with_wrong_data(self):
        """
        #Checking username with 2 and 31 symbols

       - Create driver
       - Open page
       - Fill login (2 symbols)
       - Verify error
       - Fill login (31 symbols)
       - Verify error
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\QA_IGOR2022\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = random_str(2)
        login_value = f"{login}"
        user_login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        user_login.send_keys(login_value)
        sleep(1)

        # Check username amount of symbols
        check_username = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert check_username.text == "Username must be at least 3 characters."

        # Clear username field and fill with 31 symbols
        login = random_str(31)
        login_value = f"{login}"
        user_login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        user_login.send_keys(login_value)
        sleep(1)

        # Check username amount of symbols
        check_username = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert check_username.text == "Username cannot exceed 30 characters."

    def test_password_with_wrong_data(self):
        """
        #Checking password with 4 and 51 symbols
       - Create driver
       - Open page
       - Fill password (4 symbols)
       - Verify error
       - Fill password 51 symbols)
       - Verify error
           """

        # Create driver
        driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\QA_IGOR2022\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        password_value = f"{random_str}"
        password.send_keys(password_value)
        sleep(1)

        # Check password amount of symbols
        check_username = driver.find_element(by=By.XPATH, value=".//*[@id='registration-form']/div[3]/div")
        assert check_username.text == "Password must be at least 12 characters."

        # Clear password field and fill with 51 symbols
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        password_value = f"{random_str}"
        password.send_keys(password_value)
        sleep(1)

        # Check password amount of symbols
        check_password = driver.find_element(by=By.XPATH, value=".//*[@id='registration-form']/div[3]/div")
        assert check_password.text == "Password cannot exceed 50 characters."
