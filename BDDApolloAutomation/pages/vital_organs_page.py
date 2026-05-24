import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException
)


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

    PATIENT_CHECKBOX = (
        By.CSS_SELECTOR,
        ".DiagItemAccordionPatient_checkbox__Rz7Wh label"
    )

    SELECT_SLOT_BUTTON = (
        By.XPATH,
        "//button[text()='Select Slot']"
    )

    REVIEW_CART_BUTTON = (
        By.XPATH,
        "//button[text()='Review Cart']"
    )

    PROCEED_TO_PAY = (
        By.XPATH,
        "//button[contains(.,'Proceed to Pay')]"
    )

    CREDIT_DEBIT_CARD = (
        By.XPATH,
        "//button[contains(.,'Credit/Debit Cards')]"
    )

    PAY_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Pay')]"
    )

    def __init__(self, driver):

        self.driver = driver

    # --------------------------------------------------
    # SAFE CLICK METHOD
    # --------------------------------------------------

    def safe_click(self, locator):

        for attempt in range(3):

            try:

                element = WebDriverWait(
                    self.driver,
                    30
                ).until(
                    EC.element_to_be_clickable(
                        locator
                    )
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                time.sleep(2)

                try:

                    element.click()

                except:

                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                return

            except StaleElementReferenceException:

                print(
                    f"Retrying click for {locator}"
                )

                time.sleep(2)

    # --------------------------------------------------
    # OPEN THYROID CARD
    # --------------------------------------------------
    @allure.step("Open Thyroid Card")
    def open_thyroid_card(self):

        time.sleep(5)

        self.safe_click(
            self.THYROID_CARD
        )

        print(
            "Thyroid card opened successfully"
        )

    # --------------------------------------------------
    # CLICK ADD BUTTON
    # --------------------------------------------------
    @allure.step("Click Add Button")
    def click_add_button(self):

        time.sleep(3)

        self.safe_click(
            self.ADD_BUTTON
        )

        print(
            "Add Button clicked successfully"
        )

    # --------------------------------------------------
    # CLICK GO TO CART
    # --------------------------------------------------
    @allure.step("Go to cart")
    def click_go_to_cart(self):

        time.sleep(5)

        self.safe_click(
            self.GO_TO_CART
        )

        print(
            "Go To Cart clicked successfully"
        )

    # --------------------------------------------------
    # LOGIN WITH MOBILE
    # --------------------------------------------------
    @allure.step("Login with mobile")
    def login_with_mobile(
            self,
            mobile_number
    ):

        print(
            "Waiting for login popup..."
        )

        phone = WebDriverWait(
            self.driver,
            40
        ).until(
            EC.presence_of_element_located(
                self.PHONE_INPUT
            )
        )

        phone.clear()

        phone.send_keys(
            str(mobile_number)
        )

        print(
            "Mobile number entered successfully"
        )

        time.sleep(3)

        continue_button = WebDriverWait(
            self.driver,
            40
        ).until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print(
            "Continue button clicked"
        )

    # --------------------------------------------------
    # VERIFY OTP
    # --------------------------------------------------
    @allure.step("Verify OTP")
    def click_verify_button(self):

        print(
            "Waiting 30 seconds for manual OTP..."
        )

        time.sleep(30)

        verify_button = WebDriverWait(
            self.driver,
            40
        ).until(
            EC.element_to_be_clickable(
                self.VERIFY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            verify_button
        )

        print(
            "Verify button clicked successfully"
        )

    @allure.step("Select patient")
    def select_patient_checkbox(self):

        time.sleep(5)

        self.safe_click(
            self.PATIENT_CHECKBOX
        )

        print("Patient checkbox selected")

    @allure.step("Select Slot")
    def click_select_slot_button(self):

        time.sleep(5)

        self.safe_click(
            self.SELECT_SLOT_BUTTON
        )

        print("Select Slot clicked")

    @allure.step("Review Cart")
    def click_review_cart_button(self):

        time.sleep(5)

        self.safe_click(
            self.REVIEW_CART_BUTTON
        )

        print("Review Cart clicked")

    @allure.step("Proceed to pay")
    def click_proceed_to_pay(self):

        time.sleep(5)

        self.safe_click(
            self.PROCEED_TO_PAY
        )

        print("Proceed To Pay clicked")

    @allure.step("click credit card")
    def click_credit_debit_card_section(self):

        time.sleep(5)

        self.safe_click(
            self.CREDIT_DEBIT_CARD
        )

        print("Credit/Debit Card section clicked")

    @allure.step("Enter card details")
    def enter_card_details(

            self,
            card_name,
            card_number,
            expiry_date,
            cvv
    ):

        time.sleep(10)

        iframes = self.driver.find_elements(
            By.TAG_NAME,
            "iframe"
        )

        print(
            "Total iframes:",
            len(iframes)
        )

        # NAME FIELD
        for iframe in iframes:

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(
                    iframe
                )

                fields = self.driver.find_elements(
                    By.ID,
                    "name_on_card"
                )

                if fields:
                    fields[0].send_keys(
                        str(card_name)
                    )

                    print("Card Name entered")

                    break

            except:
                pass

        # CARD NUMBER
        for iframe in iframes:

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(
                    iframe
                )

                fields = self.driver.find_elements(
                    By.NAME,
                    "card_number"
                )

                if fields:
                    fields[0].send_keys(
                        str(card_number)
                    )

                    print("Card Number entered")

                    break

            except:
                pass

        # EXPIRY
        for iframe in iframes:

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(
                    iframe
                )

                fields = self.driver.find_elements(
                    By.NAME,
                    "expiry_date"
                )

                if fields:

                    expiry_field = fields[0]

                    expiry_field.click()

                    time.sleep(1)

                    for digit in str(expiry_date):
                        expiry_field.send_keys(
                            digit
                        )

                    print("Expiry entered")

                    break

            except:
                pass

        # CVV
        for iframe in iframes:

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(
                    iframe
                )

                fields = self.driver.find_elements(
                    By.NAME,
                    "security_code"
                )

                if fields:
                    fields[0].send_keys(
                        str(cvv)
                    )

                    print("CVV entered")

                    break

            except:
                pass

        self.driver.switch_to.default_content()

        print("Card details entered successfully")

    @allure.step("Click pay")
    def click_pay_button(self):

        time.sleep(5)

        self.safe_click(
            self.PAY_BUTTON
        )

        print("Pay button clicked")