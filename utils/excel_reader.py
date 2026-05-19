import pandas as pd


class ExcelReader:

    @staticmethod
    def get_test_data(file_path):

        data = pd.read_excel(
            file_path,
            engine="openpyxl"
        )

        return data