from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import ConfigReader


class HomePage:

    LAB_TESTS = (
        By.XPATH,
        "//a[contains(@href,'lab-tests')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):

        self.driver.get(
            ConfigReader.get_base_url()
        )

    def verify_home_page(self):

        assert "Apollo" in self.driver.title

    def click_lab_tests(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.LAB_TESTS
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )