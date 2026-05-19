from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabTestsPage:

    VITAL_ORGANS = (
        By.XPATH,
        "//h3[contains(text(),'Vital Organs')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_lab_tests_page(self):

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("lab-tests")
        )

        assert "lab-tests" in self.driver.current_url

    def select_vital_organs(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.VITAL_ORGANS
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