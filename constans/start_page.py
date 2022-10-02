class StartPage:
    # Sign up
    SIGN_UP_USERNAME_FIELD_XPATH = './/input[@placeholder="Pick a username"]'
    SIGN_UP_PASSWORD_FIELD_XPATH = './/input[@placeholder="Create a password"]'
    SIGN_UP_EMAIL_FIELD_XPATH = './/input[@placeholder="Create a password"]'
    SIGN_UP_FOR_OUR_APP_BUTTON_XPATH = ".//button[@type='submit']"

    SIGN_UP_USERNAME_IS_TAKEN_TEXT = "The username is already taken."
    SIGN_UP_EMAIL_IS_TAKEN_TEXT = "The email is already being used."
    SIGN_UP_NO_MORE_THEN_30_TEXT = "Username cannot exceed 30 characters."
    SIGN_UP_NO_LESS_THEN_3_TEXT = "Username must be at least 3 characters."

    # Sign up verification text (Login == text of logged user)
    SIGN_UP_VERIFICATION_SUCCESS_XPATH = ".//span[@class='text-white mr-2']"

    # Checks - wrong Login and Email message after entering (email and login is already taken)
    WRONG_LOGIN_IS_TAKEN_XPATH = ".//div[@class='alert alert-danger small']"
    WRONG_EMAIL_IS_TAKEN_XPATH = ".//*[@id='registration-form']/div[2]"

    # Logout button
    LOGOUT_BUTTON_XPATH = ".//button[@class='btn btn-sm btn-secondary']"

    # Wrong amount of text in the USERNAME field 4 and 31
    WRONG_MIN_AMOUNT_OF_LOGIN_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    WRONG_MAX_AMOUNT_OF_LOGIN_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
