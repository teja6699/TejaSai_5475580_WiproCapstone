from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage


def test_navigation_to_lab_tests():

    driver = DriverFactory.get_driver()

    home = HomePage(driver)
    lab = LabTestsPage(driver)

    home.open_home_page()

    home.verify_home_page()

    home.click_lab_tests()

    lab.verify_lab_tests_page()

    driver.quit()