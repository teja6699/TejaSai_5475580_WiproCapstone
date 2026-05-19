import pytest

from utils.driver_factory import DriverFactory
from utils.excel_reader import ExcelReader

from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage
from pages.vital_organs_page import VitalOrgansPage


data = ExcelReader.get_test_data(
    "testdata/testdata.xlsx"
)


@pytest.mark.parametrize(
    "package_name",
    data["package_name"]
)
def test_vital_organs(package_name):

    driver = DriverFactory.get_driver()

    home = HomePage(driver)
    lab = LabTestsPage(driver)
    vital = VitalOrgansPage(driver)

    try:

        # Open Apollo Pharmacy
        home.open_home_page()

        # Verify homepage
        home.verify_home_page()

        # Navigate to Lab Tests
        home.click_lab_tests()

        # Verify lab tests page
        lab.verify_lab_tests_page()

        # Select Vital Organs
        lab.select_vital_organs()

        # Verify Vital Organs page
        vital.verify_vital_organs_page()

        # Verify package cards
        vital.verify_packages_displayed()

        print(f"Testing Package: {package_name}")

        # Screenshot
        driver.save_screenshot(
            f"screenshots/{package_name}.png"
        )

    except Exception as e:

        driver.save_screenshot(
            f"screenshots/error_{package_name}.png"
        )

        print("Test Failed:", e)

        raise

    finally:

        driver.quit()