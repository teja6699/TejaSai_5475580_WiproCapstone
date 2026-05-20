import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VitalOrgansPage:

    THYROID_CARD = (
        By.XPATH,
        "//p[contains(text(),'Thyroid')]"
    )

    ADD_BUTTON = (
        By.XPATH,
        "/html/body/main/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/button/span"
    )

    GO_TO_CART = (
        By.XPATH,
        "/html/body/main/div[2]/div/div/div[2]/div/div/div[2]/button[2]"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@name='mobileNumber']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Continue')]"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[text()='Verify']"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_vital_organs_page(self):

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("vital-organs")
        )

        print("Current URL:", self.driver.current_url)

    def open_thyroid_card(self):

        thyroid = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.THYROID_CARD
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            thyroid
        )

        self.driver.execute_script(
            "arguments[0].click();",
            thyroid
        )

    def click_add_button(self):

        add_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.ADD_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            add_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        print("Add button clicked successfully")

    def click_go_to_cart(self):
        time.sleep(3)

        go_to_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.GO_TO_CART
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            go_to_cart
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            go_to_cart
        )

        print("Go To Cart button clicked successfully")

        time.sleep(5)

    def login_with_mobile(self):
        print("Waiting for login popup...")

        time.sleep(5)

        phone_input = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                self.PHONE_INPUT
            )
        )

        phone_input.click()

        phone_input.clear()

        phone_input.send_keys("9381866215")

        print("Mobile number entered successfully")

        # Wait for button enable
        time.sleep(5)

        continue_btn = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            continue_btn
        )

        time.sleep(3)

        # JS click
        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

        print("Continue button clicked")

        print("Waiting 30 seconds for manual OTP entry...")

        time.sleep(30)

    def click_verify_button(self):
        print("Waiting for manual OTP entry...")

        # Wait for user to enter OTP manually
        time.sleep(30)

        verify_btn = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                self.VERIFY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            verify_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            verify_btn
        )

        print("Verify button clicked successfully")

        time.sleep(10)