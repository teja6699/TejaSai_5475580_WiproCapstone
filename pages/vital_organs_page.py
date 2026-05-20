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

    SELECT_SLOT_BUTTON = (
        By.XPATH,
        "//button[text()='Select Slot']"
    )

    REVIEW_CART_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Review Cart')]"
    )

    PATIENT_CHECKBOX = (
        By.CSS_SELECTOR,
        "div[class*='DiagItemAccordionPatient_checkbox'] input[type='checkbox']"
    )

    PROCEED_TO_PAY_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Proceed to Pay')]"
    )

    CREDIT_DEBIT_CARD_SECTION = (
        By.XPATH,
        "//button[contains(.,'Credit/Debit Cards')]"
    )

    NAME_ON_CARD = (
        By.ID,
        "name_on_card"
    )

    CARD_NUMBER = (
        By.NAME,
        "card_number"
    )

    EXPIRY_DATE = (
        By.NAME,
        "expiry_date"
    )

    CVV = (
        By.NAME,
        "security_code"
    )

    PAY_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Pay')]"
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

    def select_patient_checkbox(self):
        print("Waiting for patient checkbox...")

        checkbox = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                self.PATIENT_CHECKBOX
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            checkbox
        )

        time.sleep(2)

        # JS click because Apollo checkbox is custom React checkbox
        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        print("Patient checkbox selected successfully")

        time.sleep(5)



    def click_select_slot_button(self):
        print("Waiting for Select Slot popup...")

        select_slot_btn = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                self.SELECT_SLOT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            select_slot_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            select_slot_btn
        )

        print("Select Slot button clicked successfully")

        time.sleep(10)

    def click_review_cart_button(self):
        print("Waiting for Review Cart button...")

        # Wait for Apollo React rendering
        time.sleep(8)

        review_cart_btn = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                self.REVIEW_CART_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            review_cart_btn
        )

        # Extra wait for state update
        time.sleep(3)

        self.driver.execute_script(
            "arguments[0].click();",
            review_cart_btn
        )

        print("Review Cart button clicked successfully")

        time.sleep(10)

    def click_proceed_to_pay(self):
        print("Waiting for Proceed To Pay button...")

        proceed_btn = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                self.PROCEED_TO_PAY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            proceed_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            proceed_btn
        )

        print("Proceed To Pay button clicked successfully")

        time.sleep(10)

    def click_credit_debit_card_section(self):
        print("Waiting for Credit/Debit Card section...")

        card_section = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                self.CREDIT_DEBIT_CARD_SECTION
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            card_section
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            card_section
        )

        print("Credit/Debit Card section clicked")

        time.sleep(5)

    def enter_card_details(self):

        print("Waiting for payment iframes...")

        time.sleep(10)

        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

        print("Total iframes found:", len(iframes))

        # -------------------------
        # NAME ON CARD
        # -------------------------

        for index, iframe in enumerate(iframes):

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(iframe)

                fields = self.driver.find_elements(
                    By.ID,
                    "name_on_card"
                )

                if len(fields) > 0:
                    print(f"Name iframe found: {index}")

                    name_field = fields[0]

                    name_field.clear()

                    name_field.send_keys("Teja Sai")

                    print("Entered Name")

                    break

            except:
                pass

        # -------------------------
        # CARD NUMBER
        # -------------------------

        for index, iframe in enumerate(iframes):

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(iframe)

                fields = self.driver.find_elements(
                    By.NAME,
                    "card_number"
                )

                if len(fields) > 0:
                    print(f"Card Number iframe found: {index}")

                    card_field = fields[0]

                    card_field.send_keys(
                        "4111111111111111"
                    )

                    print("Entered Card Number")

                    break

            except:
                pass

        # -------------------------
        # EXPIRY DATE
        # -------------------------

        for index, iframe in enumerate(iframes):

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(iframe)

                fields = self.driver.find_elements(
                    By.NAME,
                    "expiry_date"
                )

                if len(fields) > 0:
                    print(f"Expiry iframe found: {index}")

                    expiry_field = fields[0]

                    expiry_field.click()

                    time.sleep(2)

                    expiry_field.send_keys("1")
                    expiry_field.send_keys("2")
                    expiry_field.send_keys("3")
                    expiry_field.send_keys("0")

                    print("Entered Expiry")

                    time.sleep(3)

                    break

            except:
                pass

        # -------------------------
        # CVV
        # -------------------------

        for index, iframe in enumerate(iframes):

            try:

                self.driver.switch_to.default_content()

                self.driver.switch_to.frame(iframe)

                fields = self.driver.find_elements(
                    By.NAME,
                    "security_code"
                )

                if len(fields) > 0:
                    print(f"CVV iframe found: {index}")

                    cvv_field = fields[0]

                    cvv_field.send_keys("123")

                    print("Entered CVV")

                    break

            except:
                pass

        self.driver.switch_to.default_content()

        print("Card details entered successfully")

        time.sleep(10)


    def click_pay_button(self):
        pay_btn = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                self.PAY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            pay_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            pay_btn
        )

        print("Pay button clicked successfully")

        time.sleep(20)