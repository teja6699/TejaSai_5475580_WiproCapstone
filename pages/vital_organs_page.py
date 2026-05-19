from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VitalOrgansPage:

    PACKAGE_CARDS = (
        By.XPATH,
        "//div[contains(@class,'PackageCard')]"
    )

    SEARCH_BOX = (
        By.XPATH,
        "//input[@placeholder='Search Tests & Packages']"
    )

    ADD_TO_CART = (
        By.XPATH,
        "(//button[contains(text(),'Add')])[1]"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_vital_organs_page(self):

        assert "vital-organs" in self.driver.current_url

    def verify_packages_displayed(self):

        packages = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                self.PACKAGE_CARDS
            )
        )

        assert len(packages) > 0

    def search_package(self, package_name):

        search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search.clear()
        search.send_keys(package_name)

    def add_first_package_to_cart(self):

        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART
            )
        )

        button.click()