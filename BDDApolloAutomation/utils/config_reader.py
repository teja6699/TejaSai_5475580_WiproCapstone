import configparser


class ConfigReader:

    config = configparser.ConfigParser()

    config.read("config.properties")

    @staticmethod
    def get_browser():
        return ConfigReader.config.get(
            "DEFAULT",
            "browser"
        )

    @staticmethod
    def get_base_url():
        return ConfigReader.config.get(
            "DEFAULT",
            "base_url"
        )

    @staticmethod
    def get_timeout():
        return ConfigReader.config.getint(
            "DEFAULT",
            "timeout"
        )