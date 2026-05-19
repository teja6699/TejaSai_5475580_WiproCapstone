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