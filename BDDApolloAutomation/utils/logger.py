import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger(
            "ApolloBDD"
        )

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            file_handler = logging.FileHandler(
                "logs/test.log",
                mode="a"
            )

            formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(message)s",
                "%m/%d/%Y %I:%M:%S %p"
            )

            file_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

        return logger