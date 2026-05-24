import os
import allure

from allure_commons.types import AttachmentType

from utils.excel_reader import ExcelReader
from utils.driver_factory import DriverFactory
from utils.logger import LogGenerator


# Create required folders automatically
os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports/allure-results", exist_ok=True)
os.makedirs("logs", exist_ok=True)


def before_all(context):

    context.logger = LogGenerator.loggen()

    context.logger.info(
        "========= Test Execution Started ========="
    )

    context.testdata = ExcelReader.get_test_data(
        "testdata/testdata.xlsx"
    )


def before_scenario(context, scenario):

    context.driver = DriverFactory.get_driver()

    context.logger.info(
        f"Scenario Started: {scenario.name}"
    )

    # Add scenario info to allure
    allure.dynamic.feature(
        scenario.feature.name
    )

    allure.dynamic.story(
        scenario.name
    )


def after_step(context, step):

    # Capture screenshot after every step
    screenshot = context.driver.get_screenshot_as_png()

    allure.attach(
        screenshot,
        name=f"Step Screenshot - {step.name}",
        attachment_type=AttachmentType.PNG
    )

    context.logger.info(
        f"Step Executed: {step.name} | Status: {step.status}"
    )


def after_scenario(context, scenario):

    if scenario.status == "failed":

        screenshot_path = (
            f"screenshots/{scenario.name}.png"
        )

        context.driver.save_screenshot(
            screenshot_path
        )

        # Attach failed screenshot to allure
        with open(screenshot_path, "rb") as image:

            allure.attach(
                image.read(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )

        context.logger.error(
            f"Scenario Failed: {scenario.name}"
        )

    else:

        context.logger.info(
            f"Scenario Passed: {scenario.name}"
        )

    context.driver.quit()

    context.logger.info(
        f"Scenario Ended: {scenario.name}"
    )


def after_all(context):

    context.logger.info(
        "========= Test Execution Completed ========="
    )