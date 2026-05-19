from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    LAB_TESTS = (
        By.XPATH,
        "//a[contains(@href,'lab-tests')]"
    )

    POPUP_CLOSE = (
        By.XPATH,
        "//button[contains(@class,'close')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):

        self.driver.get(
            "https://www.apollopharmacy.in/"
        )

    def verify_home_page(self):

        assert "Apollo" in self.driver.title

    def close_popup_if_present(self):

        try:

            popup = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    self.POPUP_CLOSE
                )
            )

            popup.click()

        except:
            pass

    def click_lab_tests(self):

        self.close_popup_if_present()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.LAB_TESTS
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )