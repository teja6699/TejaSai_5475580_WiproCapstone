import pytest
import os

from utils.driver_factory import DriverFactory
from utils.excel_reader import ExcelReader

from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage
from pages.vital_organs_page import VitalOrgansPage


os.makedirs("screenshots", exist_ok=True)

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

        home.open_home_page()

        home.verify_home_page()

        home.click_lab_tests()

        lab.verify_lab_tests_page()

        lab.select_vital_organs()

        vital.verify_vital_organs_page()

        vital.open_thyroid_card()

        vital.click_add_button()

        vital.click_go_to_cart()

        vital.login_with_mobile()

        driver.save_screenshot(
            f"screenshots/{package_name}_success.png"
        )

    except Exception as e:

        driver.save_screenshot(
            f"screenshots/{package_name}_failure.png"
        )

        print("Test Failed:", e)

        raise

    finally:

        driver.quit()