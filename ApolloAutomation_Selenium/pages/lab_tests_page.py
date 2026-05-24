from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabTestsPage:

    VIEW_ALL_VITAL_ORGANS = (
        By.XPATH,
        "//*[@id='mainContainerCT']/div[1]/div[6]/header/a"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_lab_tests_page(self):

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("lab-tests")
        )

        assert "lab-tests" in self.driver.current_url

    def select_vital_organs(self):

        # Scroll slowly down
        self.driver.execute_script(
            "window.scrollTo(0, 1500)"
        )

        # Wait for View All button
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.VIEW_ALL_VITAL_ORGANS
            )
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        # Click using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )