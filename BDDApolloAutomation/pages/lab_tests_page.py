from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabTestsPage:

    VITAL_ORGANS = (
        By.XPATH,
        "//*[@id='mainContainerCT']/div[1]/div[6]/header/a"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_lab_tests_page(self):

        assert "lab-tests" in self.driver.current_url

    def select_vital_organs(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.VITAL_ORGANS
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )