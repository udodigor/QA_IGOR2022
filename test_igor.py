import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_1_registration(self):
        """
        *Registration with random username and email
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
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        random_email = random_loging + "@gmail.com"
        email.send_keys(random_email)
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        random_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
        password.send_keys(random_password)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Successful registration check
        success_reg = driver.find_element(by=By.XPATH, value=".//span[@class='text-white mr-2']")
        assert success_reg.text == f"{random_loging}", f"Actual message: {success_reg.text}"
        sleep(1)

    #
    def test_2_registration_2(self):
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
        login.send_keys("testQA")
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        email.send_keys("testQA@gmail.com")
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        random_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
        password.send_keys(random_password)
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

    def test_3_logout(self):
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
        login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        random_loging = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        login.send_keys(random_loging)
        sleep(1)

        # Fill Email
        email = driver.find_element(by=By.XPATH, value='.//input[@placeholder="you@example.com"]')
        random_email = random_loging + "@gmail.com"
        email.send_keys(random_email)
        sleep(1)

        # Fill Password
        password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
        random_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
        password.send_keys(random_password)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Successful registration check
        success_reg_nam = driver.find_element(by=By.XPATH, value=".//span[@class='text-white mr-2']")
        assert success_reg_nam.text == f"{random_loging}", f"Actual message: {success_reg_nam.text}"
        sleep(1)

        # Click log out button
        button = driver.find_element(by=By.XPATH, value=".//button[@class='btn btn-sm btn-secondary']")
        button.click()
        sleep(1)

        success_reg_nam = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        assert success_reg_nam.text == "Sign up for OurApp"
        sleep(1)

    def test_4(self):
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
        login = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Pick a username"]')
        login.send_keys('re')
        sleep(1)

        # Check username amount of symbols
        check_username = driver.find_element(by=By.XPATH,
                                             value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert check_username.text == "Username must be at least 3 characters."

        # Clear username field and fill with 31 symbols
        login.clear()
        login.send_keys('testQAtestQAtestQAtestQAtestQA1')

        # Check username amount of symbols
        check_username = driver.find_element(by=By.XPATH,
                                             value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert check_username.text == "Username cannot exceed 30 characters."

    def test_5(self):
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

    # # Fill password
    password = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Create a password"]')
    password.send_keys('1234')
    sleep(1)

    # Check password amount of symbols
    check_username = driver.find_element(by=By.XPATH, value=".//*[@id='registration-form']/div[3]/div")
    assert check_username.text == "Password must be at least 12 characters."

    # Clear password field and fill with 51 symbols
    password.clear()
    password.send_keys('testQAtestQAtestQAtestQAtestQAtestQAtestQAtestQA123')

    # Check password amount of symbols
    check_password = driver.find_element(by=By.XPATH, value=".//*[@id='registration-form']/div[3]/div")
    assert check_password.text == "Password cannot exceed 50 characters."
