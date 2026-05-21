import pytest
import os

from utils.driver_factory import DriverFactory
from utils.excel_reader import ExcelReader
from utils.logger import LogGenerator

from pages.home_page import HomePage
from pages.lab_tests_page import LabTestsPage
from pages.vital_organs_page import VitalOrgansPage


# Create screenshots directory
os.makedirs("screenshots", exist_ok=True)

# Read Excel data
data = ExcelReader.get_test_data(
    "testdata/testdata.xlsx"
)


@pytest.mark.parametrize(
    "package_name,mobile_number,card_name,card_number,expiry_date,cvv",
    zip(
        data["package_name"],
        data["mobile_number"],
        data["card_name"],
        data["card_number"],
        data["expiry_date"],
        data["cvv"]
    ),
    ids=data["package_name"]
)
def test_vital_organs(
        package_name,
        mobile_number,
        card_name,
        card_number,
        expiry_date,
        cvv
):

    logger = LogGenerator.loggen()

    logger.info("========== TEST STARTED ==========")

    driver = DriverFactory.get_driver()

    home = HomePage(driver)
    lab = LabTestsPage(driver)
    vital = VitalOrgansPage(driver)

    try:

        logger.info("Opening Home Page")

        home.open_home_page()

        home.verify_home_page()

        logger.info("Home Page Verified")

        home.click_lab_tests()

        logger.info("Lab Tests Clicked")

        lab.verify_lab_tests_page()

        logger.info("Lab Tests Page Verified")

        lab.select_vital_organs()

        logger.info("Vital Organs Selected")

        vital.verify_vital_organs_page()

        logger.info("Vital Organs Page Verified")

        vital.open_thyroid_card()

        logger.info("Thyroid Card Opened")

        vital.click_add_button()

        logger.info("Add Button Clicked")

        vital.click_go_to_cart()

        logger.info("Go To Cart Clicked")

        vital.login_with_mobile(
            mobile_number
        )

        logger.info("Mobile Number Entered")

        vital.click_verify_button()

        logger.info("OTP Verified")

        vital.click_go_to_cart()

        logger.info("Go To Cart Clicked Again")

        vital.select_patient_checkbox()

        logger.info("Patient Checkbox Selected")

        vital.click_select_slot_button()

        logger.info("Select Slot Clicked")

        vital.click_review_cart_button()

        logger.info("Review Cart Clicked")

        vital.click_proceed_to_pay()

        logger.info("Proceed To Pay Clicked")

        vital.click_credit_debit_card_section()

        logger.info("Credit/Debit Card Section Clicked")

        vital.enter_card_details(
            card_name,
            card_number,
            expiry_date,
            cvv
        )

        logger.info("Card Details Entered")

        vital.click_pay_button()

        logger.info("Pay Button Clicked")

        # Success screenshot
        screenshot_name = (
            f"screenshots/"
            f"{package_name.replace(' ', '_')}_success.png"
        )

        driver.save_screenshot(
            screenshot_name
        )

        logger.info(
            f"Success Screenshot Saved: {screenshot_name}"
        )

        logger.info("========== TEST PASSED ==========")

    except Exception as e:

        screenshot_name = (
            f"screenshots/"
            f"{package_name.replace(' ', '_')}_failure.png"
        )

        driver.save_screenshot(
            screenshot_name
        )

        logger.error(
            f"Failure Screenshot Saved: {screenshot_name}"
        )

        logger.error(
            f"Test Failed: {str(e)}"
        )

        print("Test Failed:", e)

        raise

    finally:

        logger.info("Closing Browser")

        driver.quit()

        logger.info("========== TEST ENDED ==========")