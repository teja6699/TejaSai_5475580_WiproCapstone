from utils.driver_factory import DriverFactory
from utils.logger import LogGenerator

from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage


def test_navigation_to_lab_tests():

    logger = LogGenerator.loggen()
    print(logger)
    print(logger.handlers)

    logger.info("========== Navigation Test Started ==========")

    driver = DriverFactory.get_driver()

    home = HomePage(driver)

    lab = LabTestsPage(driver)

    try:

        logger.info("Opening Home Page")

        home.open_home_page()

        home.verify_home_page()

        logger.info("Home Page Verified")

        home.click_lab_tests()

        logger.info("Lab Tests Clicked")

        lab.verify_lab_tests_page()

        logger.info("Lab Tests Page Verified")

        logger.info("========== Navigation Test Passed ==========")

    except Exception as e:

        logger.error(f"Navigation Test Failed: {str(e)}")

        raise

    finally:

        driver.quit()

        logger.info("Browser Closed")

        logger.info("========== Navigation Test Ended ==========")