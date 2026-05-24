import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        # Create logs directory
        log_dir = "logs"

        if not os.path.exists(log_dir):

            os.makedirs(log_dir)

        logger = logging.getLogger(
            "ApolloAutomation"
        )

        logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
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