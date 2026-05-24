from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigReader.get_browser()

        if browser.lower() == "chrome":

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                )
            )

            driver.maximize_window()

            driver.implicitly_wait(
                ConfigReader.get_timeout()
            )

            return driver